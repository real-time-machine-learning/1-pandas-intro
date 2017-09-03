# 利用Pandas分析离线股票数据(秒级记录)

这里我们将会介绍如何用Pandas进行简单的数据分析和可视化操作。这样的步骤
往往是进行机器学习建模、读懂数据的第一步。

## 下载本章节示例程序

下载本章节实例程序和数据，只需执行下面操作：

```shell
git clone https://github.com/real-time-machine-learning/1-pandas-intro
```

## 安装配置软件环境

我们假设读者在Ubuntu或者Mac环境下进行学习。下面的步骤可以供Windows用户
参考，但可能需要稍作修改。

### 安装Python3 

在Ubuntu 下面安装Python 3，只需执行下面操作：
```shell
sudo apt-get install python3 python3-pip python3-dev build-essential libffi6 libffi-dev
```
在Mac下利用Homebrew 安装Python 3，只需执行下面操作：
```shell
brew install python3
```
Windows用户……安装一下Ubuntu好吗？

### 安装Pandas

这里我们通过Python的Pip配置文件的方法安装pandas。在后面的Docker学习中，
我们可以看到这样的配置方法非常利于自动化Docker操作。

```shell
sudo pip3 install -r requirements.txt
```

如果一切顺利，上面操作完成以后，我们可以启动Python3并且调用Pandas
```shell
python3 
>>> import pandas as pd
```

## Pandas基本操作

下面我们将利用`example.py`中的操作介绍pandas的基本模块。

## 鸣谢

感谢下面各位为本代码提出宝贵意见和指正：

 - [张野飞](https://github.com/351zyf) 

--- 

《实时机器学习实战》 彭河森、汪涵

