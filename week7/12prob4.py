import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# 下载鸢尾花数据集
iris = load_iris()

# 获取特征数据和标签数据
X = iris.data
y = iris.target.reshape(-1, 1)

# 对标签进行one-hot编码
encoder = OneHotEncoder(categories='auto')
y = encoder.fit_transform(y).toarray()

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建神经网络模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(X_train, y_train, epochs=100, batch_size=16, verbose=1)

# 在测试集上评估模型
loss, accuracy = model.evaluate(X_test, y_test)
print("测试集上的损失:", loss)
print("测试集上的准确率:", accuracy)
