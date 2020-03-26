# - 

## 包管理

`$pip freeze > requirements.txt`

`$pip install -r requirements.txt`

## 安装源

但有时候因为网络问题，并无法安装成功，毕竟pip默认的官网源在国外，这时候我们可以使用国内的pip源，你会感受到飞一般的下载速度。我常用的是aliyun的pip源，当然国内还有很多其他源供你选择，在此就不一一列出了。

切换国内源分为临时性和永久性两种，如果只是该次使用，在命令行后添加相应参数即可：

```
# 指定包名安装

pip install package -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com`

# 依据requirements.txt安装

pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

如果是想永久切换，可通过修改pip配置文件来达到此目的：

linux下修改~/.pip/pip.conf，如果没有该文件则创建；

windows下修改%HOMEPATH%\pip\pip.ini，如果没有则创建；

```
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple/
```

## 大致分类

纯python编写的软件包
c/c++语言编写的软件包
针对第二类情况，你需要确保系统上有对应的c/c++编译器及python开发者工具才能装包成功。

linux各个发行版，要先确保gcc、g++已经安装，然后再安装python开发者工具，以redhat/centos为例：
```
yum install gcc gcc-c++
yum install python-devel
# 或安装对应python版本的开发者工具
yum install python3-devel
yum install python36-devel
```
Debian/Ubuntu dev工具名字稍有不同，但思路一样
```
apt-get install python-dev
```
windows则需要安装vc++ for python x.x(即python对应的版本号)，或者使用MinGw进行编译，参考阅读[Microsoft Visual C++ Compiler for Python 3.4](https://stackoverflow.com/questions/29909330/microsoft-visual-c-compiler-for-python-3-4)

如果你实在觉得麻烦，还有一个[网站](https://www.lfd.uci.edu/~gohlke/pythonlibs/)专门提供windows下的各种python包，可在不具备编译环境的情况下，选择合适自己的python环境进行安装，使用方法非常简单，pip install xxx.whl即可。
​
这个站点虽然不是万能的，但应付大部分在windows下开发的pythoner已经绰绰有余

>https://zhuanlan.zhihu.com/p/70776169

>https://medium.com/@dayuoba/python%E5%8C%85%E7%AE%A1%E7%90%86-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5-f4bc7ec1e61e