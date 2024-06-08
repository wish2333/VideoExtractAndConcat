import os
import configparser
from modules.logger_config import logger



def init_ffpath():
    configinit = configparser.ConfigParser()
    configinit.read('.\\modules\\config.ini', 'UTF-8')
    if configinit['PATHS']['ffmpeg_path'] == '':
        ffmpeg_path_relative = '.\\FFmpeg\\bin\\ffmpeg.exe'
        ffprobe_path_relative = '.\\FFmpeg\\bin\\ffprobe.exe'
        # ffplay_path_relative = '.\\FFmpeg\\bin\\ffplay.exe'
        # 转换为绝对路径
        init_ffmpeg_path = os.path.abspath(ffmpeg_path_relative)
        init_ffprobe_path = os.path.abspath(ffprobe_path_relative)
        # init_ffplay_path = os.path.abspath(ffplay_path_relative)
        # 写入配置文件
        configinit['PATHS']['ffmpeg_path'] = init_ffmpeg_path
        configinit['PATHS']['ffprobe_path'] = init_ffprobe_path
        # configinit['PATHS']['ffplay_path'] = init_ffplay_path
        with open('.\\modules\\config.ini', 'w', encoding='UTF-8') as configfile:
            configinit.write(configfile)
        logger.info('FFmpeg路径已初始化为：' + init_ffmpeg_path)
    else:
        logger.info('FFmpeg路径已读取为：' + configinit['PATHS']['ffmpeg_path'])
        
def init_autopath():
    configinit = configparser.ConfigParser()
    configinit.read('.\\modules\\config.ini', 'UTF-8')
    if configinit['PATHS']['auto_path'] == '':
        auto_path_relative = '.\\Scripts\\auto-editor.exe'
        # 转换为绝对路径
        init_auto_path = os.path.abspath(auto_path_relative)
        # 写入配置文件
        configinit['PATHS']['auto_path'] = init_auto_path
        with open('.\\modules\\config.ini', 'w', encoding='UTF-8') as configfile:
            configinit.write(configfile)
        logger.info('Auto-Editor路径已初始化为：' + init_auto_path)
    else:
        logger.info('Auto-Editor路径已读取为：' + configinit['PATHS']['auto_path'])

class ffpath:
    config = configparser.ConfigParser()
    config.read('.\\modules\\config.ini', 'UTF-8')
    ffmpeg_path = config.get('PATHS', 'ffmpeg_path')
    ffprobe_path = config.get('PATHS', 'ffprobe_path')
    # ffplay_path = config.get('PATHS', 'ffplay_path')

    def reset(self):
        config = configparser.ConfigParser()
        config.read('.\\modules\\config.ini', 'UTF-8')
        self.ffmpeg_path = config.get('PATHS', 'ffmpeg_path')
        self.ffprobe_path = config.get('PATHS', 'ffprobe_path')
        # self.ffplay_path = config.get('PATHS', 'ffplay_path')
        logger.info('FFmpeg路径已重置为：' + self.ffmpeg_path)
        
class autopath:
    config = configparser.ConfigParser()
    config.read('.\\modules\\config.ini', 'UTF-8')
    auto_path = config.get('PATHS', 'auto_path')
    def reset(self):
        config = configparser.ConfigParser()
        config.read('.\\modules\\config.ini', 'UTF-8')
        self.auto_path = config.get('PATHS', 'auto_path')

def set_config(ffmpeg_path, ffprobe_path):
    config = configparser.ConfigParser()
    config.read('.\\modules\\config.ini', 'UTF-8')
    config['PATHS']['ffmpeg_path'] = ffmpeg_path
    config['PATHS']['ffprobe_path'] = ffprobe_path
    # config['PATHS']['ffplay_path'] = ffplay_path
    with open('.\\modules\\config.ini', 'w', encoding='UTF-8') as configfile:
        config.write(configfile)
    logger.info('FFmpeg路径已设置为：' + ffmpeg_path)

def set_auto_path(auto_path):
    config = configparser.ConfigParser()
    config.read('.\\modules\\config.ini', 'UTF-8')
    config['PATHS']['auto_path'] = auto_path
    with open('.\\modules\\config.ini', 'w', encoding='UTF-8') as configfile:
        config.write(configfile)
    logger.info('Auto-Editor路径已设置为：' + auto_path)    

