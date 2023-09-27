def conInt(n):
    s = []
    while (n):
        s.append(str(n % 2))
        n = n // 2
    s.reverse()
    return "".join(s)


def conFra(n):
    x = []
    s = []
    while (n):
        n = n * 2
        x.append(str(int(n)))
        n = n - int(n)
    for i in range(0, 10):
        s.append(x[i])
    return "".join(s)


def main():
    n = eval(input("请输入一个十进制小数："))
    a = int(n)
    b = n - a
    print("二进制小数为：", f"{conInt(a)}.{conFra(b)}")


main()
