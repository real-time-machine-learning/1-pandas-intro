
"""《实时机器学习实战》彭河森、汪涵

数据分工具Pandas介绍

这里我们将熟悉Pandas的基本模块，并且利用Pandas以及相关工具分析秒级股票
报价数据。
""" 

import pandas as pd 
from datetime import datetime

"""数据导入

这里我们将会导入2015年8月3日苹果公司的秒级股票交易数据，这里的原始数据
需要进行稍许清理才能使用，正好符合我们本章节的学习要点。
"""

## 这里我们用了Pandas的read_csv模块直接从csv文件中导入数据。

data = pd.read_csv("aapl.csv",
                   names = ["timestamp_raw","Open","High",
                            "Low","Close","Volume"],
                   index_col = False)

## 得到的 data 对象是一个DataFrame 
print(type(data))

## 看看数据长什么样，在交互窗口中打印前5行和后5行。我们可以注意到估价为
## Open, High, Low, Close, Volume格式。记录中的数值为原始股价乘以
## 10000。
data.head(5)

data.tail(5)


## 原始数据中的时间记录为每天距离格林威治标准时间的秒数乘以1000，为增加
## 可读性，我们需要将数据还原。这里我们让data对象的索引变为了处理后的时
## 间标记，调用了DataFrame.index域。

UNIX_EPOCH = datetime(1970, 1, 1, 0, 0)
def ConvertTime(timestamp_raw, date):
    """ 该函数会将原始的时间转化为所需的datetime格式 """
    delta = datetime.utcfromtimestamp(timestamp_raw) - UNIX_EPOCH
    return date + delta   

data.index = map(lambda x: ConvertTime(x, datetime(2015, 8, 3)),
                 data["timestamp_raw"]/1000)

## 这个时候timestamp_raw一列不在有用，我们可以删掉它。这里我们调用了
## DataFrame.drop()函数

data = data.drop("timestamp_raw",1)

"""数据基本操作 

我们可以调用DataFrame对象的函数对其进行各种基本的修改和描述。下面是一些
例子：
""" 

## DataFrame 的很多操作是通过调用对象的函数进行的，具体有哪些函数呢？我
## 们可以用dir()命令查看。哇，好多函数是不是？

dir(data)

## 一些常用的函数包括 mean(均值)，max(最大值)，min(最小值)等。

data.mean()

## 同时也可以调用describe 函数直接产生常用的大多统计量。
data.describe()

## 看看交易时间是什么时候？上面的操作也可以执行在data.index上面。这里
## DataFrame.index相当于一个Series对象。

data.index.min()
data.index.max()

## 我们可以看到交易时间其实包括了盘前和盘后大量时间。在实际交易策略中，
## 我们往往只会在正常交易时间进行交易。所以需要对数据按照时间进行拆分。
## 这样的操作非常容易：

data_trading_hour = data["201508030930":"201508031529"]

## 将交易时间的数据保存起来供后面使用：

data_trading_hour.to_csv("aapl-trading-hour.csv")

""" 可视化操作

对每一秒收盘价进行可视化操作：
""" 

import matplotlib
from matplotlib import pyplot as plt


## 设置画图风格为R的ggplot风
matplotlib.style.use('ggplot')

## 每秒收盘价是什么样子的走势？可以这么看

data_trading_hour["Close"].plot()
## plt.savefig("plots/closing-price-plot.png")
plt.show()

## 每秒成交量是什么样的分布？我们可以做出直方图:

data_trading_hour["Volume"].plot.hist()
## plt.savefig("plots/volume-histogram.png")
plt.show()

## 怎么会这样？看看是否具有特别大的成交量出现？果然如我们假设，中午时分
## 有大单交易发生。

data_trading_hour["Volume"].describe()

data_trading_hour["Volume"].plot()
## plt.savefig("plots/volume-plot.png")
plt.show()

"""收盘价变化率初探

当然做实时量化交易我们最感兴趣的还是每秒的变化率。那么我们来看看股价变
化有什么样的分布。
"""

## 下面我们可以看到，Series对象的很多操作可以链式在一行完成，非常方便：

data_trading_hour["Close"].diff().plot.hist()
## plt.savefig("plots/price-change-histogram.png")
plt.show()

change = data_trading_hour["Close"].diff()/data_trading_hour["Close"]
change.plot()
## plt.savefig("plots/price-change-plot.png")
plt.show()

## 看看前一秒变化率和后一秒变化率之间的关系。

change.shift(1).corr(change)
change.shift(2).corr(change)

## 系统性的看看相差时间长度和相关性变化之间的差距：

plt.acorr(change[1:], lw = 2)
## plt.savefig("plots/price-change-auto-correlation.png")
plt.show()

## 哇，没想到相关程度这么大，那我们在后面好好利用这样的性质做做文章。
