from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data  # 我们只取特征空间用于K-means聚类

# K-means聚类
kmeans = KMeans(n_clusters=3, n_init=10)  # 选择3作为聚类数量，因为我们知道有三类鸢尾花
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
