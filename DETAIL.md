# FFmpeg+Python：GUI实现批量头尾处理

**项目概述**

本项目旨在开发一个用户友好的图形界面应用程序，用于视频片头和片尾的快速切割与合并功能。通过集成Qt Designer设计的界面与Python编程语言，结合强大的ffmpeg工具，用户能够轻松指定视频文件、设置切割时间点，完成视频处理任务。项目最终目标是提高视频编辑效率，尤其适合需要批量处理视频的用户。

## 简要流程大纲：

**环境搭建**

安装必要的软件和库：确保Python环境配置妥当，安装PySide6、ffmpeg。

**界面设计（使用Qt Designer）**

主界面设计：设计包含文件选择按钮（用于选择视频文件）、时间输入框（分别输入片头去除时间、片尾去除时间或直接输入裁剪时间段）、输出路径选择按钮、预览窗口（可选）、开始处理按钮和进度条。并转换.ui文件为.py文件。

**编写核心逻辑代码**

读取视频信息：使用ffmpeg获取视频时长等基本信息

时间处理：基于用户输入，计算实际裁剪命令（主要是结尾时间）参数。

调用ffmpeg：构造并执行ffmpeg命令行指令，进行视频切割和合并操作。

进度反馈：实现进度条更新逻辑，展示视频处理进度（这一步可能需要解析ffmpeg输出的信息）

错误处理：捕获并处理ffmpeg执行过程中可能出现的错误，向用户提供友好提示

**界面与逻辑代码绑定**

利用PySide的信号与槽机制，将界面元素（如按钮点击事件）与后端处理逻辑连接起来。

**测试与调试**

对软件进行详尽的功能测试，确保视频切割与合并功能准确无误，界面响应迅速，错误处理机制有效。

**优化与美化**

根据测试反馈调整界面布局，提升用户体验；考虑加入多线程处理以提高程序响应速度，特别是在处理大文件时。

**打包与部署**

将应用打包成可执行文件（如使用PyInstaller），方便分发和部署，确保在没有开发环境的系统上也能正常运行。

## 界面设计

使用Qt Designer进行界面设计。这个过程包括创建基本界面元素、布局调整、以及如何为这些元素设置属性。

**添加必要组件**、**设定布局**（略）

**设置组件属性**（略）

**转换.ui文件为.py文件**

1. 命令行转换：

   ```
   pyside6-uic input.ui -o output.py
   ```

2. VS Code绑定uic转换

## 在main.py中引入ui

```python
from PyQt5.QtWidgets import QApplication
from output import Ui_MainWindow  # 假设转换后生成的文件名为output.py

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
       super().__init__()
        self.setupUi(self)  # 初始化界面
        # 进一步设置信号槽和其他逻辑...

if "__name__" == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
```

## 编写核心逻辑代码

### 设定FFmpeg路径（config.py）

```python
import os

class ffpath:
    # 相对路径
    ffmpeg_path_relative = '.\\FFmpeg\\bin\\ffmpeg.exe'
    ffprobe_path_relative = '.\\FFmpeg\\bin\\ffprobe.exe'

    # 转换为绝对路径
    ffmpeg_path = os.path.abspath(ffmpeg_path_relative)
    ffprobe_path = os.path.abspath(ffprobe_path_relative)
```

### 初始化FFmpeg（ffmpegApi.py）

```python
import subprocess
import os
#import time
# 从config.py中拿到ffmpeg.exe和ffprobe.exe的绝对路径
from config import ffpath

class FFmpeg:

    # 初始化函数，用于初始化实例的ffmpeg_path属性
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path
```

### 定义run方法来调用cmd（ffmpegApi.py）

虽然subprocess.Popen可以输入列表，但实考虑到FFmpeg命令中可能有空格、路径等元素，在运行中可能报错，故先转换为字符串形式输入。

```python
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
        print(f"尝试执行：{cmd_str}")
        p = subprocess.Popen(cmd_str, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode != 0:
            print(f"命令执行失败，错误信息：{err.decode('utf-8')}")
            raise Exception(err.decode('utf-8'))
```

