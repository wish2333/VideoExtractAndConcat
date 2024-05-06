# ffmpegApi.py
# 实现了FFmpeg的命令行接口，可以对视频进行各种操作，如截取、合并、转码、截图等。

import subprocess
import os
import time

class FFmpeg:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path

    # 定义run方法来执行FFmpeg命令
    def run(self, cmd):
        """
        执行给定的FFmpeg命令，并返回其输出。

        参数:
        - cmd: 一个列表，包含要执行的FFmpeg命令及其参数。

        返回值:
        - 执行命令的标准输出（字符串）。

        抛出:
        - Exception: 如果命令执行失败（返回码非0），则抛出包含错误信息的异常。
        """
        cmd = [self.ffmpeg_path] + cmd
        cmd_str = ' '.join(cmd)
        p = subprocess.Popen(cmd_str, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 打印执行的命令行
        print("执行：" + cmd_str)
        # 等待命令执行完成
        out, err = p.communicate()
        # 如果命令执行失败，则抛出异常
        if p.returncode != 0:
            raise Exception(err.decode('utf-8'))
        return out.decode('utf-8')

    # 输出ffmpeg的版本信息
    def version(self):
        return self.run(['-version'])
    
    # 截取视频
    def extract_video(self, input_folder, start_time, end_time, output_folder, encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2'):
        # 遍历文件夹中的所有mp4视频文件
        for file in os.listdir(input_folder):
            if file.endswith('.mp4'):
                input_file = os.path.join(input_folder, file)
                # 检测输出文件夹是否存在，不存在则创建
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_file = os.path.join(output_folder, file)
                # 调用ffmpeg命令行工具，对视频进行截取
                cmd = ['-i', f'"{input_file}"', '-ss', start_time, '-t', end_time, encoder, f'"{output_file}"']
                # 打印最终输入命令行的cmd指令，从列表转换为字符串
                # print("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
                self.run(cmd)
                print(file + '视频截取完成')
            else:
                print(file + '不是mp4文件，跳过')

    # 合并视频
    def merge_video(self, input_folder, input_file1, input_file2, output_folder, encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2'):
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
                    '-i', f'"{input_file1}"', 
                    '-i', f'"{input_file}"', 
                    '-i', f'"{input_file2}"', 
                    '-filter_complex', 
                    '"[0:v]fps=30,scale=1280:720,setsar=1[v0];[1:v]fps=30,scale=1280:720,setsar=1[v1];[2:v]fps=30,scale=1280:720,setsar=1[v2];[0:a]aformat=sample_rates=44100:channel_layouts=stereo[a0];[1:a]aformat=sample_rates=44100:channel_layouts=stereo[a1];[2:a]aformat=sample_rates=44100:channel_layouts=stereo[a2];[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[vout][aout]" -map "[vout]" -map "[aout]"', encoder, f'"{output_file}"']
                # 打印最终输入命令行的cmd指令，从列表转换为字符串
                # print("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
                self.run(cmd)
                print(file + '视频合并完成')
            else:
                print(file + '不是mp4文件，跳过')


ffmpeg = FFmpeg(r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe')  # 确保路径正确且适用于您的系统

"""
下面是测试示例代码
"""

# 调用version函数，打印ffmpeg的版本信息
# print(ffmpeg.version())

# 调用extract_video函数，对视频进行截取
input_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\input'
output_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output1'
start_time = '00:00:01.000'
end = '00:00:03.500'
ffmpeg.extract_video(input_folder, start_time, end, output_folder)
print('视频截取完成')

# 调用merge_video函数，对视频进行合并
# input_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output1'
# output_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output2'
# input_file1 = r'Q:\Git\FFmpeg-python\02FFmpegTest\input\1\op.mp4'
# input_file2 = r'Q:\Git\FFmpeg-python\02FFmpegTest\input\1\ed.mp4'
# ffmpeg.merge_video(input_folder, input_file1, input_file2, output_folder)
# print('视频合并完成')

