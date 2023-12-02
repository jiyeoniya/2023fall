from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 下载鸢尾花数据集
iris = load_iris()
print(iris)
# 获取特征数据和标签数据
X = iris.data
y = iris.target

# 将数据随机打乱，并按照2:8的比例划分测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 输出划分结果
print("训练集大小:", X_train.shape, y_train.shape)
print(X_train)
print("测试集大小:", X_test.shape, y_test.shape)
print(X_test)