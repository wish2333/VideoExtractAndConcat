import os
from PySide6.QtCore import QThread, Qt, Signal, QObject
from PySide6.QtWidgets import QWidget, QFileDialog, QListWidgetItem
from qfluentwidgets import MessageBox

from modules.config import autopath, ffpath
from modules.autoEditorApi import AutoEditor
from modules.Ui_VautocutInterface import Ui_VautocutInterface

from modules.logger_config import logger

# Inherited from QObject, the subclasses designed for executing background tasks.
class Worker(QObject):
    started = Signal()
    finished = Signal()
    interrupted = Signal()
    callback = Signal()

    def __init__(self, auto_editor_path, cmd, callback=None):
        super().__init__()
        self.auto_editor_path = auto_editor_path
        self.cmd = cmd
        self._started_flag = False  # 
        self._interrupted_flag = False  # The flag of the worker starting.
        self.callback = callback  # The callback function.
        self.is_interrupted = False  # Callback flag when a task is interrupted.

    def interrupted_callback(self):
        logger.info("The interrupt signal is received. Worker interrupted.")
        self.is_interrupted = True  # Set the flag of the worker interrupted.
        if callable(self.callback):
            self.callback()  # Call the callback function.
        self.interrupted.emit()  # Emit the signal of the worker interrupted.

    def run_video(self):
        self._started_flag = True  # Set the flag of the worker starting.
        self.started.emit()  # Emit the signal of the worker starting.
        self.auto_editor_instance = AutoEditor(self.auto_editor_path, interrupt_flag=self._interrupted_flag, callback=self.interrupted_callback)  # Create an instance of the AutoEditor class.
        self.auto_editor_instance.run(self.cmd)  # Run the editor with the given command.
        self.finished.emit()  # Emit the signal of the worker finished.

    def interrupt(self):
        self._interrupted_flag = True  # Set the flag of the worker starting.
        self.auto_editor_instance.update_interrupt_flag(self._interrupted_flag)  # Update the interrupt flag of the AutoEditor instance.
        logger.info("The interrupt signal is sent. Worker is interrupted.")

class WorkerThread(QThread):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker
        self.worker.interrupted.connect(self.handle_interrupted)  # When the worker is interrupted, call the handle_interrupted function.
    def run(self):
        try:
            self.worker.run_video()
        except Exception as e:
            logger.error(f"An error occurred while running the worker: {e}")

    def handle_interrupted(self):
        self.quit()  # Quit the thread.

