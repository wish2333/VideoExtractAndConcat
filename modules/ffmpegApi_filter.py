# ffmpegApi.py
# 实现了FFmpeg的命令行接口，可以对视频进行各种操作，如截取、合并、转码、截图等。

import subprocess
import os
from modules.logger_config import logger
import time
import threading
from modules.config import ffpath
import configparser


class FFmpegFilter:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(
            self,
            ffmpeg_path=ffpath.ffmpeg_path,
            ffprobe_path=ffpath.ffprobe_path,
            interrupt_flag=False,  # 中断标志
            callback=None,  # 回调函数
    ):
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path
        self.interrupt_flag = interrupt_flag
        self.callback = callback

    def update_interrupt_flag(self, flag=True):
        self.interrupt_flag = flag

    def check_interrupt_flag(self):
        while not self.interrupt_flag:
            # logger.info("ffmpegapi守卫线程运行中")
            time.sleep(1)
        logger.debug("ffmpegapi检测到中断请求")
        self.interrupt_run()

    def interrupt_run(self):
        if self.interrupt_flag:
            # 如果收到中断信号，则终止FFmpeg进程
            logger.debug("尝试终止FFmpeg进程")
            self.p.terminate()
            self.p.wait(timeout=5)
            if self.p.poll() is None:
                self.p.kill()
            if callable(self.callback):
                self.callback()
            self.interrupt_flag = False
            logger.debug("FFmpeg进程强制终止")
        logger.debug("ffmpegapi中断请求已处理")

    # 定义run方法来执行FFmpeg命令
    def run(self, cmd):
        t = None  # 守卫线程预留在try之外
        try:
            cmd = [self.ffmpeg_path] + cmd
            cmd_str = ' '.join(cmd)
            logger.info(f"尝试执行：{cmd_str}")
            # 创建线程运行FFmpeg命令
            self.p = subprocess.Popen(cmd_str,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      encoding='utf-8',
                                      text=True)
            # 创建线程检测中断信号
            t = threading.Thread(target=self.check_interrupt_flag)
            t.daemon = True
            t.start()
            if t.is_alive():
                logger.debug('启动守卫线程成功')
            else:
                logger.error('启动守卫线程失败')
            # 实时输出FFmpeg命令的执行信息
            while True:
                line = self.p.stdout.readline()
                if not line:
                    # 如果没有更多输出，检查进程是否已经结束
                    if self.p.poll() is not None:
                        break
                    else:
                        continue
                logger.debug(line.strip())  # 打印输出信息
                print(line.strip(), end='\r')  # 打印输出信息
            # 如果出错，获取错误信息
            out, err = self.p.communicate()
            if self.p.returncode != 0:
                logger.error(f"命令执行失败，错误信息：{err}")
                raise Exception(err)
        except FileNotFoundError as fnf_error:
            logger.error(
                f"找不到ffmpeg或ffprobe命令，请检查ffmpeg_path和ffprobe_path是否正确配置。")
            raise fnf_error
        except PermissionError as p_error:
            logger.error(
                f"ffmpeg或ffprobe命令没有执行权限，请检查ffmpeg_path和ffprobe_path是否正确配置。")
            raise p_error
        except Exception as e:
            logger.error(f"执行FFmpeg命令失败：{e}")
            raise e
        finally:
            logger.info("FFmpeg命令执行完成")
            if t and t.is_alive():
                self.interrupt_flag = True  # 设置中断标志
                t.join()
                self.interrupt_flag = False  # 重置中断标志
                logger.debug("守卫线程退出")

    # 获取视频时长
    def get_duration(self, input_file):
        cmd1 = [
            self.ffprobe_path, '-v', 'error', '-show_entries',
            'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
            input_file
        ]
        logger.debug("执行：" + ' '.join(cmd1))
        result = subprocess.run(cmd1, capture_output=True, text=True)
        # 检查输出是否为空
        stdout = result.stdout.strip()
        if not stdout:
            logger.error("ffprobe 输出为空，无法获取视频持续时间")
            return None  # 或者返回一个默认值
        try:
            duration = float(stdout)
            logger.debug("视频总秒数为：" + str(duration))
            return duration
        except ValueError as e:
            logger.error("转换视频持续时间为浮点数时出错：", str(e))
            raise e  # 或者返回一个错误信息

    # 横竖转换Filter
    def rotate_filter(self, image_, scale_x='1080', scale_y='1920', input=None):
            if image_[0] == 'H2V-I':
                # ffmpeg 命令：横屏转竖屏，视频宽边保持，图片缩放，视频下方叠加图片，空白区域显示为透明
                if input != 'flag':
                    duration = self.get_duration(input)
                else:
                    duration = '@duration'
                filter = f'-filter_complex "[1:v]scale={scale_x}:{scale_y},setsar=1,loop=-1:size={duration}[bg];[0:v]scale={scale_x}:-2,setsar=1[v];[bg][v]overlay=(W-w)/2:(H-h)/2:shortest=1[vout]" -map "[vout]" -map 0:a'
                filter = f'-filter_complex "[1:v]scale={scale_x}:{scale_y},setsar=1,loop=-1:size={duration}[bg];[0:v]scale={scale_x}:-2,setsar=1[v];[bg][v]overlay=(W-w)/2:(H-h)/2:shortest=1[vout]" -map "[vout]" -map 0:a'
            elif image_[0] == 'H2V-T':
                # ffmpeg 命令：横屏转竖屏，背景叠加模糊视频
                filter = f'-filter_complex "[0:v]split=2[v_main][v_bg];[v_main]scale=w={scale_x}:h=-1,setsar=1,pad={scale_x}:{scale_y}:(ow-iw)/2:(oh-ih)/2:color=black@0[v_scaled];[v_bg]crop=ih*{float(scale_x)/float(scale_y)}:ih,boxblur=10:5,scale={scale_x}:{scale_y}[bg_blurred];[bg_blurred][v_scaled]overlay=(W-w)/2:(H-h)/2:shortest=1[vout]" -map "[vout]" -map 0:a'
            elif image_[0] == 'H2V-B':
                # ffmpeg 命令：横屏转竖屏，不叠加图片，空白区域显示为黑色
                filter = f'-filter_complex "[0:v]scale=w={scale_x}:h=-1,setsar=1,pad={scale_x}:{scale_y}:(ow-iw)/2:(oh-ih)/2:black[vout]" -map "[vout]" -map 0:a'
            elif image_[0] == 'V2H-I':
                # ffmpeg 命令：竖屏转横屏，视频宽边保持，图片缩放，视频下方叠加图片，空白区域显示为透明
                if input != 'flag':
                    duration = self.get_duration(input)
                else:
                    duration = '@duration'
                filter = f'-filter_complex "[1:v]scale={scale_x}:{scale_y},setsar=1,loop=-1:size={duration}[bg];[0:v]scale=-2:{scale_y},setsar=1[v];[bg][v]overlay=(W-w)/2:(H-h)/2:shortest=1[vout]" -map "[vout]" -map 0:a'
            elif image_[0] == 'V2H-T':
                # ffmpeg 命令：竖屏转横屏，背景叠加模糊视频
                filter = f'-filter_complex "[0:v]split=2[v_main][v_bg];[v_main]scale=w=-1:h={scale_y},setsar=1,pad={scale_x}:{scale_y}:(ow-iw)/2:(oh-ih)/2:color=black@0[v_scaled];[v_bg]crop=iw:iw*{float(scale_y)/float(scale_x)},boxblur=10:5,scale={scale_x}:{scale_y}[bg_blurred];[bg_blurred][v_scaled]overlay=(W-w)/2:(H-h)/2:shortest=1[vout]" -map "[vout]" -map 0:a'
            elif image_[0] == 'V2H-B':
                # ffmpeg 命令：竖屏转横屏，不叠加图片，空白区域显示为黑色
                filter = f'-filter_complex "[0:v]scale=-1:h={scale_y},setsar=1,pad={scale_x}:{scale_y}:(ow-iw)/2:(oh-ih)/2:black[vout]" -map "[vout]" -map 0:a'
            else:
                return
            return filter

    # 横屏转竖屏
    def rotate_video(
            self,
            input,
            output,
            image_,
            audio_filter=False,
            scale_x='1080',
            scale_y='1920',
            encoder='-c:v libx264 -preset medium -crf 23 -c:a aac -b:a 256k -ar 44100 -ac 2'):

        # 构建cmd
        cmd = ['-hide_banner', '-y', '-i', f'"{input}"']

        # 旋转处理
    
        rotate_filter = self.rotate_filter(image_, scale_x, scale_y)
        if rotate_filter is not None:
            if image_[0] == 'V2H-I' or image_[0] == 'H2V-I':
                cmd += ['-i', f'{image_[1]}']
            cmd += [rotate_filter]

        # 音频处理
        if audio_filter:
            cmd += ['-af', 'loudnorm=i=-16.0:lra=5.0:tp=-0.3']

        # 编码处理
        cmd += [encoder, '-max_muxing_queue_size 1024', f'"{output}"']
        # self.run(cmd)
        return cmd


# 测试用例
# f = FFmpeg(r'Q:\Git\FFmpeg-python\FFmpeg\bin\ffmpeg.exe', r'Q:\Git\FFmpeg-python\FFmpeg\bin\ffprobe.exe')
# input = r'Q:\Git\FFmpeg-python\测试视频\test-input\【1080P_4月】神之塔 OP&ED TV size - 1.OP(Av412589437,P1).mp4'
# output = r'Q:\Git\FFmpeg-python\测试视频\output\【1080P_4月】神之塔 OP&ED TV size - 1.OP(Av412589437,P1).mp4'
# image_ = ['T', r'F:\资源-图片\收藏\2021-12\45529923_p0.jpg']
# encoder = '-c:v h264_nvenc -preset medium -crf 23 -c:a aac -b:a 256k'
# p = f.rotate_video(input, output, image_)
# p_str = ' '.join(p)
# print(p)
# print(p_str)
