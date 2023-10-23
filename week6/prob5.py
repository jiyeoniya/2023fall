import numpy as np

# 输入的数据矩阵
data = np.array([
    [1, -1, 4],
    [2, 1, 3],
    [1, 3, -1]
])

# 计算协方差矩阵
covariance_matrix = np.cov(data)

# 打印结果
print(covariance_matrix)