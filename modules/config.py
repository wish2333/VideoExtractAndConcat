import os

class ffpath:
    # 相对路径
    ffmpeg_path_relative = '.\\FFmpeg\\bin\\ffmpeg.exe'
    ffprobe_path_relative = '.\\FFmpeg\\bin\\ffprobe.exe'

    # 转换为绝对路径
    ffmpeg_path = os.path.abspath(ffmpeg_path_relative)
    ffprobe_path = os.path.abspath(ffprobe_path_relative)

