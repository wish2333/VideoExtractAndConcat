# VideoExtractAndConcat

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
