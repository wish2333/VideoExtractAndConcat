# VideoExtractAndConcat

**项目概述**

本项目旨在开发一个用户友好的图形界面应用程序，用于视频片头和片尾的快速切割与合并功能。通过集成Qt Designer设计的界面与Python编程语言，结合强大的ffmpeg工具，用户能够轻松指定视频文件、设置切割时间点，完成视频处理任务。项目最终目标是提高视频编辑效率，尤其适合需要批量处理视频的用户。

**未完成的优化，计划的项有：**

- [x] 优化性能
- [x] 中止处理
- [x] 允许调出控制台
- [x] 使FFmpeg运行时的输出返回到控制台
- [x] 使合并流程能够识别两段视频的合并（目前必须同时传入片头片尾）
- [x] 窗口美化
- [x] 打包依赖库
- [x] 封装bat或exe
- [x] 其他
   - [x] 加速滤镜功能
   - [x] 切割时间段功能
   - [ ] 其他见更新日志

## 使用指南（20240507/20240513）

下载release包，解压后打开exe或bat文件即可！

ffmpegApi.py更新见[DETAIL20240513.md](docs/DETAIL20240513.md)

## 源码使用指南（20240506）

1. 安装python环境和第三方库pyside6

```
pip install pyside6
```

2. 安装FFmpeg到main.py目录下，文件树结构如下

```
├── FFmpeg        # 注意大写           
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

4. 不安装pyside6、不调用gui，以代码形式运行，可以对ffmpegApi.py直接调用：见[DETAIL20240506.md](docs/DETAIL20240506.md)中调试用代码部分。

## 快照

![version-pre3.0](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre3.0.jpg)

![version-pre2.0](https://github.com/wish2333/VideoExtractAndConcat/blob/master/docs/snapshot/VideoExtractAndConcat-version-pre2.0.jpg)

# 更新日志

详细日志见[UpdateLog-version-pre3.0-.md](docs/UpdateLog-version-pre3.0-.md)、[UpdateLog-version-pre0.1-pre2.0.md](docs/UpdateLog-version-pre0.1-pre2.0.md)

## 规划进度

- [ ] 视频批处理界面
   - [x] 锁片头尾
   - [ ] 转码参数
      - [ ] 码率bug
      - [ ] 提示
   - [ ] 添加音轨
- [x] 视频单文件界面
   - [x] 音视频及内含字幕混流
- [ ] 音频界面
   - [ ] 批量处理音频
   - [ ] 加封面
- [ ] 字幕界面
   - [ ] 批量添加字幕
- [x] ffmpeg自定义参数界面
   - [x] 复杂滤镜
- [ ] 读取界面
   - [ ] ffprobe
- [x] 设定界面
   - [x] ffmpeg路径设置→每次封装记得删ini里面的参数
- [x] 关于界面
- [x] 转封装
- [ ] 提取音频视频字幕等等
- [x] 进程中止
   - [x] 发出中止信号→导致软件闪退
   - [x] subprocess中止
- [x] 自动剪辑界面

## Update20240608-version-1.0

VautocutInterface用于自动剪辑（剪气口导出视频/音频/工程文件/切片、转码、切割、加速）

## Update20240608-version-pre5.0

remuxInterface用于转封装和提取（未实现）

VfilterInterface用于处理旋转等复杂滤镜模块（额外功能：音频标准化）

## Update20240519-version-pre4.2

**version-pre4.1-interrupt**

视频批处理面板完成了中断按钮及逻辑实现（通过中断标志和回调函数向api模块的传输与接受），api模块通过守卫线程实现中断操作并调用回调函数传输中断完成标志。

**version-pre4.2-avsmix**

完成了视频面板（单文件）的音视频及字幕混流合成。

修复了中断后守卫线程t没有被正确关闭的错误。

## Update20240516-version-pre4.0

实现了常规界面about\setting，支持修改FFmpeg，优化视频界面

## Update20240513-version-pre3.0

实现批处理界面，添加了加速、切割时间段和合并片头片尾功能，部分逻辑以及API接口函数有所修改，后续调用需要注意

## Update 20240511-version-pre2.0

UI重构，参考[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)和[MihiroToolbox](https://github.com/Eanya-Tonic/MihiroToolbox)构造UI和功能分布

目前仅完成单文件（音视频）转码裁切的功能面板，且功能暂未完善（如字幕封装、音频替换封装等）

脱离了PyInstaller封装，暴露源代码。暂未优化大小，未来可以精简。

## Update 20240510

返回到pre0.2进行，优化代码结构，重新使用同步执行FFmpeg命令，使用logging模块实现格式化日志并输出日志。通过QObject、QThread和Singal实现多线程，确保UI不假死，实际上多线程没有优化性能的作用，只是不希望程序假死，优雅！

### 调整内容

#### ffmpegApi.py

实时返回ffmpeg执行命令（实际上并不实时而是需要等待某一步进行完成后才能返回，因而尚不能实现返回进度条→是不是去掉while True的判断就行了？笑哭）

#### main.py

1. 多线程设置
2. logging记录日志信息
3. 调整主题
4. 检查ffmpeg修改后的情况

## Update 20240509-2206

version-pre1.1弃用

### 弃用原因

异步多线程运行并不适用于ffmpeg视频处理，pre1.2将恢复到pre0.2的subprocess同步运行，解决假死并不必要，但是将尝试使用Thread多线程分开UI运行和FFmpeg运行

## Update 20240509-1530

优化代码结构和模块调用，使用asyncio模块实现异步执行FFmpeg命令，使用logging模块实现格式化日志并输出日志

### 进度

- [x] 对version函数的修改
- [x] 对extract函数的修改
   - [x] async def get_duration
   - [x] asyncio.run(run_async())
- [x] 对merge函数的修改
- [x] 处理overwrite事件（默认覆盖-y或不覆盖-n）

# 

## Release 20240508-1517

调整了封装结构，使得ffmpeg能够被正确识别（ffmpeg封装将在star>100时取消）

## Release 20240507-1904

发布封装包，可以优雅运行程序啦，就是pyinstaller封装出来的东西大小是在太感人了，再寻思寻思别的封装技术

## Create 20240506-1911

上传了源代码，实现了批量处理片头片尾的问题

**目前存在的问题**

- 固定必须有片头和片尾，暂时缺失两个文件合并的情况
- 没能实现打包，等有空了在研究研究
- 待定

# 参考项目

[FFmpeg](https://ffmpeg.org/download.html)

[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

[auto-editor](https://github.com/WyattBlue/auto-editor)

[MihiroToolbox](https://github.com/Eanya-Tonic/MihiroToolbox)
