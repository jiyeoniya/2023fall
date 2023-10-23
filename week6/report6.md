# WEEK6 H.W. REPORT

## 第一题：

### Q:使用 numpy 生成服从标准正态分布的 100 个样本。

#### A：使用numpy中的random.normal函数，用于生成服从标准正态分布的随机数，它有三个参数

    loc: 均值，默认为0
    scale: 标准差，默认为1
    size: 输出的形状，默认为None，即只输出一个值
  如果只提供均值和标准差，函数将返回一个符合指定均值和标准差的单个随机数。例如，np.andom.normal(1,1)将返一个符合均值为1，标准差为1的正态分布随机数。
  如果提供了均值、标准差和形状，函数将返回一个符合指定均值、标准差和形状的随机数数组。例如，np.random.norma(2,1,(2.2))将回一个形状为(2.2)，均值为2，标准差为1的正态分布随机数数组
  总结来说，np.fandom.nomal函数的作用是生成符合正态分布的随机数，可以通过设置均值、标准差和形状来调整生成的随机数的特征。则运行结果如下：

![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob1.png "")

## 第二题：

### Q:通过 Python 程序为抽样出的样本绘图展示。

#### A：第二题为第一题的延伸，我们可以使用 pyplot 中的 hist() 方法来绘制直方图。hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数。hist() 方法可以用于可视化数据的分布情况，例如观察数据的中心趋势、偏态和异常值等。

#### hist() 方法语法格式如下：

    matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)

参数说明：

    x：表示要绘制直方图的数据，可以是一个一维数组或列表。
    bins：可选参数，表示直方图的箱数。默认为10。
    range：可选参数，表示直方图的值域范围，可以是一个二元组或列表。默认为None，即使用数据中的最小值和最大值。
    density：可选参数，表示是否将直方图归一化。默认为False，即直方图的高度为每个箱子内的样本数，而不是频率或概率密度。
    weights：可选参数，表示每个数据点的权重。默认为None。
    cumulative：可选参数，表示是否绘制累积分布图。默认为False。
    bottom：可选参数，表示直方图的起始高度。默认为None。
    histtype：可选参数，表示直方图的类型，可以是'bar'、'barstacked'、'step'、'stepfilled'等。默认为'bar'。
    align：可选参数，表示直方图箱子的对齐方式，可以是'left'、'mid'、'right'。默认为'mid'。
    orientation：可选参数，表示直方图的方向，可以是'vertical'、'horizontal'。默认为'vertical'。
    rwidth：可选参数，表示每个箱子的宽度。默认为None。
    log：可选参数，表示是否在y轴上使用对数刻度。默认为False。
    color：可选参数，表示直方图的颜色。
    label：可选参数，表示直方图的标签。
    stacked：可选参数，表示是否堆叠不同的直方图。默认为False。
    **kwargs：可选参数，表示其他绘图参数。

plt.xlim（）这个函数主要用于获取或设置x轴的范围，xmin 和 xmax 分别是x轴的最小值和最大值。

np.linspace(start, stop, num)：以指定的起始点、终止点和样本数量生成等间距的数值点。

np.exp(x)：计算exp()的值。

plt.plot(x, y, color, linewidth)：绘制函数的曲线，其中x和y是数据点的横纵坐标列表，color指定曲线的颜色，linewidth指定曲线的线宽。

plt.title(label)：设置图形标题。

plt.xlabel(label)：设置X轴标签。

plt.ylabel(label)：设置Y轴标签。

plt.show()：显示图形。

#### 最后运行结果如下：
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob2.png "")

## 第三题：

### Q:通过 Python 程序计算矩阵[[2, 1],[4, 5]]的特征值和特征向量

#### A：在NumPy中，我们可以借助numpy.linalg.eig()计算给定方阵的特征值和右特征向量。它将一个正方形数组作为参数，它将返回两个值，第一个是数组的特征值，第二个是给定正方形数组的右特征向量。参数为方阵。

#### Return:它将返回两个值，第一个是特征值，第二个是特征向量。则运行结果如下：

![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob3.png "")

## 第四题：

### Q:请用编程幂迭代法计算矩阵[[2, 1],[4, 5]]的最大特征值

#### A：实现了使用幂迭代方法计算矩阵的最大特征值和对应的特征向量。其中涉及到的变量和操作含义如下：

    A：创建一个2x2的浮点型矩阵A。
    v0：创建一个初始特征向量v0，包含两个浮点数。
    eps：设置收敛精度，用于判断特征值是否收敛。
    eig_power(A, v0, eps)：调用幂迭代方法求解矩阵A的最大特征值和特征向量。
    uk：初始化特征向量为初始特征向量v0。
    flag：迭代终止标志位，初始设置为1。
    val_old：上一次迭代的特征值，初始设置为0。
    n：迭代次数。
    vk：将矩阵A与特征向量uk相乘得到新的特征向量vk。
    val：从vk中选取绝对值最大的元素作为当前迭代的特征值。

其运行结果如下：
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob4.png "")


## 第五题：

### Q:给出数据矩阵如下,通过 Python 程序计算协方差矩阵 C

Data    | 1 | 2 | 3
-------- | ----- | ----- | -----
X  | 1 | -1 | 4
Y  | 2 | 1 | 3
Z  | 1 | 3 | -1


#### A：在NumPy中，我们可以借助numpy.cov()计算给定方阵的协方差矩阵。Return:它将返回给定方阵的协方差矩阵。则运行结果如下：

![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob5.png "")

## 第六题：

### Q:通过幂迭代法计算上述协方差矩阵的全部特征值和特征向量

#### A：该题和第四题类似，不再做赘述。运行结果如下：

![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob6.png "")

## 第七题：

### Q: 10.5 实践：Python 统计分析-- 10.5.1文本词频统计

#### A：因为需要一个文本，所以自己随便写了一个txt文本：
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob7b.png "")

运行结果如下：
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/prob7.png "")

## 第八题：

### Q: 10.5.2 线性回归模型--选择“sklearn”包自带的+波士顿房价预测数据集

#### A：把仓库中的csv文件导入与代码同一个文件夹，并进行分析，分析后所得图像如下：
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/boston1.png "")
![](https://github.com/jiyeoniya/2023fall/blob/main/week6/pics/boston2.png "")