### 截取视频（ffmpegApi.py）

定义extract_video函数

```python
def extract_video(self, input_folder, start_time, end, output_folder, encoder='-c:v copy -c:a copy'):
    """
    获得FFmpeg命令的逻辑，给出具体的FFmpeg命令并传入run函数中运行
    
    参数：
    folder：输入输出文件夹参数须为绝对路径字符串
    start_time, end：片头片尾的持续时间参数须为H:mm:ss:fff格式的字符串
    encoder参数须为字符串，默认为'-c:v copy -c:a copy'复制流
    """
```

在extract_video函数下定义time_calculate以处理片尾时间（FFmpeg仅提供了从头到尾的检索方式，即需要根据片尾持续时间计算片尾的时间戳）：①该函数仅进行计算，获取视频duration不在此函数中；②先将end字符串转换为浮点数，并于float(duration)进行计算，再转换对应格式字符串

```python
        def time_calculate(duration, end):
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
```

在extract_video函数下主要代码：FFmpeg命令中，核心在于传入-accurate_seek参数，虽然不能精准定位，从而导致切不到真正想要的时间点和片段，但是胜在不出错，对于批量处理这种粗糙工作来说是更好的选择，如需对单个视频的智能精准切割，可以考虑losslesscut，期待它出批处理功能。

```python
        # 遍历文件夹中的所有mp4视频文件
        for file in os.listdir(input_folder):
            if file.endswith('.mp4'):
                input_file = os.path.join(input_folder, file)
                # 检测输出文件夹是否存在，不存在则创建
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                output_file = os.path.join(output_folder, file)
                # 读取视频的总时长（调用config.py中ffpath类的ffprobe_path），传入run函数中运行
                cmd1 = [ffpath.ffprobe_path, '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file]
                print("执行：" + ' '.join(cmd1))
                result = subprocess.run(cmd1, capture_output=True, text=True)
                duration = float(result.stdout.strip())
                print("视频总秒数为：", duration)
                # 调用time_calculate函数将end时间转换为秒数浮点数计算后返回结束时间字符串
                end_time = time_calculate(duration, end)
                # 调用ffmpeg命令行工具，对视频进行截取
                cmd = ['-ss', start_time, '-to', end_time, '-accurate_seek', '-i', f'"{input_file}"',  encoder, f'"{output_file}"']
                # 打印最终输入命令行的cmd指令，从列表转换为字符串
                # print("执行：" + r'Q:\Git\FFmpeg-python\02FFmpegTest\FFmpeg\bin\ffmpeg.exe ' + ' '.join(cmd))
                self.run(cmd)
                print(file + '视频截取完成')
            else:
                print(file + '不是mp4文件，跳过')
```

### 合并视频（ffmpegApi.py）

定义merge_video函数：FFmpeg命令中，核心在于-filter_complex复杂滤镜参数，在重新编码前统一视频格式。虽然需要消耗时间，但是最为保险，目的同样是防止在批处理中出错。根据本人实践经验，需要处理统一以下五个要素后在项目中即可应对所有视频：视频帧率、分辨率、像素宽高比。

```python
def merge_video(self, input_folder, input_file1, input_file2, output_folder, encoder='-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2'):
     """
    获得FFmpeg命令的逻辑，给出具体的FFmpeg命令并传入run函数中运行
    
    参数：
    folder：输入输出文件夹参数须为绝对路径字符串
    input_file：片头片尾参数须为绝对路径字符串
    encoder参数须为字符串，默认为'-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -ar 44100 -ac 2'重新编码
    """
    
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
```

### 调试用代码（ffmpegApi.py）

