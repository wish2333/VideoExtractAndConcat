# VideoExtractAndConcat

## 使用要求

**依赖**

- ffmpeg

**第三方依赖库**

- pyside6 

**安装ffmpeg方法**

将ffmpeg解压进FFmpeg文件夹中，使得文件树结构为

- FFmpeg
  - bin
  - ...
- main.py
- ...

## Create 20240506-1911

上传了源代码，实现了批量处理片头片尾的问题

**目前存在的问题**

- 固定必须有片头和片尾，暂时缺失两个文件合并的情况
- 没能实现打包，等有空了在研究研究
- 待定
