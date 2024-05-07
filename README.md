# VideoExtractAndConcat

**项目概述**

本项目旨在开发一个用户友好的图形界面应用程序，用于视频片头和片尾的快速切割与合并功能。通过集成Qt Designer设计的界面与Python编程语言，结合强大的ffmpeg工具，用户能够轻松指定视频文件、设置切割时间点，完成视频处理任务。项目最终目标是提高视频编辑效率，尤其适合需要批量处理视频的用户。

**未完成的优化，计划的项有：**

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

# 更新日志

## Create 20240506-1911

上传了源代码，实现了批量处理片头片尾的问题

**目前存在的问题**

- 固定必须有片头和片尾，暂时缺失两个文件合并的情况
- 没能实现打包，等有空了在研究研究
- 待定
