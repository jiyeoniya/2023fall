import tensorflow as tf

# 定义 LeNet-5 模型
def lenet5_model(input_shape, num_classes):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(16, kernel_size=(5, 5), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(120, activation='relu'),
        tf.keras.layers.Dense(84, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model

# 创建 LeNet-5 模型实例
input_shape = (32, 32, 1)  # 输入图像尺寸为 32x32，单通道灰度图像
num_classes = 10  # 分类数为 10
model = lenet5_model(input_shape, num_classes)

# 打印模型结构
model.summary()
