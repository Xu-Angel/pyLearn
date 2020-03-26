python -> 2.7
https://www.python.org/downloads/
open /System/Library/Frameworks/Python.framework/Versions
which python3
vi ~/.zshrc
alias pyp3
source ~/.zshrc
pyp3 -V
pip3 -V

```
https://docs.python.org/zh-cn/3.8/using/mac.html#getting-and-installing-macpython
Mac OS X 10.8 附带 Apple 预安装的 Python 2.7 。 如果你愿意，可以从 Python 网站（ https://www.python.org ）安装最新版本的 Python 3 。 Python 的当前“通用二进制”版本可以在 Mac 的新 Intel 和传统 PPC CPU 上本地运行。

你安装后得到的东西有：

应用程序文件夹中的 Python 3.8 文件夹。在这里可以找到IDLE，即官方Python发行版的标准的开发环境；PythonLauncher，用来处理来自finder的双击python脚本；以及“build applet”工具，将python脚本打包为系统上的独立应用程序。

框架 /Library/Frameworks/Python.framework ，包括 Python 可执行文件和库。安装程序将此位置添加到 shell 路径。 要卸载 MacPython ，你可以简单地移除这三个项目。 Python 可执行文件的符号链接放在 /usr/local/bin/ 中。

Apple 提供的 Python 版本分别安装在 /System/Library/Frameworks/Python.framework 和 /usr/bin/python 中。 你永远不应修改或删除这些内容，因为它们由 Apple 控制并由 Apple 或第三方软件使用。 请记住，如果你选择从 python.org 安装较新的 Python 版本，那么你的计算机上将安装两个不同但都有用的 Python ，因此你的路径和用法与你想要执行的操作一致非常重要。


```