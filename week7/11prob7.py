from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 加载鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 2. 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 数据标准化（通常对于Logistic回归是一个好的做法）
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 4. 创建Logistic回归模型
clf = LogisticRegression(max_iter=1000)  # max_iter定义了求解算法的最大迭代次数

# 5. 训练模型
clf.fit(X_train, y_train)

# 6. 进行预测
y_pred = clf.predict(X_test)

# 7. 计算和打印准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
