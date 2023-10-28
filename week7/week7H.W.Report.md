# week7 HomeWork Report 

## 

### 第十一章践习题 参考了助教的思路，以下只是为了查阅方便粘贴到了自己的仓库：

**题目5：﻿﻿通过梯度下降法，给出 Logistic 回归模型的求解过程，请写出详细的推导过程**

**参考答案：**

Logistic回归是一种广泛用于二元分类问题的统计分析方法。虽然它的名称中含有“回归”，但实际上它是用于分类任务的。在这里，我们将深入探讨如何通过梯度下降法手动解决Logistic回归问题。我们首先从Logistic回归模型的基本原理谈起，然后讨论梯度下降法如何应用于优化问题。

### Logistic 回归模型基础

1. **Sigmoid 函数**:
    Logistic回归使用Sigmoid函数，将线性回归结果映射到[0,1]区间，用于预测二元目标变量的概率。Sigmoid函数定义如下：
    $$
    \sigma(z) = \frac{1}{1 + e^{-z}}
    $$

2. **模型假设**:
   Logistic回归模型假设目标变量`y`的对数几率是输入`X`的线性组合。这里，`z`代表线性组合：`z = w^T X + b`，其中`w`是权重向量，`b`是偏差项。

3. **代价函数**:
   我们使用交叉熵损失函数，因为这会使得梯度下降优化更加有效。对于单个数据点，损失函数是：
   $$
   J(w, b) = -y \log(\sigma(z)) - (1 - y) \log(1 - \sigma(z))
   $$
   对于整个训练集，代价函数是所有训练样本损失的平均。

### 梯度下降求解

梯度下降是一种迭代优化算法，用于最小化代价函数。基本思想是计算代价函数的梯度，并沿着减少最快的方向调整参数。

1. **计算梯度**:
   首先，我们需要计算代价函数相对于模型参数的梯度。对于权重`w`和偏差`b`，梯度计算如下：
   $$
   \frac{\partial J}{\partial w} = \frac{1}{N} \sum_{i=1}^{N} (\sigma(z^{(i)}) - y^{(i)})x^{(i)}
   $$
   $$
   \frac{\partial J}{\partial b} = \frac{1}{N} \sum_{i=1}^{N} (\sigma(z^{(i)}) - y^{(i)})
   $$
   其中`N`是训练样本的数量。

2. **更新规则**:
   然后，我们用以下规则更新参数：
   $$
   w = w - \alpha \frac{\partial J}{\partial w}
   $$
   $$
   b = b - \alpha \frac{\partial J}{\partial b}
   $$
   其中，`α`是学习率，控制我们更新参数的步长。

3. **迭代优化**:
   通过多次迭代过程，我们不断用计算出的梯度更新参数，直到代价函数收敛为止。

### 算法步骤总结

1. 初始化模型参数（通常初始化为0或小的随机值）。
2. 计算模型的预测输出。
3. 计算代价函数（损失）。
4. 计算代价函数的梯度。
5. 更新模型参数。
6. 重复步骤2-5，直到满足停止准则（例如，达到预定的迭代次数，或代价函数的改变非常小）。

通过这个过程，模型最终学习到数据的权重参数，用于对新的输入数据进行预测。这就是使用梯度下降法进行Logistic回归的基本过程。实际应用中可能需要考虑更多复杂的因素，如特征缩放、正则化以及更高级的优化算法等。



## 习题6

**题目：下载鸢尾花数据集，编程实现如下功能：**

* 读取数据文件
* 将数据随机打乱，并按照3:7的比例划分测试集和训练集

**提示：**

1. 鸢尾花数据集可以直接从`sklearn`的函数进行下载（`sklearn.datasets.load_iris()`）
2. 可以使用`sklearn`的函数`train_test_split`，也可以用`numpy`和`pandas`完成



## 习题7

**题目：通过logistics回归解决鸢尾花数据集分类问题**

**参考答案：**

首先，确保已经安装了必要的库：
```bash
pip install scikit-learn
```

