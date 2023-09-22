import random
import math


def calculate_pi_mc(num_points):
    points_inside_circle = 0
    points_inside_square = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1
        points_inside_square += 1

    pi = 4 * (points_inside_circle / points_inside_square)
    return pi

num_points = 1000000
pi_mc = calculate_pi_mc(num_points)
print("蒙特卡洛方法计算π的近似值：", pi_mc)


def calculate_pi_leibniz(num_terms):
    pi = 0
    sign = 1

    for i in range(num_terms):
        term = sign / (2*i + 1)
        pi += term
        sign *= -1

    pi *= 4
    return pi

num_terms = 1000000
pi_leibniz = calculate_pi_leibniz(num_terms)
print("Leibniz公式计算π的近似值：", pi_leibniz)


def calculate_pi_bbp(num_terms):
    pi = 0

    for k in range(num_terms):
        term = (1/16**k) * ((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6)))
        pi += term

    return pi


num_terms = 100
pi_bbp = calculate_pi_bbp(num_terms)
print("马青公式计算π的近似值：", pi_bbp)

