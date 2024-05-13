# UpdateLog20240511

## version-pre2.0

UI重构，参考[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)和[MihiroToolbox](https://github.com/Eanya-Tonic/MihiroToolbox)构造UI和功能分布

![verison-pre2.0](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre2.0.jpg)

目前仅完成单文件（音视频）转码裁切的功能面板，且功能暂未完善（如字幕封装、音频替换封装等）

脱离了PyInstaller封装，暴露源代码。暂未优化大小，未来可以精简。

## PyQt-Fluent-Widgets 搭配 QtDesigner

## QtDesigner组件提升

## 实现FluentWindow

### main.py建立主界面

```python
import sys
# 第三方库
from PySide6.QtCore import Qt, QThread, Signal, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import setThemeColor, FluentWindow

from Ui_vencoInterface import Ui_Form

class mainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venco Interface")
        # self.setWindowIcon(QIcon("icon.png"))


if __name__ == '__main__':
    # enable dpi scale
	# 这一项好像有问题QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec()
```

### Interface.py

```python
from PySide6.QtCore import Qt, QThread, Signal, QObject
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtWidgets import QWidget

from Ui_vencoInterface import Ui_Form

class VencoInterface(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
```

### main.py添加子界面

```python
from from venco_Interface import VencoInterface

def __init__(self):
    # ....
    # 添加子界面
	self.vencoInterface = VencoInterface(self)
    self.addSubInterface(self.vencoInterface, FluentIcon.RINGER, "Venco Interface")
```

## 界面编排

## 转码界面

功能：（单文件）转码+切割

### 文件设置

#### 控制台console

- readonly

#### 输入文件夹、输出文件夹、字幕、音频

### 编码设置

#### 初始化自定义编码

```python
class TextEditClass():
    # custom_encoder
    def change_custom_encoder(self, 
        vcodec = '-vcodec libx264 ', 
        vpreset = '-preset medium -crf 23 ',
        resolution = '',
        fps = '',
        acodec = '-acodec aac ',
        apreset = '-b:a 128k ',
    ):

class VencoInterface(QWidget, Ui_Form):
    # ......
    # encoder
	custom_encoder = TextEditClass.change_custom_encoder(TextEditClass)
	self.plainTextEdit.setPlainText(custom_encoder) 
```

#### 绑定各项编码设置到自定义编码plainTextEdit中显示

### 开始执行

- 如果有输入、输出→检查输入是否合法
  - 合法→检查是否切割
    - 简单转码流程
    - 切割流程
  - 不合法
    - 弹窗警告
- 如果没有输入、输出→检查是否有音频
  - 有音频→音频转码流程
  - 无音频→无事发生
- 功能暂未完善（如字幕封装、音频替换封装等）

# UpdateLog20240510

返回到pre0.2进行，优化代码结构，重新使用同步执行FFmpeg命令，使用logging模块实现格式化日志并输出日志。通过QObject、QThread和Singal实现多线程，确保UI不假死，实际上多线程没有优化性能的作用，只是不希望程序假死，优雅！

![image-version-pre1.2from0.2](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre1.2from0.2.jpg)

## 调整内容

### ffmpegApi.py

实时返回ffmpeg执行命令（实际上并不实时而是需要等待某一步进行完成后才能返回，因而尚不能实现返回进度条→是不是去掉while True的判断就行了？笑哭）

```python
# 创建线程运行FFmpeg命令
p = subprocess.Popen(
    cmd_str, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT
)
# 实时输出FFmpeg命令的执行信息
while True:
    line = p.stdout.readline().decode('utf-8')
    if not line:
        # 如果没有更多输出，检查进程是否已经结束
        if p.poll() is not None:
            break
            else:
                continue
	logging.info(line.strip())  # 打印输出信息
```

### main.py

1. 多线程设置

   ```python
   # 引入并创建多线程函数
   from PySide6.QtCore import QThread, Signal, QObject
   # 继承自QObject的子类，用于执行后台任务的子类
   class Worker(QObject):
       finished = Signal()  # 任务完成时发出的信号
       def __init__(self, task_type, ffmpeg_path, ffprobe_path, *task_args):
           super().__init__()
           self.task_type = task_type
           self.ffmpeg_path = ffmpeg_path
           self.ffprobe_path = ffprobe_path
           self.task_args = task_args
       def run_ffmpeg_task(self):
           if self.task_type == 'extract_video':
               self.extract_video(*self.task_args)
           elif self.task_type =='merge_video':
               self.merge_video(*self.task_args)
           self.finished.emit()  # 任务完成，发出信号
   
       # 在这里可以添加更多任务类型的判断和调用
       def extract_video(self, input_folder, start_time, end_time, output_folder, encoder, overwrite):
           ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
           ffmpeg_instance.extract_video(input_folder, start_time, end_time, output_folder, encoder, overwrite)
       def merge_video(self, input_folder, file1, file2, output_folder, encoder, overwrite):
           ffmpeg_instance = FFmpeg(self.ffmpeg_path)  # 实例化FFmpegApi
           ffmpeg_instance.merge_video(input_folder, file1, file2, output_folder, encoder, overwrite)
           
   # 继承自QThread的子类，用于后台执行任务的线程类
   class WorkerThread(QThread):
       def __init__(self, worker):
           super().__init__()
           self.worker = worker
   
       def run(self):
           self.worker.run_ffmpeg_task()
   
   # 实际的调用范例，记得继承self以保持加载，而不会被清除
   # 创建Worker实例
   self.worker = Worker('extract_video', ffpath.ffmpeg_path, ffpath.ffprobe_path, self.folder_path1, start_time, end_time, self.folder1_path, encoder, '-y')
   # 实例化WorkerThread
   self.thread = WorkerThread(self.worker)
   self.thread.started.connect(lambda: self.textEdit.append("开始切割视频"))  # 线程开始时显示提示信息
   self.thread.finished.connect(lambda: self.textEdit.append("视频切割完成"))  # 线程结束时显示提示信息
   self.thread.finished.connect(self.worker.deleteLater)  # 线程结束时删除worker对象
   self.thread.finished.connect(self.thread.deleteLater)  # 线程结束时删除线程对象
   self.thread.start()  # 开始线程
   ```

2. logging记录日志信息

   ```python
   import logging
   # 初始化logger
   logging.basicConfig(
       level=logging.INFO, 
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
       filename='log.txt', 
       filemode='w', 
       encoding='utf-8'
   )
   # 添加一个StreamHandler用于控制台输出（可选）
   console_handler = logging.StreamHandler()
   console_handler.setLevel(logging.INFO)
   console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
   logging.getLogger('').addHandler(console_handler)
   logging.info("logger initialized")
   ```

3. 调整主题

   ```python
   from qt_material import apply_stylesheet
   import sys
   
   # 运行窗口程序
   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MainWindow()  # 创建窗口对象
       apply_stylesheet(app, theme='dark_blue.xml')
       window.show()  # 显示窗口
       app.exec()  # 运行程序
   ```

4. 检查ffmpeg修改后的情况

   ```python
   # 判断ffmpeg文件是否存在
   if not (os.path.isfile(ffpath.ffmpeg_path) and os.path.isfile(ffpath.ffprobe_path)):
   	self.textEdit.append("ffmpeg路径或ffprobe路径错误，请检查！")
   ```

# UpdateLog20240509

version-pre1.1弃用

## 弃用原因

异步多线程运行并不适用于ffmpeg视频处理，pre1.2将恢复到pre0.2的subprocess同步运行，解决假死并不必要，但是将尝试使用Thread多线程分开UI运行和FFmpeg运行

# UpdateLog20240508

![image-version-pre1.0](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre1.0.jpg)

优化代码结构，使用asyncio模块实现异步执行FFmpeg命令，使用logging模块实现格式化日志并输出日志

## 修改方向

1. **提高性能效率**：当前代码执行命令后立即等待命令执行完成，这会导致程序在执行命令时出现停滞。如果处理的视频文件较大，或者FFmpeg命令执行时间较长，这将严重影响程序的响应能力。可以考虑使用`asyncio.create_subprocess_exec`异步执行命令，以提高程序的响应性和执行效率。
2. **增强可维护性**：将命令行字符串的构建和执行封装成更具体的函数，比如`execute_cmd`。这样做可以提高代码的可读性和可维护性，同时也方便复用。
3. **日志记录**：目前代码使用`print`函数打印执行的命令和错误信息，这在调试阶段是可行的，但在生产环境中不够灵活。建议引入日志模块（如`logging`），这样可以更方便地控制日志级别，以及将日志输出到不同的地方（如文件、网络等）。
4. **异常处理的改进**：当命令执行失败时，抛出通用的`Exception`可能不是最好的选择。可以定义更具体的异常类，或者根据不同的错误情况抛出不同的异常，这样有助于调用者更准确地处理异常。
5. 优化subprocess代码

## 修改内容

1. class类名修改为FFmpegHandler，需要在main.py中修改
2. logging日志记录
3. 调整为asyncio异步执行
4. 调整debug到新文件

### 修改说明：

1. **安全性问题**：由于使用了异步执行命令`asyncio.create_subprocess_exec`，参数是按位置传递的，这避免了通过字符串拼接构造命令行命令的安全风险。
2. **异常处理**：增加了更详细的异常处理和日志记录，当发生异常时，会记录错误日志并抛出异常，便于问题的定位和解决。
3. **字符编码处理**：在`err.decode('utf-8', errors='ignore')`中增加了`errors='ignore'`参数，用于忽略编码错误，以提高代码的健壮性。
4. **提高性能效率**：通过使用`asyncio`异步执行命令，避免了在执行命令时的阻塞，提高了程序的响应性和执行效率。
5. **增强可维护性**：通过将日志记录引入，替代了直接使用`print`函数，提高了代码的可维护性和日志管理的灵活性。
6. **日志记录**：使用`logging`模块替代`print`进行日志记录，便于管理日志级别和输出。
7. **异常处理的改进**：对异常处理进行了改进，通过记录详细的错误日志并抛出异常，便于调用者根据异常信息进行精确处理。
8. **编码兼容性**：通过使用`asyncio.create_subprocess_exec`和`communicate`，以及合适的错误处理策略，提高了编码的兼容性。

## Debug

debug.py

### 发现问题：asyncio调用错误

如直接调用以下代码会报错

```python
def version(self):
    print(self.run_async(['-version']))
```

原因：由async来def的函数为一个coroutine function，调用时返回coroutine object而不会运行其中的程序

解决：①进入async模式

```python
coro = run_async(['-version'])
asynio.run(coro)
```

②将coroutine变为task

```
await run_async(['-version'])
```

### 发现问题：cmd传入ffmpeg报错

见issue-cmd.log

#### 可能原因，create_subprocess_exec传入错误

https://www.cnblogs.com/lxd670/p/17603616.html

https://www.jianshu.com/p/c7fba094ab42

```python
# 1.源码参数
async def create_subprocess_exec(
  program, 
  *args, 
  stdin=None, 
  stdout=None,
  stderr=None, loop=None,
  limit=streams._DEFAULT_LIMIT, **kwds
)

# 2.调用时入参
asyncio.create_subprocess_exec('ls -l',stdout=asyncio.subprocess.PIPE,stdin=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE)

# 3.相当于program 指向了 'ls -l'命令
# 4.系统中只有ls、pwd等这些命令，所以'ls -l'这个命令会报错说找不到这个命令文件(FileNotFoundError)
# 5.正确的解法应该是asyncio.create_subprocess_exec('ls', '-l', xxx),把命令和参数分开。
args = cmd.split(' ')
```

还有个问题就是直接在cmd运行、通过subprocess运行都可以在input、output_file路径和filter参数加上引号，但是asyncio不行，因为他是一项一项输入的，不需要引号做划分，这也是个坑点

## 进度

- [x] 对version函数的修改
- [x] 对extract函数的修改
  - [x] async def get_duration
  - [x] asyncio.run(run_async())
- [x] 对merge函数的修改
- [x] 处理overwrite事件（默认覆盖-y或不覆盖-n）

## 下一步修改目标

- [ ] overwrite选项UI实现
- [ ] 双文件合并选项核心逻辑实现、UI实现
- [ ] UI重构，为后续功能预留空间
  - [ ] 源代码链接
  - [ ] Browse同步textEdit
  - [ ] 每个功能一栏
- [ ] 后续功能预想
  - [ ] 单文件、多文件转码
  - [ ] 编码格式选项实现