接下来，您可以按照以下步骤进行操作：

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 数据标准化（通常对于Logistic回归是一个好的做法）
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 4. 创建Logistic回归模型
clf = LogisticRegression(max_iter=1000)  # max_iter定义了求解算法的最大迭代次数

# 5. 训练模型
clf.fit(X_train, y_train)

# 6. 进行预测
y_pred = clf.predict(X_test)

# 7. 计算和打印准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
```

上述代码首先加载了鸢尾花数据集，并将其分为训练集和测试集。然后，我们对数据进行了标准化，这对于Logistic回归非常有用，因为它依赖于数据的尺度。接下来，我们定义和训练了Logistic回归模型，并最终在测试集上评估了其性能。

注意：这只是一个简单的例子。在实际应用中，您可能还需要考虑交叉验证、超参数调优等步骤。



## 习题8

**题目：编程计算鸢尾花数据集中不同标签类别数据的中心点，即各维度的均值，并计算数据点到中心点的欧式距离**

**参考答案：略**



## 习题9

**题目：K-means算法是一种有效的聚类算法，请编程实现K-means算法对鸢尾花数据集进行聚类**

**参考答案：**

下面是一个简单的Python脚本，用于在鸢尾花(Iris)数据集上执行K-means聚类。这个脚本使用了`scikit-learn`库，这是一个在Python中进行机器学习操作的非常流行和强大的库。

首先，请确保已经安装了`scikit-learn`库。如果还没有安装，可以使用以下命令安装：

```sh
pip install scikit-learn
```

以下是使用K-means进行聚类的代码：

```python
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 我们只取特征空间用于K-means聚类

# K-means聚类
kmeans = KMeans(n_clusters=3)  # 选择3作为聚类数量，因为我们知道有三类鸢尾花
kmeans.fit(X)

# 获取聚类标签和中心点
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_

# 可视化聚类结果
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')  # 根据K-means聚类的标签给每个点上色

# 画出聚类的中心点
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, alpha=0.75)

plt.title("K-means Clustering on Iris Dataset")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()
```

### 第十二章践习题

**题目4：﻿﻿通过Tensorflow或者 Pytorch 编实现神经网络模型完成尾花数据集的分类**

**A：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/12.4.png "")**

### 

**题目5：﻿﻿任选一张图片,利用深度学习的方法编实现如下功能:**

**(1)将图片转换为灰度图像**

**(2)将图片放缩成指定大小****

**A：原图为：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/imagetest.jpg "")**

**灰度图像：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/12.5a.png "") 缩放后：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/12.5b.png "")**



**题目7：通过Tensorflow 或者 Pytorch,构建 LeNet -5 模型**

**A：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/12.7.png "")**

**题目8：﻿﻿基于 mnist数据集和 LeNet-5模型自设定参数训练题目 7中定义的模型**

**A：![](https://github.com/jiyeoniya/2023fall/blob/main/week7/12.8.png "")**

**实践：实践：Python 深度学习——手写汉字识别**

**目前有许多基于深层卷积神经网络的手写字体识别研究!如手写数字和手写英文字母。这些研究证明良好设计的卷积神经网络结构能够非常有效地识别手写字体。这激发了越来越多的人研究卷积神经网络在面对更复杂的手写字符时是否有良好的表现"
与手写数字识别任务相比，手写汉字识别是一个更加复杂和有挑战性的工作"首先汉字数量非常多!仅常用汉字就多达三千多个，而相比之下数字只有十个0其次，汉字字符
相比数字字符有更多的笔画和更复杂的组合结构，这意味着汉字字符包含了非常复杂的特征，图!121"展示了手写数字与手写汉字的对比0另外，不同人之间的手写汉字字
体风格差异巨大，一些人的字迹更是存在着偏旁部首粘连在一起的情况"本节实践将展示如何应用深度学习技术!构建手写汉字识别模型**


**A：主要参考了下面这个仓库以及推文：**


https://github.com/chenyr0021/Chinese_character_recognition/tree/master

https://blog.csdn.net/qq_31417941/article/details/97915035

**因此不做过多阐述。**
