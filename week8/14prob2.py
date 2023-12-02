from sklearn.feature_extraction.text import CountVectorizer
# 语料库
train_x = ['build fails due publication-tests.xml build target', 'due to sb']
test_x = ['build one to ']
# 将文本中的词语转换为词频矩阵  选择前256个词 相当于词向量的维度是256维的
cv_ = CountVectorizer(max_features=256)
# 计算个词语出现的次数  此类方法一般先fit拟合，再transform转换
X = cv_.fit_transform(train_x)
# 输出语料库
print('corpus', train_x)
# 输出词典
print('feature_names', cv_.get_feature_names_out())
# 输出词汇
print('vocabulary_', cv_.vocabulary_)
# 输出模型参数
print('params', cv_.get_params(deep=True))
# 输出词频
print(X)
# 查看词频结果
print(X.toarray())
