
import os

from PySide6.QtCore import Qt, QThread, Signal, QObject, QTime
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QListWidgetItem
from qfluentwidgets import MessageBox

from modules.config import ffpath
from modules.ffmpegApi import FFmpeg
from modules.Ui_remuxInterface import Ui_remuxInterface

from modules.logger_config import logger

# 继承自QObject的子类，用于执行后台任务的子类
class Worker(QObject):
    started = Signal()  # 任务开始时发出的信号
    finished = Signal()  # 任务完成时发出的信号
    interrupted = Signal()  # 任务被中断时发出的信号
    callback = Signal()  # 任务执行过程中输出的信号

    def __init__(self, task_type, ffmpeg_path, ffprobe_path, *task_args, callback=None):
        super().__init__()
        self.task_type = task_type
        self.ffmpeg_path = ffmpeg_path
        self.ffprobe_path = ffprobe_path
        self.task_args = task_args
        logger.info(f"Simple {task_type} task started")
        self._started_flag = False  # 任务是否开始的标志
        self._interrupted_flag = False  # 任务是否被中断的标志
        self.callback = callback  # 任务执行过程中输出的回调函数
        self.is_interrupted = False  # 任务被中断时的回调函数
    def interrupt(self):
        self._interrupted_flag = True  # 设置任务被中断的标志
        self.ffmpeg_instance.update_interrupt_flag(self._interrupted_flag)  # 更新全局中断标志
        logger.info('中止信号已发出')
    def interrupted_callback(self):
        logger.info('中止信号回调，worker任务被中断')
        self.is_interrupted = True  # 设置任务被中断的标志
        if callable(self.callback):
            self.callback()
        self.interrupted.emit()  # 发出中断信号

    def run_ffmpeg_task(self):
        self._started_flag = True  # 任务开始的标志
        self.started.emit()  # 任务开始，发出信号
        if self.task_type == 'remux_video':
            self.remux_video(*self.task_args)
        elif self.task_type == 'norEx_video':
            self.norEx_video(*self.task_args)
        elif self.task_type == 'mulEx_video':
            self.mulEx_video(*self.task_args)
        else:
            logger.error(f"Unknown task type: {self.task_type}")
        
        self.finished.emit()  # 任务完成，发出信号
        

    # 在这里可以添加更多任务类型的判断和调用
    def remux_video(self, input, output, format, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.remux_video(input, output, format, overwrite)
    def norEx_video(self, input, output, action, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.norEx_video(input, output, action, overwrite)
    def mulEx_video(self, input, output, action, overwrite='-y'):
        self.ffmpeg_instance = FFmpeg(self.ffmpeg_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # 实例化FFmpegApi
        self.ffmpeg_instance.mulEx_video(input, output, action, overwrite)



# 继承自QThread的子类，用于后台执行任务的线程类
class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
        self.worker.interrupted.connect(self.handle_interrupt)  # 任务被中断时停止线程
    def run(self):
        try:
            self.worker.run_ffmpeg_task()
        except Exception as e:
            logger.error(f"Error occurred while running {self.worker.task_type} task: {e}")

    def handle_interrupt(self):
        self.quit()  # 停止线程

class RemuxInterface(QWidget, Ui_remuxInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_variables()
        # self.init_action()
        self.init_print()
        self.bind()
        # 必须给子界面设置全局唯一的对象名
    
    # Init_variables
    def init_variables(self):
        # file
        self.input_file_args = []
        self.output_file_args = []
        # 循环
        self.i = 0
        self.is_paused = False

    # Init_action
    # def init_action(self):
        
        


    # Init_print
    def init_print(self):
        logger.debug("remuxInterface is initialized")  # 直接使用导入的全局日志记录器
        

    # Bind Event
    def bind(self):

        # file operation
        self.remuxIFinputfile.clicked.connect(self.select_input_file)
        self.remuxIFoutputfolder.clicked.connect(self.select_output_folder)
        self.remuxIFinputclear.clicked.connect(self.clear_input_file)
        # self.remuxpushButton_2.clicked.connect(lambda: self.norEx('V'))
        # self.remuxpushButton_3.clicked.connect(lambda: self.norEx('A'))
        # self.remuxpushButton_5.clicked.connect(lambda: self.mulEx('V'))
        # self.remuxpushButton_6.clicked.connect(lambda: self.mulEx('A1'))
        # self.remuxpushButton_4.clicked.connect(lambda: self.mulEx('A2'))
        # self.remuxpushButton_7.clicked.connect(lambda: self.mulEx('A3'))
        # self.remuxpushButton_10.clicked.connect(lambda: self.mulEx('A4'))
        # self.remuxpushButton_8.clicked.connect(lambda: self.mulEx('S1'))
        # self.remuxpushButton_9.clicked.connect(lambda: self.mulEx('S2'))

        # remux operation
        self.remuxpushButton.clicked.connect(self.remux)



    
    #  File_operation
    def select_input_file(self):
        self.append_input_file_args, _ = QFileDialog.getOpenFileNames(self, "选择输入文件", "", "All Files (*)")
        for file_path in self.append_input_file_args:
            if file_path not in self.input_file_args:
                self.input_file_args.append(file_path)
                item = QListWidgetItem(file_path)
                self.remuxIFinputlist.addItem(item)

    def select_output_folder(self):
        if self.input_file_args != []:
            output_folder = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "")  # 选择输出文件夹
            if output_folder != '':  # 输出文件夹不为空且输出文件夹与输入文件夹不同
                self.output_file_args = [os.path.join(output_folder, os.path.basename(file_path)) for file_path in self.input_file_args]  # 获得输出文件，输出文件名与输入文件名相同
                self.remuxIFoutputfolder.setText(output_folder)
            else:
                self.remuxIFoutputfolder.setText('选择输出文件夹')
        else:
            MessageBox("警告", "请先选择输入文件！", parent=self).exec()

    def clear_input_file(self):
        self.input_file_args = []
        self.output_file_args = []
        self.remuxIFoutputfolder.setText('选择输出文件夹')
        self.remuxIFinputlist.clear()


    def remux(self):
        if self.input_file_args != [] and self.output_file_args != []:
            self.freeze_config('正在执行转码任务，请稍等...')  # 如果输入文件和输出文件都存在，则执行转码任务
            while self.i < (len(self.input_file_args)):
                if self.is_paused:  # 若暂停，则不进行循环
                    break
                input_file = self.input_file_args[self.i]
                output_file = self.output_file_args[self.i]  # 获得输出文件名(原文件名+后缀名)
                if os.path.isfile(input_file):
                    try:
                        self.freeze_config()
                        self.worker = Worker('remux_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, self.remuxcomboBox.currentText())  # 创建worker对象
                        self.thread = WorkerThread(self.worker)  # 创建线程对象
                        self.thread.started.connect(self.on_thread_started())  # 线程开始时发出信号
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.finished.connect(self.remux_thread_finished)  # 线程结束时开启下一个线程
                        self.thread.start()  # 开始线程
                    except Exception as e:
                        logger.error(f"Error occurred while creating worker object: {e}")
                else:
                    m = MessageBox("错误", f"{input_file}不存在！", parent=self)
                    if m.exec():
                        self.remux_thread_finished()  #  进行下一个文件
                    else:
                        self.clear_input_file()  # 清空输入文件列表
                        break


    def norEx(self, param):
        if self.input_file_args != [] and self.output_file_args != []:
            self.freeze_config('正在执行转码任务，请稍等...')  # 如果输入文件和输出文件都存在，则执行转码任务
            while self.i < (len(self.input_file_args)):
                if self.is_paused:  # 若暂停，则不进行循环
                    break
                input_file = self.input_file_args[self.i]
                output_file = self.output_file_args[self.i] + os.path.splitext(input_file)[-1]  # 获得输出文件名(原文件名+后缀名)
                if os.path.isfile(input_file):
                    try:
                        self.freeze_config()
                        self.worker = Worker('norEx_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, param)  # 创建worker对象
                        self.thread = WorkerThread(self.worker)  # 创建线程对象
                        self.thread.started.connect(self.on_thread_started())  # 线程开始时发出信号
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.finished.connect(self.remux_thread_finished)  # 线程结束时开启下一个线程
                        self.thread.start()  # 开始线程
                    except Exception as e:
                        logger.error(f"Error occurred while creating worker object: {e}")
                else:
                    m = MessageBox("错误", f"{input_file}不存在！", parent=self)
                    if not m.exec():
                        self.clear_input_file()  # 清空输入文件列表
                        self.i = 2666666666  # 设定一个很大的数值，使线程结束
                    self.norEx_thread_finished(param)  #  进行下一个文件
                    break

    def mulEx(self, param):
        if self.input_file_args != [] and self.output_file_args != []:
            while self.i < (len(self.input_file_args)):
                if self.is_paused:  # 若暂停，则不进行循环
                    break
                input_file = self.input_file_args[self.i]
                output_file = self.output_file_args[self.i] + os.path.splitext(input_file)[-1]  # 获得输出文件名(原文件名+后缀名)
                if os.path.isfile(input_file):
                    try:
                        self.freeze_config()
                        self.worker = Worker('mulEx_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, input_file, output_file, param)  # 创建worker对象
                        self.thread = WorkerThread(self.worker)  # 创建线程对象
                        self.thread.started.connect(self.on_thread_started())  # 线程开始时发出信号
                        self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
                        self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
                        self.thread.finished.connect(self.remux_thread_finished)  # 线程结束时开启下一个线程
                        self.thread.start()  # 开始线程
                    except Exception as e:
                        logger.error(f"Error occurred while creating worker object: {e}")
                else:
                    m = MessageBox("错误", f"{input_file}不存在！", parent=self)
                    if not m.exec():
                        self.clear_input_file()  # 清空输入文件列表
                        self.i = 2666666666  # 设定一个很大的数值，使线程结束
                        self.mulEx_thread_finished(param)  #  进行下一个文件
                        break

    def on_thread_started(self):
        self.is_paused = True  # 开启暂停标志
        logger.info(f'线程创建，暂停循环，i={self.i}')
    def remux_thread_finished(self):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        if self.i < len(self.input_file_args):  # 还有文件未处理
            logger.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
            self.remux()  # 开启下一个线程
        else:
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("提示", "转码任务已完成！", parent=self).exec()
    def norEx_thread_finished(self, param):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        if self.i < len(self.input_file_args):  # 还有文件未处理
            logger.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
            self.norEx(param)  # 开启下一个线程
        else:
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("提示", "转码任务已完成！", parent=self).exec()
    def mulEx_thread_finished(self, param):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        if self.i < len(self.input_file_args):  # 还有文件未处理
            logger.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
            self.mulEx(param)  # 开启下一个线程
        else:
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("提示", "转码任务已完成！", parent=self).exec()

    def freeze_config(self, text=''):
        self.remuxcomboBox.setEnabled(False)  # 禁止修改视频格式
        logger.info(f"Freeze config. {text}")
        # self.VcodecpIFconsole.appendPlainText("冻结配置")
    def unfreeze_config(self):
        self.remuxcomboBox.setEnabled(True)  # 解除视频格式冻结
        logger.info("Unfreeze config.")
        # self.VcodecpIFconsole.appendPlainText("解除冻结配置")

    def stop(self):
        if self.worker._started_flag:
            self.is_paused = True  # 开启暂停标志
            logger.info(f'暂停循环，i={self.i}')
            self.i = 2600000000  # 设定一个很大的数值，使线程结束
            self.worker.interrupt()  # 停止worker
            if self.worker.is_interrupted:  # 停止worker
                self.thread.wait()  # 等待线程结束
                self.worker.deleteLater()  # 删除worker对象
                self.thread.deleteLater()  # 删除线程对象
                self._started_flag = False
                self.is_paused = False  # 重置暂停标志
                self.i = 0  # 循环计数器清零
                self.unfreeze_config()
                MessageBox("警告", "转码任务已暂停！软件即将退出，请重新启动！", parent=self).exec()