```python
# 调用extract_video函数，对视频进行截取
input_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\input'
output_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output1'
start_time = '00:00:01.000'
end = '00:00:03.500'
ffmpeg.extract_video(input_folder, start_time, end, output_folder)
print('视频截取完成')

# 调用merge_video函数，对视频进行合并
input_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output1'
output_folder = r'Q:\Git\FFmpeg-python\02FFmpegTest\output2'
input_file1 = r'Q:\Git\FFmpeg-python\02FFmpegTest\input\1\op.mp4'
input_file2 = r'Q:\Git\FFmpeg-python\02FFmpegTest\input\1\ed.mp4'
ffmpeg.merge_video(input_folder, input_file1, input_file2, output_folder)
print('视频合并完成')
```

## Pyside界面与逻辑代码绑定（main.py）

### 导入第三方库和自定义py库

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Ui_VideoEditor import Ui_MainWindow
from ffmpegApi import FFmpeg
from config import ffpath

# 导入ffmpeg路径
init1 = print("初始化ffmpeg路径为：", ffpath.ffmpeg_path)
init2 = print("初始化ffprobe路径为：", ffpath.ffprobe_path)
```

### 主窗口类

```python
class MainWindow(QMainWindow, Ui_MainWindow):
    # 初始化窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        # 打开控制台窗口
        # TODO：未完成
```

### 主窗口类下，绑定事件槽

```python
    # 绑定事件槽
    def bind(self):
        # 设置按钮的信号槽
        self.importBn1.clicked.connect(self.import_video_folder1)
        self.importBn2.clicked.connect(self.import_video_file1)
        self.importBn3.clicked.connect(self.import_video_file2)
        self.importBn4.clicked.connect(self.import_video_folder2)
        self.exportBn1.clicked.connect(self.export_video_folder1)
        self.exportBn2.clicked.connect(self.export_video_folder2)
        self.pushButton1.clicked.connect(self.process_extract)
        self.pushButton2.clicked.connect(self.process_concat)
        self.pushButtonF.clicked.connect(self.adjust_ffmpeg_path)
```

### 主窗口类下，调整ffmpeg路径

```python
def adjust_ffmpeg_path(self):
        ffmpeg_folder = QFileDialog.getExistingDirectory(
            self, "选择bin文件夹", "./")
        ffpath.ffmpeg_path = f"{ffmpeg_folder}\\ffmpeg.exe"
        ffpath.ffprobe_path = f"{ffmpeg_folder}\\ffprobe.exe"
        if ffpath.ffmpeg_path:
            self.textEdit.append(f"ffmpeg路径修改为：{ffpath.ffmpeg_path}；{ffpath.ffprobe_path}")
            print(ffpath.ffmpeg_path)
```

### 主窗口类下，切割流程

```python
    # 切割流程
    # 点击导入视频文件夹按钮，弹出文件选择对话框，选择视频文件夹，选择完成后显示在文本框中
    def import_video_folder1(self):
        self.folder_path1 = QFileDialog.getExistingDirectory(
            self, "选择视频文件夹", "./")
        if self.folder_path1:
            self.textEdit.append(f"切割：输入文件夹为{self.folder_path1}")
    # 点击导出切割文件夹按钮，弹出文件选择对话框，选择文件夹，选择完成后显示在文本框中
    def export_video_folder1(self):
        self.folder1_path = QFileDialog.getExistingDirectory(
            self, "选择导出文件夹", "./")
        if self.folder1_path:
            self.textEdit.append(f"切割：输出文件夹为{self.folder1_path}")
    # 点击切割按钮，调用FFmpegApi的extract_video函数，切割视频
    def process_extract(self):
        # 检测程序是否输入了视频文件夹
        if not hasattr(self, 'folder_path1'):
            self.textEdit.append("切割：请先输入视频文件夹")
            return
        if not hasattr(self, 'folder1_path'):
            self.textEdit.append("切割：请先输入视频文件夹")
            return
        # 开始切割视频
        # 读取片头时间和片尾时间，以及编码格式
        start_time = self.time1.text()
        end_time = self.time2.text()
        encoder = self.line.text()
        if self.folder_path1 and self.folder1_path:
            # 实例化FFmpegApi
            ffmpeg_instance = FFmpeg(ffpath.ffmpeg_path)
            # 调用extract_video函数
            ffmpeg_instance.extract_video(self.folder_path1, start_time, end_time,self.folder1_path, encoder)
            self.textEdit.append("视频切割完成")
        else:
            self.textEdit.append("切割：请先输入视频文件夹")
