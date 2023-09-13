def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input(""))
print(factorial(n))