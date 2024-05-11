#### 将.py文件打包成.exe文件

- [创建虚拟环境安装相应的包](https://blog.csdn.net/jpython0/article/details/127912468#_1)
- [使用auto-py-to-exe](https://blog.csdn.net/jpython0/article/details/127912468#autopytoexe_19)



## [创建虚拟环境](https://so.csdn.net/so/search?q=创建虚拟环境&spm=1001.2101.3001.7020)安装相应的包

首先[打开cmd](https://so.csdn.net/so/search?q=打开cmd&spm=1001.2101.3001.7020)创建虚拟环境

```powershell
conda create --name pyside2 python=3.9
1
```

进入虚拟环境

```powershell
conda activate pyside2
1
```

![img](https://img-blog.csdnimg.cn/372ae6941c6045ac8f16650efb79ee1d.png)
安装相应的包，pyside2或者pyqt5等等。。。
最后安装`auto-py-to-exe`

```powershell
pip install auto-py-to-exe
1
```

## 使用auto-py-to-exe

虚拟环境下输入`auto-py-to-exe`
![在这里插入图片描述](https://img-blog.csdnimg.cn/0f2405ae893d4b5fb12140d78496603b.png)
然后跳出这个界面
![在这里插入图片描述](https://img-blog.csdnimg.cn/d17e43af42aa494f822d063dd64f9b9a.png)
**附加文件说明：**
添加文件：是指单独添加你自己写的.py文件路径
添加目录：你自己写的一堆.py文件放在一个包内，然后把包的路径添加进去
添加空白：我也不懂，感觉没啥用（大佬勿喷，本人小白一个）
![在这里插入图片描述](https://img-blog.csdnimg.cn/295f96593a344b7e8525e29dfcdad754.png)
点击蓝色按钮运行，当看到这两行，就打开输出目录。
![在这里插入图片描述](https://img-blog.csdnimg.cn/68dfe9da9f6c4b82a4e517afb0a0a821.png)
一般会以主文件名字命名文件夹，我的是main.py，文件夹名字就是main，打开文件夹，里面 有main.exe，先回想下你的项目有没有依赖的txt，xml，cfg，csv，xslx之类的文件，把这些文件放入到主文件引用的位置。最后双击main.exe运行。

这个方法比pyinstaller方便多了，喜欢的点个赞吧。

## 使用嵌入式包+get-pip封装

