from sklearn.naive_bayes import MultinomialNB  # 朴素贝叶斯
from sklearn.datasets import fetch_20newsgroups   # 获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer


newsgroups = fetch_20newsgroups()
tfidf_vec = TfidfVectorizer()
train_v = tfidf_vec.fit_transform(newsgroups)
test_v = tfidf_vec.transform(newsgroups)

train = fetch_20newsgroups(subset='train')
test = fetch_20newsgroups(subset='test')

model = MultinomialNB()
model.fit(train_v, train.target)
print("准确率为:", model.score(test_v, test.target))
