def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


a = int(input("请输入一个整数："))
if is_prime(a):
    print(a, "是质数")
else:
    print(a, "不是质数")
b = int(input("请输入一个整数："))
if is_prime(b):
    print(b, "是质数")
else:
    print(b, "不是质数")