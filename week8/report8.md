# WEEK8 H.W. REPORT

## 第13章

## 第一题：

### Q:学习 Python的scikit-learn模块,导 sklearn自带的尾花(ris)数据集并对数据特征可视化。

#### A：导入sklearn.datasets模块，使用load_iris()函数加载Iris数据集，并将数据集中的数据和标签分别存储在X和y变量中。之后将数据集分成训练集和测试集。你可以使用train_test_split()函数来实现，该函数可以将数据集随机分成训练集和测试集两部分。使用matplotlib或者seaborn等可视化库对数据进行可视化。可以绘制散点图、箱线图、热力图等类型的图表来展示数据特征。

## 第二题：

### Q:用sklearn的 train_test_split 方法对尾花(iris)数据集进行随机切分,80%为训练集,20%为测试集。

#### A：导入所需的库和模块，加载鸢尾花数据集，使用train_test_split方法对数据集进行切分。最后将test_size参数设置为0.2，即将20%的数据作为测试集，80%的数据作为训练集。

## 第三题：

### Q:运用KNN分方法对尾花(ris)数据进分别输出训练和测试的准确度。

#### A：导入所需的库和模块，加载鸢尾花数据集并切分为训练集和测试集。之后创建KNN分类器，并使用训练集进行拟合，再对训练集和测试集进行预测，并计算准确度，然后使用predict()方法对训练集和测试集进行预测，然后利用accuracy_score()方法计算准确度。

## 第八题：

### Q:文本挖掘:文本数据集包含 1000 个文档分属于 20 个不同的类别
### (http://www.cs.cmu.edu/afs/cs/project/theo-11/www/naive-bayes.html),尝试通过机器学习算法,挖掘这些文档的特征,将其分成不同的类别。

#### A：只需综合上述所有过程，不再进行赘述。

## 第十四章

## 第二题：

### Q:运用词袋模型对任意文本进行向量化,输出结果向量。

#### A：使用Scikit-learn库中的CountVectorizer类来将文本数据转换为词频矩阵。导入必要的库和模块。定义训练集和测试集的文本数据。创建一个CountVectorizer对象，设置最大特征数为256。使用fit_transform方法将训练集的文本数据转换为词频矩阵X。打印语料库(train_x)、词典(feature_names)、词汇(vocabulary_)和模型参数(params)的信息。打印词频矩阵X和对应的词频结果(X.toarray())。

## 第三题：

### Q:运用sklearn中的tfidf方法,对 sklearn 自带的20newsgroups 数据集进行向量化输出第一个文本的结果向量。

#### A：TF-IDF(Term Frequency-Inverse Document Frequency)是一种常用的文本特征提取方法，它可以通过统计词频和逆文本频率来衡量词语在文档中的重要性。TfidfVectorizer类实现了TF-IDF特征提取的功能。通过调用fit_transform方法，可以将文本数据转换为TF-IDF矩阵。
使用了Scikit-learn库中的fetch_20newsgroups函数获取新闻数据集，并使用TfidfVectorizer将文本数据转换为TF-IDF特征向量。
  
  先导入必要的库和模块，然后使用fetch_20newsgroups函数从Scikit-learn的数据集中获取训练集和测试集的新闻数据。创建一个TfidfVectorizer对象，用于将文本数据转换为TF-IDF特征向量。使用fit_transform方法将训练集的文本数据转换为TF-IDF矩阵train_v。使用transform方法将测试集的文本数据转换为TF-IDF矩阵test_v。最后打印训练集的TF-IDF矩阵train_v和第一个文档的稀疏表示(train_v[1].toarray())。

## 第四题：

### Q:运用朴素贝叶斯的方法对向量化的文本进行分类,输出训练集和测试集的分类准确度。

#### A：MultinomialNB是一种基于朴素贝叶斯算法的分类器，适用于处理离散特征，特别是出现次数计数的情况。在这个例子中，TF-IDF矩阵被用作朴素贝叶斯分类器的输入特征。

导入必要的库和模块。使用fetch_20newsgroups函数从Scikit-learn的数据集中获取完整的新闻数据集。创建一个TfidfVectorizer对象，用于将文本数据转换为TF-IDF特征向量。
使用fit_transform方法将新闻数据集的文本数据转换为TF-IDF矩阵train_v。使用transform方法将测试集的文本数据转换为TF-IDF矩阵test_v。使用fetch_20newsgroups函数分别获取训练集(train)和测试集(test)的新闻数据。
创建一个MultinomialNB对象作为朴素贝叶斯分类器模型。使用fit方法对训练集的TF-IDF矩阵(train_v)和目标值(train.target)进行训练。
使用score方法计算分类器在测试集的TF-IDF矩阵(test_v)和目标值(test.target)上的准确率并输出。

## 第五题：

### Q:任取一段音频,对其进行快速傅里叶变换,可视化傅里叶变换的结果

#### A：使用librosa库进行操作。

## 第八题：

### Q:图数据是一种常见数据结构,Cora 数据集是一个研究中常用的图数据集该图数据8集中的节点分属于不同类别,
### 下载地址:http://www.cs.umdedu/~sen/lbcproi/LBChtml,请尝试选取合适的数据挖掘算法，对该图数据集进行分类

## 第九题：

### Q:高维数据的可视化展示需要通过降维技术来实现请在第8题的基础上使用PCA算法对分类结果进行降维处理,并进行二维展示。

#### A：这两道题合为一题。导入必要的库和模块，然后从PyTorch Geometric中加载Cora数据集，并进行必要的数据转换和归一化操作。定义GCN模型类，其中包括两个GCNConv层和一个log_softmax层。初始化模型，定义损失函数和优化器。在训练模式下，使用Adam优化器进行模型训练，并计算损失。在评估模式下，使用训练好的模型进行预测，并计算测试准确率。使用PCA进行降维处理，将节点特征降低到二维。绘制二维散点图，展示节点特征的分布情况。

