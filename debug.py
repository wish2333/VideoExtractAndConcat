# Debugging code for the ffapi.py file.

from ffmpegApi import FFmpegHandler
from config import ffpath
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
print("logger initialized")

# initialize ffmpeg_path
try:
    # initialize ffmpeg_path
    init1 = ffpath.ffmpeg_path
    init2 = ffpath.ffprobe_path

    if not init1 or not init2:
        raise ValueError("初始化路径为空")

    logging.info(f"初始化ffmpeg路径为：{init1}")
    logging.info(f"初始化ffprobe路径为：{init2}")

    # Initialize FFmpegHandler and pass it the ffmpeg path
    ff = FFmpegHandler(init1, init2)

    # 调用version函数，打印ffmpeg的版本信息
    # logging.info("获取ffmpeg版本信息...")
    # version_info = ff.version()
    # logging.info(f"ffmpeg版本信息：{version_info}")

except Exception as e:
    logging.error(f"初始化FFmpegHandler时发生错误：{str(e)}")

finally:
    logging.info("初始化FFmpegHandler程序成功")

"""
下面是测试示例代码
"""

# 调用version函数，打印ffmpeg的版本信息
# logging.info(ff.version())


# 调用extract_video函数，对视频进行截取
input_folder = r'D:\Project\勤思\20240425\test'
output_folder = r'D:\Project\勤思\20240425\output2'
start_time = '00:00:01.000'
end = '02:02:03.500'
ff.extract_video(input_folder, start_time, end, output_folder)
logging.info('视频截取完成')

# 调用merge_video函数，对视频进行合并
# input_folder = r'D:\Project\勤思\20240425\test'
# output_folder = r'D:\Project\勤思\20240425\output2'
# input_file1 = r'D:\Project\勤思\20240425\test\1.mp4'
# input_file2 = r'D:\Project\勤思\20240425\test\1.mp4'
# ff.merge_video(input_folder, input_file1, input_file2, output_folder)
# logging.info('视频合并完成')
