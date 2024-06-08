# autoEditorApi.py
# 实现了FFmpeg的命令行接口，可以对视频进行各种操作，如截取、合并、转码、截图等。

import subprocess
import os
from modules.logger_config import logger
import time
import threading
from modules.config import autopath
import configparser


class AutoEditor:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(
            self,
            auto_editor_path=autopath.auto_path,
            interrupt_flag=False,  # 中断标志
            callback=None,  # 回调函数
    ):
        self.auto_editor_path = auto_editor_path
        self.interrupt_flag = interrupt_flag
        self.callback = callback

    def update_interrupt_flag(self, flag=True):
        self.interrupt_flag = flag

    def check_interrupt_flag(self):
        while not self.interrupt_flag:
            # logger.info("auto-editor-Api守卫线程运行中")
            time.sleep(1)
        logger.debug("auto-editor-Api检测到中断请求")
        self.interrupt_run()

    def interrupt_run(self):
        if self.interrupt_flag:
            # 如果收到中断信号，则终止FFmpeg进程
            logger.debug("尝试终止AutoEditor进程")
            self.p.terminate()
            self.p.wait(timeout=5)
            if self.p.poll() is None:
                self.p.kill()
            if callable(self.callback):
                self.callback()
            self.interrupt_flag = False
            logger.debug("AutoEditor进程强制终止")
        logger.debug("auto-editor-Api中断请求已处理")

    # 定义run方法来执行FFmpeg命令
    def run(self, cmd):
        t = None  # 守卫线程预留在try之外
        try:
            cmd = [self.auto_editor_path] + cmd
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
                f"找不到auto-editor命令，请检查auto_editor_path是否正确配置。")
            raise fnf_error
        except PermissionError as p_error:
            logger.error(
                f"auto-editor命令没有执行权限，请检查auto_editor_path是否正确配置。")
            raise p_error
        except Exception as e:
            logger.error(f"执行AutoEditor命令失败：{e}")
            raise e
        finally:
            logger.info("AutoEditor命令执行完成")
            if t and t.is_alive():
                self.interrupt_flag = True  # 设置中断标志
                t.join()
                self.interrupt_flag = False  # 重置中断标志
                logger.debug("守卫线程退出")