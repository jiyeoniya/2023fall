import random



def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[i] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[minIndex]:
                minIndex = j  # i 不是最小数时，将  和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr




def select_sort(array):
    for i in range(len(array)):
        x = i  # min index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
                array[i], array[x] = array[x], array[i]
    return array


size = int(input("请输入要生成的数组的长度："))
n = int(input("请输入要生成的数组的个数："))
# 创建空字典用于存储随机数组
lists = {}
# 生成随机数组并存储到字典中
for i in range(1, n + 1):
    lists['list' + str(i)] = [random.randint(1, 100) for _ in range(size)]
for i in range(1, n + 1):
    print("第%d个数组：" % i, lists['list' + str(i)])
    print(bubbleSort(lists['list' + str(i)]))
    print(selectionSort(lists['list' + str(i)]))
    print(insertionSort(lists['list' + str(i)]))
    print(select_sort(lists['list' + str(i)]))


