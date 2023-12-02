from sklearn import datasets
import pandas as pd
from collections import Counter, defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


iris_datas = datasets.load_iris()

print(iris_datas.data) # 数据集中的数据
print(iris_datas.target_names) #  iris的种类

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

style_list = ['o', '^', 's']  # 设置点的不同形状，不同形状默认颜色不同，也可自定义
data = iris_datas.data
labels = iris_datas.target_names
cc = defaultdict(list)

for i, d in enumerate(data):
    cc[labels[int(i / 50)]].append(d)
p_list = []
c_list = []


for each in [0, 2]:
    for i, (c, ds) in enumerate(cc.items()):
        draw_data = np.array(ds)
        p = plt.plot(draw_data[:, each], draw_data[:, each + 1], style_list[i])
        p_list.append(p)
        c_list.append(c)

    plt.legend(map(lambda x: x[0], p_list), c_list)
    plt.title('鸢尾花花瓣的长度和宽度') if each else plt.title('鸢尾花花萼的长度和宽度')
    plt.xlabel('花瓣的长度(cm)') if each else plt.xlabel('花萼的长度(cm)')
    plt.ylabel('花瓣的宽度(cm)') if each else plt.ylabel('花萼的宽度(cm)')
    plt.show()


iris = pd.DataFrame(iris_datas.data, columns=['SpealLength', 'Spealwidth', 'PetalLength', 'PetalLength'])
iris.describe()

# 数据直方图
# 之前已经使用过describe()计算出四个属性所对应的四分位数, 最大值以及最小值等统计量。这些均是以表格的形式展示。

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
dataset.hist() #数据直方图histograms
plt.show()

# 散点图
# x轴表示sepal-length花萼长度，y轴表示sepal-width花萼宽度

dataset.plot(x='sepal-length', y='sepal-width', kind='scatter')
plt.show()

# KDE图
# KDE图也被称作密度图(Kernel Density Estimate,核密度估计)。

dataset.plot(kind='kde')
plt.show()

# 箱线图
# kind='box’绘制箱图,包含子图且子图的行列布局layout为2*2，子图共用x轴、y轴刻度，标签为False。

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

