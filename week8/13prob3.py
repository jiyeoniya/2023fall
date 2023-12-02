import numpy as np
# Puplot 提供了一套和MATLAB类似的绘图API，使得Matplotlib的机制更像MATLAB。
# 我们只需要调用Pyplot模块所提供的函数就可以快速绘图并设置图表的各个细节
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier # 导入sklearn类库及KNN模型
from sklearn.datasets import load_iris

# 加载鸢尾花数据集，并分割成样本特征X和样本标签Y
iris = load_iris()
X = iris.data[:, :2]
Y = iris.target

# 绘制背景颜色和散点颜色映射表
cmap_light = ListedColormap(['#FFB6C1', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#228B22', '#0000FF'])
# 构建KNN模型
clf = KNeighborsClassifier(n_neighbors=10, weights='uniform')
# 调用模型的fit函数进行训练
clf.fit(X,Y)

# 画出决策边界
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# 绘制预测结果图
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())  # xlim：当前图形X轴的范围
plt.ylim(yy.min(), yy.max())
plt.title('3_Class(k=10,weights=uniform)')
plt.show()
