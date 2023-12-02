from sklearn.datasets import fetch_20newsgroups as news   # 获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer

train = news(subset='train')
test = news(subset='test')

vectorizer = TfidfVectorizer()  # 词频逆文本频率，把一段话转化为向量
train_v = vectorizer.fit_transform(train.data)
test_v = vectorizer.transform(test.data)

print(train_v)
print(train_v[1].toarray())

# # 检查训练数据集中是否存在未包含单词的文档
# for i in range(train_v.shape[0]):
#     if not np.any(train_v[i].toarray()):
#         print(f"第{i+1}个文档中没有包含任何单词")
#
# # 检查测试数据集中是否存在未包含单词的文档
# for i in range(test_v.shape[0]):
#     if not np.any(test_v[i].toarray()):
#         print(f"第{i+1}个文档中没有包含任何单词")

# corpus = [
#     "What is the weather like today",
#     "what is for dinner tonight",
#     "this is question worth pondering",
#     "it is a beautiful day today"
# ]
#
# tfidf_vec1 = TfidfVectorizer()
#
# # 使用 fit_transform() 得到 TF-IDF 矩阵
# tfidf_matrix = tfidf_vec1.fit_transform(corpus)
# print(tfidf_matrix)
#
# # 使用 get_feature_names_out() 得到所有的单词
# print(tfidf_vec.get_feature_names_out())
#
#
# # 得到每个单词对应的 ID
# print(tfidf_vec.vocabulary_)
