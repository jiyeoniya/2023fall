import numpy as np
from sklearn import linear_model

# 定义方程f(z)
def f(z):
    return 9 + 8 * z

# 从[0, 30]区间均匀采样30个点作为原始采样点
z = np.linspace(0, 10, 30)

# 生成服从标准正态分布的噪声数据
noise = np.random.normal(0, 1, size=30)
y = f(z) + np.random.rand(30)

# 将噪声数据加到原始采样点上得到新的样本点
samples = f(z) + noise

reg = linear_model.LinearRegression()
z = z.reshape(-1, 1)
reg.fit(z, y)



# 打印新样本点的值

print(reg.coef_)
