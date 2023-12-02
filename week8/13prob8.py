import urllib.request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 下载数据集
url = "http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

# 解析文档和标签，具体方法取决于数据集的格式
documents = []  # 存储文档
labels = []  # 存储对应的标签

# 在这里，你需要解析网页数据并将文档和标签提取出来，根据实际数据集的格式来处理

# 创建TF-IDF特征提取器
tfidf_vectorizer = TfidfVectorizer(max_features=1000)  # 可根据需要调整特征数量

# 将文档转换为TF-IDF特征矩阵
X = tfidf_vectorizer.fit_transform(documents)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# 创建朴素贝叶斯分类器
nb_classifier = MultinomialNB()

# 训练分类器
nb_classifier.fit(X_train, y_train)

# 进行预测
y_pred = nb_classifier.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print("准确性:", accuracy)