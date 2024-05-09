# ffmpegApi.py

import asyncio
import logging
import os
# import time

from config import ffpath


class FFmpegHandler:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(self, 
        ffmpeg_path=ffpath.ffmpeg_path,
        ffprobe_path=ffpath.ffprobe_path
    ):
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path

    # 使用异步方式执行FFmpeg命令
    async def run_async(self, 
        cmd
    ):
        try:
            cmd_args = cmd.split(' ')
            logging.info(f"尝试执行：{cmd}")
            # 创建子进程，使用 asyncio 来异步执行命令
            p = await asyncio.create_subprocess_exec(
                *cmd_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT)
            # 从stdout异步读取，并打印到控制台
            while True:
                line = await p.stdout.readline()
                if not line:
                    # 如果没有更多输出，检查进程是否已经结束
                    if p.returncode is not None:
                        break # 进程已结束，跳出循环
                    else:
                        # 等待一段时间后再次尝试读取
                        await asyncio.sleep(0.1)
                        continue
                # 打印输出到控制台
                line_str = line.decode('utf-8', errors='ignore').strip()
                logging.info(line_str)
            # 获取命令行输出
            out, err = await p.communicate()
            if p.returncode != 0:
                logging.error(
                    f"命令执行失败，错误信息：{err.decode('utf-8', errors='ignore')}")
                raise Exception(
                    f"命令执行失败，命令：{cmd}，错误信息：{err.decode('utf-8', errors='ignore')}"
                )
            else:
                logging.info(f"命令执行成功，命令：{cmd}")
        except FileNotFoundError as fnf_error:
            logging.error(f"文件未找到错误：{fnf_error}")
            raise fnf_error
        except PermissionError as p_error:
            logging.error(f"权限错误：{p_error}")
            raise p_error
        except Exception as e:
            logging.error(f"命令执行失败，错误信息：{e}")
            raise e

    # 输出ffmpeg的版本信息
    def version(self
    ):
        cmd = f'{self.ffmpeg_path} -version'
        coro = self.run_async(cmd)
        asyncio.run(coro)
        return

    # 获取视频的时长
    async def get_duration(self, 
        input_file, 
    ):
        cmd1 = [
            self.ffprobe_path, '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', input_file
        ]
        logging.info(f"尝试执行：{' '.join(cmd1)}")
        # 使用 asyncio 来异步执行命令
        process = await asyncio.create_subprocess_exec(
            *cmd1,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        # 等待进程完成并获取输出
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise Exception(f"命令执行失败，错误信息：{stderr.strip()}")
        # 假设持续时间直接在stdout中，我们解码并返回
        duration = stdout.strip()
        try:
            duration = float(duration)
        except ValueError:
            raise ValueError(f"无法将视频时长'{duration}'转换为浮点数。")
        logging.info(f"视频时长为：{duration}秒")
        return duration

    def time_calculate(self, 
        duration, 
        end
    ):
        # 转换为浮点数进行计算
        hours, minutes, seconds_milliseconds = end.split(':')
        seconds, milliseconds = seconds_milliseconds.split('.')
        hours = float(hours)
        minutes = float(minutes)
        end_float = hours * 3600 + minutes * 60 + float(seconds)
        end_float += float(milliseconds) / 1000
        end_time_float = duration - end_float
        print("结束时间点为：", end_time_float)
        # 浮点数结果转换为字符串格式
        m, s = divmod(end_time_float, 60)
        h, m = divmod(m, 60)
        end_time = "%02d:%02d:%06.3f" % (h, m, s)
        print("结束时间点为：", end_time)
        return end_time

    # 截取视频
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
                coro1 = self.get_duration(input_file)
                duration = asyncio.run(coro1)
                # 将end时间转换为秒数浮点数计算后返回结束时间字符串
                end_time = self.time_calculate(duration, end)

                # 调用ffmpeg命令行工具，对视频进行截取
                # cmd = [
                #     self.ffmpeg_path, '-ss', start_time, '-to', end_time, '-accurate_seek', '-i',
                #     f'"{input_file}"', encoder, f'"{output_file}"'
                # ]
                cmd = f'{self.ffmpeg_path} {overwrite} -ss {start_time} -to {end_time} -accurate_seek -i {input_file} {encoder} {output_file}'
                coro = self.run_async(cmd)
                asyncio.run(coro)
                logging.info(file + '视频截取完成')
            else:
                logging.info(file + '不是mp4文件，跳过')
        return

    # 合并视频
    def merge_video(self,
        input_folder,
        input_file1,
        input_file2,
        output_folder,
        encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2',
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

                # 调用ffmpeg命令行工具，对视频进行合并
                # cmd = [
                #     '-i', f'"{input_file1}"', '-i', f'"{input_file}"', '-i',
                #     f'"{input_file2}"', '-filter_complex',
                #     '"[0:v]fps=30,scale=1280:720,setsar=1[v0];[1:v]fps=30,scale=1280:720,setsar=1[v1];[2:v]fps=30,scale=1280:720,setsar=1[v2];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[vout][aout]" -map "[vout]" -map "[aout]"',
                #     encoder, f'"{output_file}"'
                # ]
                filter_complex = f'[0:v]fps=30,scale=1280:720,setsar=1[v0];[1:v]fps=30,scale=1280:720,setsar=1[v1];[2:v]fps=30,scale=1280:720,setsar=1[v2];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[vout][aout]'
                cmd = f'{self.ffmpeg_path} {overwrite} -i {input_file1} -i {input_file} -i {input_file2} -filter_complex {filter_complex} -map [vout] -map [aout] {encoder} {output_file}'
                coro = self.run_async(cmd)
                asyncio.run(coro)
                logging.info(file + '视频合并完成')
            else:
                logging.info(file + '不是mp4文件，跳过')

# Create 20240506 使用subporcess模块实现FFmpeg命令行接口
# Update 20240508 优化代码结构，使用asyncio模块实现异步执行FFmpeg命令