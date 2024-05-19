# ffmpegApi.py
# 实现了FFmpeg的命令行接口，可以对视频进行各种操作，如截取、合并、转码、截图等。

import subprocess
import os
import logging
import time
import threading

from modules.config import ffpath

class FFmpeg:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(self, 
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
            # logging.info("ffmpegapi守卫线程运行中")
            time.sleep(1)
        logging.info("ffmpegapi检测到中断请求")
        self.interrupt_run()
    def interrupt_run(self):
        if self.interrupt_flag:
            # 如果收到中断信号，则终止FFmpeg进程
            logging.info("尝试终止FFmpeg进程")
            self.p.terminate()
            self.p.wait(timeout=5)
            if self.p.poll() is None:
                self.p.kill()
            if callable(self.callback):
                self.callback()
            self.interrupt_flag = False
            logging.info("FFmpeg进程强制终止")
        logging.info("ffmpegapi中断请求已处理")
        

    # 定义run方法来执行FFmpeg命令
    def run(self, 
        cmd
    ):
        t = None  # 守卫线程预留在try之外
        try:
            cmd = [self.ffmpeg_path] + cmd
            cmd_str = ' '.join(cmd)
            logging.info(f"尝试执行：{cmd_str}")
            # 创建线程运行FFmpeg命令
            self.p = subprocess.Popen(
                cmd_str, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT
            )
            # 创建线程检测中断信号
            t = threading.Thread(target=self.check_interrupt_flag)
            t.daemon = True
            t.start()
            if t.is_alive():
                logging.info('启动守卫线程成功')
            else:
                logging.error('启动守卫线程失败')
            # 实时输出FFmpeg命令的执行信息
            while True:
                line = self.p.stdout.readline().decode('utf-8')
                if not line:
                    # 如果没有更多输出，检查进程是否已经结束
                    if self.p.poll() is not None:
                        break
                    else:
                        continue
                logging.info(line.strip())  # 打印输出信息
            # 如果出错，获取错误信息
            out, err = self.p.communicate()
            if self.p.returncode != 0:
                logging.info(f"命令执行失败，错误信息：{err.decode('utf-8')}")
                raise Exception(err.decode('utf-8'))
        except FileNotFoundError as fnf_error:
            logging.error(f"找不到ffmpeg或ffprobe命令，请检查ffmpeg_path和ffprobe_path是否正确配置。")
            raise fnf_error
        except PermissionError as p_error:
            logging.error(f"ffmpeg或ffprobe命令没有执行权限，请检查ffmpeg_path和ffprobe_path是否正确配置。")
            raise p_error
        except Exception as e:
            logging.error(f"执行FFmpeg命令失败：{e}")
            raise e
        finally:
            logging.info("FFmpeg命令执行完成")
            if t and t.is_alive():
                self.interrupt_flag = True  # 设置中断标志
                t.join()
                self.interrupt_flag = False  # 重置中断标志
                logging.info("守卫线程退出")
    
    # 输出ffmpeg的版本信息
    def version(self):
        return self.run(['-version'])
    
    # 获取视频时长
    def get_duration(self, 
        input_file
    ):
        cmd1 = [
            self.ffprobe_path, 
            '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', 
            input_file
        ]
        logging.info("执行：" + ' '.join(cmd1))
        result = subprocess.run(cmd1, capture_output=True, text=True)
        # 检查输出是否为空
        stdout = result.stdout.strip()
        if not stdout:
            logging.warning("ffprobe 输出为空，无法获取视频持续时间")
            return None  # 或者返回一个默认值
        try:
            duration = float(stdout)
            logging.info("视频总秒数为：" + str(duration))
            return duration
        except ValueError as e:
            logging.error("转换视频持续时间为浮点数时出错：", str(e))
            raise e  # 或者返回一个错误信息

    # 计算时间字符串
    def time_calculate(self, duration, end):
        logging.info(end)
        # 转换为浮点数进行计算
        hours, minutes, seconds, milliseconds = end.split(':')
        hours = float(hours)
        minutes = float(minutes)
        end_float = hours * 3600 + minutes * 60 + float(seconds)
        end_float += float(milliseconds) / 1000
        end_time_float = duration - end_float
        logging.info("结束时间点为：", end_time_float)
        # 浮点数结果转换为字符串格式
        m, s = divmod(end_time_float, 60)
        h, m = divmod(m, 60)
        end_time = "%02d:%02d:%06.3f" % (h, m, s)
        logging.info("结束时间点为：", end_time)
        return end_time

    # 截取视频(输入文件夹)
    def extract_video(self, 
        input_folder, 
        start_time, 
        end, 
        output_folder, 
        encoder='-c:v copy -c:a copy', 
        overwrite='-y'
    ):
        # 遍历文件夹中的所有mp4视频文件
        for file in os.listdir(input_folder):
            if file.endswith('.mp4'):
                input_file = os.path.join(input_folder, file)
                # 检测输出文件夹是否存在，不存在则创建
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_file = os.path.join(output_folder, file)
                # 读取视频的总时长
                duration = self.get_duration(input_file)
                # 将end时间转换为秒数浮点数计算后返回结束时间字符串
                end_time = self.time_calculate(duration, end)
                # 调用ffmpeg命令行工具，对视频进行截取
                cmd = [
                    '-hide_banner',
                    overwrite, 
                    '-ss', start_time, 
                    '-to', end_time, 
                    '-accurate_seek', 
                    '-i', f'"{input_file}"',  
                    encoder, 
                    f'"{output_file}"']
                # 打印最终输入命令行的cmd指令，从列表转换为字符串
                # logging.info("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
                self.run(cmd)
                logging.info(file + '视频截取完成')
            else:
                logging.info(file + '不是mp4文件，跳过')

    # 截取视频(输入文件)
    def extract_video_single(self, 
        input_file, 
        output_file, 
        start_time, 
        end, 
        encoder='-c:v copy -c:a copy', 
        overwrite='-y'
    ):
        start_time = start_time[:7] + '.' + start_time[8:]  # 转换为ffmpeg格式的时间格式
        # 读取视频的总时长
        duration = self.get_duration(input_file)
        # 将end时间转换为秒数浮点数计算后返回结束时间字符串
        end_time = self.time_calculate(duration, end)
        # 调用ffmpeg命令行工具，对视频进行截取
        cmd = [
            '-hide_banner',
            overwrite, 
            '-ss', start_time, 
            '-to', end_time, 
            '-accurate_seek', 
            '-i', f'"{input_file}"',  
            encoder, 
            f'"{output_file}"']
        # 打印最终输入命令行的cmd指令，从列表转换为字符串
        # logging.info("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频截取完成')

    def cut_video(self, 
        input_file, 
        output_file,
        start_time, 
        end_time, 
        encoder='-c:v copy -c:a copy', 
        overwrite='-y'
    ):
        start_time = start_time[:7] + '.' + start_time[8:]  # 转换为ffmpeg格式的时间格式
        end_time = end_time[:7] + '.' + end_time[8:]  # 转换为ffmpeg格式的时间格式
        cmd = [
            '-hide_banner',
            overwrite, 
            '-ss', start_time, 
            '-to', end_time, 
            '-accurate_seek', 
            '-i', f'"{input_file}"',  
            encoder, 
            f'"{output_file}"']
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频截取完成')

    # 合并视频(输入文件夹)
    def merge_video_folder(self, input_folder, input_file1, input_file2, output_folder, encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2', overwrite='-y'):
        # 遍历文件夹中的所有mp4视频文件
        for file in os.listdir(input_folder):
            if file.endswith('.mp4'):
                input_file = os.path.join(input_folder, file)
                # 检测输出文件夹是否存在，不存在则创建
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_file = os.path.join(output_folder, file)
                # 调用ffmpeg命令行工具，对视频进行合并
                cmd = [
                    '-hide_banner',
                    overwrite, 
                    '-i', f'"{input_file1}"', 
                    '-i', f'"{input_file}"', 
                    '-i', f'"{input_file2}"', 
                    '-filter_complex', 
                    '"[0:v]fps=30,scale=1280:720,setsar=1[v0];[1:v]fps=30,scale=1280:720,setsar=1[v1];[2:v]fps=30,scale=1280:720,setsar=1[v2];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[vout][aout]" -map "[vout]" -map "[aout]"', 
                    encoder, 
                    f'"{output_file}"']
                # 打印最终输入命令行的cmd指令，从列表转换为字符串
                # logging.info("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
                self.run(cmd)
                logging.info(file + '视频合并完成')
            else:
                logging.info(file + '不是mp4文件，跳过')
    
    # 合并视频(输入3个文件)
    def merge_video(self, 
        input_file, 
        output_file, 
        input_file1, 
        input_file2, 
        encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2', 
        resolution='1920:1080', 
        fps='30', 
        overwrite='-y'
    ):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', f'"{input_file1}"', 
            '-i', f'"{input_file}"', 
            '-i', f'"{input_file2}"', 
            '-filter_complex', 
            f'"[0:v]fps={fps},scale={resolution},setsar=1[v0];[1:v]fps={fps},scale={resolution},setsar=1[v1];[2:v]fps={fps},scale={resolution},setsar=1[v2];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[vout][aout]" -map "[vout]" -map "[aout]"', 
            encoder, 
            f'"{output_file}"']
        # 打印最终输入命令行的cmd指令，从列表转换为字符串
        # logging.info("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频截取完成')

    # 合并视频(输入2个文件)
    def merge_video_two(self, 
        op_file, 
        output_file, 
        ed_file, 
        encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2', 
        resolution='1920:1080', 
        fps='30', 
        overwrite='-y'
    ):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', f'"{op_file}"', 
            '-i', f'"{ed_file}"', 
            '-filter_complex', 
            f'"[0:v]fps={fps},scale={resolution},setsar=1[v0];[1:v]fps={fps},scale={resolution},setsar=1[v1];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[vout][aout]" -map "[vout]" -map "[aout]"', 
            encoder, 
            f'"{output_file}"']
        # 打印最终输入命令行的cmd指令，从列表转换为字符串
        # logging.info("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
        self.run(cmd)
        file = os.path.basename(output_file)
        logging.info(file + '视频合并完成')

    # 合并视频(concat)
    # def concat_video(self, 
    #     input_file1, 
    #     input_file2, 
    #     output_file, 

    # 音频转码
    def audio_encode(self, 
        input_file, 
        output_file, 
        encoder = r'-acodec aac -b:a 128k ', 
        overwrite='-y'):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', 
            f'"{input_file}"', 
            encoder, 
            f'"{output_file}"'
        ]
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '音频转码完成')

    # 视频转码
    def video_encode(self, 
        input_file, 
        output_file, 
        encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k', 
        overwrite='-y'):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', 
            f'"{input_file}"', 
            encoder, 
            f'"{output_file}"'
        ]
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频转码完成')

    # 加速转码
    def accelerated_encode(self, 
        input_file, 
        output_file, 
        rate=1,
        encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k', 
        overwrite='-y'):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', 
            f'"{input_file}"', 
            f'-filter_complex "[0:v]setpts=PTS/{rate}[v];[0:a]atempo={rate}[a]" -map "[v]" -map "[a]"',
            encoder, 
            f'"{output_file}"'
        ]
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频加速完成')

    # 音视频字幕混合
    def avsmix_encode(self, 
        input_file, 
        output_file, 
        audio,
        subtitle,
        encoder = r'-vcodec libx264 -preset medium -crf 23 -acodec aac -b:a 128k', 
        overwrite='-y'):
        cmd = [
            '-hide_banner',
            overwrite, 
            '-i', 
            f'"{input_file}"', 
            audio,
            subtitle, 
            encoder,
            f'"{output_file}"'
        ]
        self.run(cmd)
        file = os.path.basename(input_file)
        logging.info(file + '视频字幕混合完成')