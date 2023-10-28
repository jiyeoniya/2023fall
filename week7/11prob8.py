import numpy as np
from sklearn.datasets import load_iris

# 下载鸢尾花数据集
iris = load_iris()

# 获取特征数据和标签数据
X = iris.data
y = iris.target

# 根据标签划分数据
def split_data_by_label(X, y):
    # 初始化字典用于存储不同类别的数据
    data_by_label = {}
    for label in np.unique(y):
        # 获取当前类别的数据
        data_of_label = X[y == label]
        data_by_label[label] = data_of_label
    return data_by_label

# 计算各类别数据的中心点
def compute_centroids(data_by_label):
    centroids = {}
    for label, data_of_label in data_by_label.items():
        centroid = np.mean(data_of_label, axis=0)
        centroids[label] = centroid
    return centroids

# 计算欧式距离
def compute_euclidean_distance(point, centroid):
    distance = np.linalg.norm(point - centroid)
    return distance

# 将不同类别的数据分组
data_by_label = split_data_by_label(X, y)

# 计算不同类别数据的中心点
centroids = compute_centroids(data_by_label)

# 输出各类别的中心点
for label, centroid in centroids.items():
    print("类别", label+1, "的中心点:", centroid)

# 计算数据点到中心点的欧式距离
for label, data_of_label in data_by_label.items():
    centroid = centroids[label]
    distances = [compute_euclidean_distance(point, centroid) for point in data_of_label]
    print("类别", label+1, "数据点到中心点的欧式距离:", distances)
