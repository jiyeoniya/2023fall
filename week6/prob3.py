import numpy as np

# 定义矩阵
A = np.array([[2, 1], [4, 5]])

# 使用eig函数计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

print("特征值: ", eigenvalues)
print("特征向量: ", eigenvectors)