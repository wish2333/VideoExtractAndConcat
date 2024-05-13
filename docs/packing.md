#### 将.py文件打包成.exe或.bat文件

- [使用嵌入式包+get-pip封装](https://blog.csdn.net/ScienceRui/article/details/103612099)
- [创建虚拟环境安装相应的包](https://blog.csdn.net/jpython0/article/details/127912468#_1)
- [使用auto-py-to-exe](https://blog.csdn.net/jpython0/article/details/127912468#autopytoexe_19)

## 使用嵌入式包+get-pip封装

**下载嵌入式（绿色版）——Embeddable Python**

第一步，从Python官网:https://www.python.org/下载嵌入式Python包。具体的操作如下图所示，这里有以下2点**注意事项**：

> - 要下载的是带“embeddable”的Python，**而不是**的带“executable”字样的Python
> - 嵌入式Python可以理解为是一个精简版的、免安装的Python，其不包含常用的pip包管理工具、tkinter等基本的包。

**下载并安装Python包管理工具——pip**

- Python的包管理工具pip，其本身也是一个Python包，嵌入式Python默认没有安装，因此，为了使用第三方Python包，这里首先得安装pip工具。下载网址：https://bootstrap.pypa.io/get-pip.py，具体的安装方法如下图所示。
- **注意事项：**get-pip.py文件可以放在任何目录，不一定要如下图所示放在解压了的文件中。一定要注意修改python37_.pth文件，也即取**消该文件中对"import site"的注释**，依次让嵌入式的Python解释器初始化时导入site模块

**使用pip下载并安装其它Python包**

- 使用pip工具为嵌入式的Python安装其它第三方包，如：numpy、pandas、matplotlib、PyQt5、scikit-learn等，这与小编之前写的文章——“1.2 第三方Python包的安装——Pip命令的使用”几乎相同，唯一不同的点是，这里安装第三方包，**要指定用嵌入式的Python解释器来执行pip命令**（因为我们不希望使用系统中已有的Python来执行，否则就是为系统中的Python安装第三方包了），**同时要加入“-m”参数**，以此指定以导入模块的方式执行pip（即先导入pip到嵌入式Python环境，在执行pip命令），而非直接执行pip命令，直接执行pip命令，会提示类似“无法找到pip所在的文件和目录”的错误。正常安装的Python已经将pip工具所在的目录加入到环境变量，所以，在Python环境不冲突的情况下，无需指定解释器，无需加上pip参数。具体来说，嵌入式Python使用pip安装第三方包的命令如下（这里的路径取决于你的嵌入式Python解压后存放的路径,可对比一下与“1.2 第三方Python包的安装——Pip命令的使用”文中的不同）：

- 下方命令中D:\路径\python.exe可以是先cd进入目录然后用python，pip(3) 可能不需要带3

- | 命令                                                      | 作用                                                         |
  | --------------------------------------------------------- | ------------------------------------------------------------ |
  | D:\路径\python.exe -m pip(3) list                         | 查看已安装的Python包，该命令将罗列出所有安装了的Python包     |
  | D:\路径\python.exe -m pip(3) list -outdate                | 查看已安装的有更新的Python包，该命令将罗列出所有安装了的过时的Python包 |
  | D:\路径\python.exe -m pip(3) install + 包的名称或路径     | 加包的名称时，边下载，边安装Python包；加包的路径时，安装已下载了的Python包 |
  | D:\路径\python.exe -m pip(3) install 包的名称==x.x.x      | 用两个等号来安装指定版本的Python包，这里（x.x.x为版本号）    |
  | D:\路径\python.exe -m pip(3) uninstall + 包的名称         | 卸载指定的Python包                                           |
  | D:\路径\python.exe -m pip(3) install --upgrade + 包的名称 | 更新指定的包到最新的release版本                              |

**记得删除第三方库中多余的文件，否则打包巨大**

**创建bat，如下方**

```bat
cd runtime
python main.py
```



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

