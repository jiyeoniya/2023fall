import numpy as np

# 输入的数据矩阵
data = np.array([
    [1, -1, 4],
    [2, 1, 3],
    [1, 3, -1]
])

# 计算协方差矩阵
covariance_matrix = np.cov(data)


def eig_power(A, v0, eps):
    uk = v0
    flag = 1
    val_old = 0
    n = 0
    while flag:
        n = n + 1
        vk = A * uk
        val = vk[np.argmax(np.abs(vk))]
        uk = vk / val
        if (np.abs(val - val_old) < eps):
            flag = 0
        val_old = val
        # print(np.asarray(uk).flatten(), val)
    print('max eigenvalue:', val)
    print('eigenvector:', np.asarray(uk).flatten())
    # print('iteration:', n)
    return val, uk


if __name__ == '__main__':
    A = np.matrix(covariance_matrix, dtype='float')
    v0 = np.matrix([[1], [1], [1]], dtype='float')
    eps = 1e-10
    val, uk = eig_power(A, v0, eps)
