import numpy as np
import matplotlib.pyplot as plt

# 从正态分布中抽样出100个样本，参数mean=0, std=1
samples = np.random.normal(loc=0, scale=1, size=100)

# 使用matplotlib来为样本绘图
plt.hist(samples, bins=30, density=True, alpha=0.5, color='blue')

# 绘制出理论的正态分布曲线
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-(x - 0) ** 2 / 2) / np.sqrt(2 * np.pi)
plt.plot(x, p, 'k', linewidth=2)

plt.title('Normal Distribution Sampling')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()