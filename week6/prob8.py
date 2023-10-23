import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
plt.rcParams['font.sans-serif']=['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus']=False

# 导入波士顿房价数据集
from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)

# 建立线性回归模型
regr = linear_model.LinearRegression()
# 用前450条数据作为训练集
regr.fit(X[0:450, :], y[0:450])
a, b = regr.coef_, regr.intercept_
# 后56条数据作为
test = X[450:506, :]
# 绘图
x = np.arange(56)
plt.scatter(x, y[450:], s=10, label="实际数据点",)
plt.plot(x, regr.predict(test), c='r', label="拟合数据")
plt.xlabel("样本")
plt.ylabel("MEDV")
plt.grid()
plt.legend()
plt.show()
