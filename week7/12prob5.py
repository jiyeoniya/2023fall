import cv2

# 加载图片
image = cv2.imread('imagetest.jpg')

# 将图片转化为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 指定输出图像的大小
target_size = (400, 300)
resized_image = cv2.resize(image, target_size)

# 显示灰度图像
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)

# 显示放缩后的图像
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

# 关闭所有窗口
cv2.destroyAllWindows()
