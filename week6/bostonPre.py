import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score

# 从读取的房价数据存储在bos变量中
bos = pd.read_csv('boston.csv')
# 打印bos包含的内容
print(bos.keys())
# 打印data的变量名
print(bos.columns[:-1])
# data的第6列数据为RM
print(bos['RM'].head())
# 选取data中的RM变量
x = bos[['RM']]
# 设定target为y
y = bos['MEDV']
# 定义自定义字体，文件名是系统中文字体
myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.scatter(x, y)
# x轴标签设定文字为中文msyh格式
plt.xlabel(u'住宅平均房间数', fontproperties=myfont)
# y轴标签设定文字为中文msyh格式
plt.ylabel(u'房地产价格', fontproperties=myfont)
# 标题
plt.title(u'RM与MEDV的关系', fontproperties=myfont)
plt.show()

# 把x、y转化为数组形式，便于计算
x = np.array(x.values)
y = np.array(y.values)
# 以25%的数据构建测试样本，剩余作为训练样本
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# 设定回归算法
lr = LinearRegression()
# 使用训练数据进行参数求解
lr.fit(x_train, y_train)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print('求解系数为：', lr.intercept_)
print('求解系数为：', lr.coef_)
# 对测试集的预测
y_hat = lr.predict(x_test)
# 打印前10个预测值
print(y_hat[0:9])
# y_test与y_hat的可视化
# 设置图片尺寸
plt.figure(figsize=(10, 6))
# 创建t变量
t = np.arange(len(x_test))
# 绘制y_test曲线
plt.plot(t, y_test, 'r', linewidth=2, label='y_test')
# 绘制y_hat曲线
plt.plot(t, y_hat, 'g', linewidth=2, label='y_train')
# 设置图例
plt.legend()
plt.show()
# 拟合优度R2的输出方法1
print("r2:", lr.score(x_test, y_test))
# 拟合优度R2的输出方法2
print("r2_score:", r2_score(y_test, y_hat))
# 用Scikit_learn计算MAE
print("MAE:", metrics.mean_absolute_error(y_test, y_hat))
# 用Scikit_learn计算MSE
print("MSE:", metrics.mean_squared_error(y_test, y_hat))
# 用Scikit_learn计算RMSE
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_hat)))