```

### 主窗口类下，合并流程

```python
    # 合并流程
    # 点击导入视频文件夹按钮，弹出文件选择对话框，选择视频文件夹，选择完成后显示在文本框中
    def import_video_folder2(self):
        self.folder_path2 = QFileDialog.getExistingDirectory(
            self, "选择视频文件夹", "./")
        if self.folder_path2:
            self.textEdit.append(f"合并：输入文件夹为{self.folder_path2}")
    # 点击导入片头视频文件按钮，弹出文件选择对话框，选择视频文件，选择完成后添加到文本框中且不覆盖前面的文字内容
    def import_video_file1(self):
        self.file1_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "./", "视频文件 (*.mp4)")
        if self.file1_path:
            self.textEdit.append(f"合并：输入片头文件为{self.file1_path}")

    # 点击导入片尾视频文件按钮，弹出文件选择对话框，选择视频文件，选择完成后添加到文本框中且不覆盖前面的文字内容
    def import_video_file2(self):
        self.file2_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "./", "视频文件 (*.mp4)")
        if self.file2_path:
            self.textEdit.append(f"合并：输入片尾文件为{self.file2_path}")

    # 点击导出合并文件夹按钮，弹出文件选择对话框，选择文件夹，选择完成后显示在文本框中
    def export_video_folder2(self):
        self.folder2_path = QFileDialog.getExistingDirectory(
            self, "选择导出文件夹", "./")
        if self.folder2_path:
            self.textEdit.append(f"合并：输出文件夹为{self.folder2_path}")
    # 点击开始合并按钮，调用FFmpegApi的merge_video函数，合并视频
    def process_concat(self):
        # 检测程序是否输入了视频文件夹
        if not hasattr(self, 'folder_path2'):
            self.textEdit.append("合并：请先输入视频文件夹")
            return
        if not hasattr(self, 'file1_path'):
            self.textEdit.append("合并：请先输入片头视频文件")
            return
        if not hasattr(self, 'file2_path'):
            self.textEdit.append("合并：请先输入片尾视频文件")
            return
        if not hasattr(self, 'folder2_path'):
            self.textEdit.append("合并：请先输入导出文件夹")
            return
        # 开始合并视频
        # 读取片头时间和片尾时间，以及编码格式
        encoder = self.line2.text()
        if self.folder_path2 and self.file1_path and self.file2_path and self.folder2_path:
            # 实例化FFmpegApi
            ffmpeg_instance = FFmpeg(ffpath.ffmpeg_path)
            # 调用merge_video函数
            ffmpeg_instance.merge_video(self.folder_path2, self.file1_path, self.file2_path, self.folder2_path, encoder)
            self.textEdit.append("视频合并完成")
        else:
            self.textEdit.append("合并：请先输入视频文件夹")
```

### 运行窗口程序

```python
# 运行窗口程序
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()  # 创建窗口对象
    window.show()  # 显示窗口
    app.exec_()  # 运行程序
```

## 优化与美化、打包与部署

未完成，计划的项有：

- [ ] 优化性能
- [ ] 中止处理
- [ ] 允许调出控制台
- [ ] 使FFmpeg运行时的输出返回到控制台
- [ ] 使合并流程能够识别两段视频的合并（目前必须同时传入片头片尾）
- [ ] 窗口美化
- [ ] 打包依赖库
- [ ] 封装bat或exe
- [ ] 其他

## 使用指南（20240506）

1. 安装python环境和第三方库pyside6

```
pip install pyside6
```

2. 安装FFmpeg到main.py目录下，文件树结构如下

```
├── FFmpeg    	# 注意大写           
│   └── bin
│   └── ...
├── main.py     # 主程序
├── ...      
```

可以不按上述文件树组织文件，但需要在程序中手中点击设定ffmpeg/bin文件夹路径

3. 运行main.py

```
python main.py
```

