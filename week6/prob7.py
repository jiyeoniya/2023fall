def Statistic(file):
    # 打开文件
    f = open(file, 'r', encoding='utf-8')  # 这里我们指定了编码为utf-8
    # 创建一个空字典
    dictionary = {}
    for line in f.readlines():
        if len(line) > 10:
            # print(type(line))
            # 则除文木中的标点符号
            mark = [',', '.', ':', ';', '\'s', '?', '(', ')', '。', '，', '、', '（', '）']
            for m in mark:
                line = line.replace(m, '')
                # print(line)
            lineattr = line.strip().split(" ")
            for char in lineattr:
                if char not in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1
                    # print (dictionary)
    a = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    # 按照字典 value 值大小进行排序
    # print (a1)
    return a


'''  
输出文木中前n个最常出现的单词  
file: 文木的路径  
n: 输入出单词的个数  
'''

a = Statistic("test.txt")
for i in range(len(a)):
    print(a[i])