class VautocutInterface(QWidget, Ui_VautocutInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_variables()
        self.init_action()
        self.init_print()
        self.bind()
        
    def init_variables(self):
        # file
        self.input_file_args = []

        # circle
        self.i = 0
        self.is_paused = False

        # filter[margin, edit, cut, speed, anormalize , vcodec, acodec, export]
        self.filter = ['', '', '', '', '', '', '','']
        
    def init_action(self):
        # addItems
        vcodec_list = ['default', 'libx264', 'libx265', 'h264_nvenc', 'h264_qsv', 'h264_amf', 'hevc_nvenc', 'hevc_qsv', 'hevc_amf']
        self.VautocutlineEditVE.addItems(vcodec_list)
        vsize_list = ['-b:v 10M', '-b:v 500k', '-q:v 0']
        self.VautocutlineEdit.addItems(vsize_list)
        acodec_list = ['default', 'aac', 'alac', 'libfdk_aac', 'ac3', 'flac', 'libmp3lame', 'libopus', 'libvorbis', 'libwavpack']
        self.VautocutlineEditAE.addItems(acodec_list)

        # radioButton
        self.VautocutradioButton_11.setChecked(True)
        self.VautocutradioButton_10.setChecked(True)

    def init_print(self):
        logger.debug("VautocutInterface initialized.")  # Log the initialization of the VautocutInterface.

    def bind(self):

        # file operation
        self.Vautocutinputfile.clicked.connect(self.open_file)
        self.Vautocutinputclear.clicked.connect(self.clear_input_file)

        # change filter
        self.VautocutlineEditVE.currentTextChanged.connect(self.change_vcodec)
        self.VautocutlineEdit.currentTextChanged.connect(self.change_vcodec)
        self.VautocutlineEditAE.currentTextChanged.connect(self.change_acodec)
        self.VautocutcomboBox_3.currentTextChanged.connect(self.change_acodec)
        self.VautocutcheckBox.checkStateChanged.connect(self.change_anormalize)
        self.VautocutdoubleSpinBox.valueChanged.connect(self.change_margin)
        self.VautocutdoubleSpinBox_4.valueChanged.connect(self.change_margin)
        self.VautocutdoubleSpinBox_2.valueChanged.connect(self.change_cut)
        self.VautocutdoubleSpinBox_3.valueChanged.connect(self.change_cut)
        self.VautocutdoubleSpinBox_5.valueChanged.connect(self.change_speed)
        self.VautocutradioButton_6.toggled.connect(self.change_edit)
        self.VautocutradioButton_7.toggled.connect(self.change_edit)
        self.VautocutradioButton_8.toggled.connect(self.change_edit)
        self.VautocutradioButton_9.toggled.connect(self.change_edit)
        self.VautocutradioButton_10.toggled.connect(self.change_edit)
        self.VautocutlineEdit_2.textChanged.connect(self.change_edit)
        self.VautocutlineEdit_3.textChanged.connect(self.change_edit)
        self.VautocutlineEdit_4.textChanged.connect(self.change_edit)
        self.VautocutradioButton.toggled.connect(self.change_export)
        self.VautocutradioButton_2.toggled.connect(self.change_export)
        self.VautocutradioButton_3.toggled.connect(self.change_export)
        self.VautocutradioButton_4.toggled.connect(self.change_export)
        self.VautocutradioButton_5.toggled.connect(self.change_export)
        self.VautocutcheckBox_2.checkStateChanged.connect(self.change_export)

        # start
        self.VautocutpushBtn.clicked.connect(self.run_auto_editor)
        self.VautocutSTBtn.clicked.connect(self.interrupt_auto_editor)
        self.VautocutpushBtn_2.clicked.connect(self.unfreeze_config)


    def open_file(self):
        self.append_input_file_args, _ = QFileDialog.getOpenFileNames(self, "选择输入文件", "", "All Files (*)")
        for file in self.append_input_file_args:
            if file not in self.input_file_args:
                self.input_file_args.append(file)
                item = QListWidgetItem(file)
                self.Vautocutinputlist.addItem(item)
    def clear_input_file(self):
        self.input_file_args = []
        self.Vautocutinputlist.clear()

    def change_filter(self):
        filter_str = ''.join(self.filter)
        self.VcodecpIFplainTextEdit.setPlainText(filter_str)

    def change_margin(self):
        a = self.VautocutdoubleSpinBox.text()
        b = self.VautocutdoubleSpinBox_4.text()
        if a != '0.00' and b != '0.00':
            self.filter[0] = f'--margin {a}s,{b}sec'
        elif a != '0.00' and b == '0.00':
            self.filter[0] = f'--margin {a}sec'
        elif a == '0.00' and b != '0.00':
            self.filter[0] = f'--margin {b}sec'
        else:
            self.filter[0] = ''
        self.change_filter()

    def change_edit(self):
        if self.VautocutradioButton_6.isChecked():
            self.filter[1] = f' --edit "{self.VautocutlineEdit_2.text()}"'
        elif self.VautocutradioButton_7.isChecked():
            self.filter[1] = f' --edit "{self.VautocutlineEdit_3.text()}"'
        elif self.VautocutradioButton_8.isChecked():
            self.filter[1] = f' --edit "{self.VautocutlineEdit_4.text()}"'
        elif self.VautocutradioButton_9.isChecked():
            self.filter[1] = ' --edit none'
        else:
            self.filter[1] = ''
        self.change_filter()
        

    def change_cut(self):
        a = self.VautocutdoubleSpinBox_2.text()
        b = self.VautocutdoubleSpinBox_3.text()
        if a != '0.00' and b != '0.00':
            self.filter[2] = f' --cut-out 0,{a}sec -{b}sec,end'
        elif a != '0.00' and b == '0.00':
            self.filter[2] = f' --cut-out 0,{a}sec'
        elif a == '0.00' and b != '0.00':
            self.filter[2] = f' --cut-out -{b}sec,end'
        else:
            self.filter[2] = ''
        self.change_filter()

    def change_speed(self):
        speed = self.VautocutdoubleSpinBox_5.text()
        if speed != '1.00':
            self.filter[3] = f' -v {speed}'
        else:
            self.filter[3] = ''
        self.change_filter()

    def change_anormalize(self):
        if self.filter[7] in ['', ' --export audio', ' --export clip-sequence'] and self.VautocutcheckBox.isChecked():
            self.filter[4]  = ' --audio-normalize ebu:i=-5,lra=5,gain=5,tp=-0.3'
        else:
            self.filter[4] = ''
        self.change_filter()



    def change_vcodec(self):
        vcodec = self.VautocutlineEditVE.currentText()
        vsize = self.VautocutlineEdit.currentText()
        if self.filter[7] in ['', ' --export clip-sequence'] and vcodec != 'default':
            self.filter[5] = f' -c:v {vcodec} {vsize}'
        else:
            self.filter[5] = ''
        self.change_filter()

    def change_acodec(self):
        acodec = self.VautocutlineEditAE.currentText()
        asize = self.VautocutcomboBox_3.currentText()
        if self.filter[7] in ['', ' --export clip-sequence'] and acodec != 'default':
            self.filter[6] = f' -c:a {acodec} -b:a {asize}'
        else:
            self.filter[6] = ''
        self.change_filter()

    def change_export(self):
        if not self.VautocutcheckBox_2.isChecked():
            if self.VautocutradioButton_5.isChecked():
                self.filter[7] = ' --export audio'
            elif self.VautocutradioButton.isChecked():
                self.filter[7] = ' --export premiere'
            elif self.VautocutradioButton_2.isChecked():
                self.filter[7] = ' --export resolve'
            elif self.VautocutradioButton_3.isChecked():
                self.filter[7] = ' --export shotcut'
            elif self.VautocutradioButton_4.isChecked():
                self.filter[7] = ' --export clip-sequence'
            else:
                self.filter[7] = ''
        else:
            if self.VautocutradioButton_5.isChecked():
                self.filter[7] = ' --export audio'
            elif self.VautocutradioButton.isChecked():
                self.filter[7] = ' --silent-speed 1 --video-speed 1 --export premiere'
            elif self.VautocutradioButton_2.isChecked():
                self.filter[7] = ' --silent-speed 1 --video-speed 1 --export resolve'
            elif self.VautocutradioButton_3.isChecked():
                self.filter[7] = ' --silent-speed 1 --video-speed 1 --export shotcut'
            elif self.VautocutradioButton_4.isChecked():
                self.filter[7] = ' --export clip-sequence'
            else:
                self.filter[7] = ''
        self.change_vcodec()
        self.change_acodec()
        self.change_anormalize()
        self.change_filter()

    def run_auto_editor(self):
        if self.input_file_args != []:
            while self.i < len(self.input_file_args):
                if self.is_paused:
                    break
                input_file = self.input_file_args[self.i]
                if os.path.isfile(input_file):
                    command = []
                    command.append(f'"{input_file}"')
                    command.append(self.VcodecpIFplainTextEdit.toPlainText())
                    command.append(f'--ffmpeg-location "{ffpath.ffmpeg_path}" --no-open')
                    try:
                        self.freeze_config()
                        self.worker = Worker(autopath.auto_path, command)
                        self.thread = WorkerThread(self.worker)
                        self.thread.started.connect(self.on_thread_started())
                        self.thread.finished.connect(self.worker.deleteLater)  
                        self.thread.finished.connect(self.thread.deleteLater)  
                        self.thread.finished.connect(self.filter_thread_finished)  
                        self.thread.start()
                    except Exception as e:
                        logger.error(f"An error occurred while running the worker: {e}")
                else:
                    m = MessageBox("错误", "输入文件不存在！", parent=self)
                    if not m.exec():
                        self.unfreeze_config()
                        self.i = 2666666666
                        self.filter_thread_finished()
                        break

    def on_thread_started(self):
        self.is_paused = True  # 开启暂停标志
        logger.info(f'线程创建，暂停循环，i={self.i}')

    def filter_thread_finished(self):
        self.is_paused = False  # 重置暂停标志
        self.i = self.i + 1  # 开启下一个文件
        if self.i < len(self.input_file_args):  # 还有文件未处理
            logger.info(f'{self.i-1}线程结束，开始循环，i={self.i}')
            self.run_auto_editor()  # 开启下一个线程
        else:
            self.i = 0  # 循环计数器清零
            self.unfreeze_config()
            MessageBox("提示", "转码任务已完成！", parent=self).exec()

    def freeze_config(self):
        self.Vautocutinputfile.setEnabled(False)
        self.Vautocutinputclear.setEnabled(False)
        self.VautocutlineEditVE.setEnabled(False)
        self.VautocutlineEdit.setEnabled(False)
        self.VautocutlineEditAE.setEnabled(False)
        self.VautocutcomboBox_3.setEnabled(False)
        self.VautocutcheckBox.setEnabled(False)
        self.VautocutdoubleSpinBox.setEnabled(False)
        self.VautocutdoubleSpinBox_4.setEnabled(False)
        self.VautocutdoubleSpinBox_2.setEnabled(False)
        self.VautocutdoubleSpinBox_3.setEnabled(False)
        self.VautocutdoubleSpinBox_5.setEnabled(False)
        self.VautocutradioButton.setEnabled(False)
        self.VautocutradioButton_2.setEnabled(False)
        self.VautocutradioButton_3.setEnabled(False)
        self.VautocutradioButton_4.setEnabled(False)
        self.VautocutradioButton_5.setEnabled(False)
        self.VautocutradioButton_6.setEnabled(False)
        self.VautocutradioButton_7.setEnabled(False)
        self.VautocutradioButton_8.setEnabled(False)
        self.VautocutradioButton_9.setEnabled(False)
        self.VautocutradioButton_10.setEnabled(False)
        self.VautocutradioButton_11.setEnabled(False)
        self.VautocutlineEdit_2.setEnabled(False)
        self.VautocutlineEdit_3.setEnabled(False)
        self.VautocutlineEdit_4.setEnabled(False)
        self.VautocutcheckBox_2.setEnabled(False)
        self.VautocutpushBtn.setEnabled(False)
        self.VautocutSTBtn.setEnabled(False)
        self.VcodecpIFplainTextEdit.setEnabled(False)

    def unfreeze_config(self):
        self.Vautocutinputfile.setEnabled(True)
        self.Vautocutinputclear.setEnabled(True)
        self.VautocutlineEditVE.setEnabled(True)
        self.VautocutlineEdit.setEnabled(True)
        self.VautocutlineEditAE.setEnabled(True)
        self.VautocutcomboBox_3.setEnabled(True)
        self.VautocutcheckBox.setEnabled(True)
        self.VautocutdoubleSpinBox.setEnabled(True)
        self.VautocutdoubleSpinBox_4.setEnabled(True)
        self.VautocutdoubleSpinBox_2.setEnabled(True)
        self.VautocutdoubleSpinBox_3.setEnabled(True)
        self.VautocutdoubleSpinBox_5.setEnabled(True)
        self.VautocutradioButton.setEnabled(True)
        self.VautocutradioButton_2.setEnabled(True)
        self.VautocutradioButton_3.setEnabled(True)
        self.VautocutradioButton_4.setEnabled(True)
        self.VautocutradioButton_5.setEnabled(True)
        self.VautocutradioButton_6.setEnabled(True)
        self.VautocutradioButton_7.setEnabled(True)
        self.VautocutradioButton_8.setEnabled(True)
        self.VautocutradioButton_9.setEnabled(True)
        self.VautocutradioButton_10.setEnabled(True)
        self.VautocutradioButton_11.setEnabled(True)
        self.VautocutlineEdit_2.setEnabled(True)
        self.VautocutlineEdit_3.setEnabled(True)
        self.VautocutlineEdit_4.setEnabled(True)
        self.VautocutcheckBox_2.setEnabled(True)
        self.VautocutpushBtn.setEnabled(True)
        self.VautocutSTBtn.setEnabled(True)
        self.VcodecpIFplainTextEdit.setEnabled(True)

    def interrupt_auto_editor(self):
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
                MessageBox("警告", "转码任务已暂停！", parent=self).exec()