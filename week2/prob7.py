import math


def cubic_rot(c, max_iter=100, tolerance=1e-10):
    x = c
    for i in range(max_iter):
        last_x = x
        x = ((2*x)**3 + c) / ((3*x)**2)
        if abs(x-last_x) < tolerance:
            print('Cube rot of %f is %f' % (c, x))
            return x


cubic_rot(10)


# 牛顿迭代法求三次方根的迭代公式是:
# xn+1 = (2xn3 + c) / (3xn2)