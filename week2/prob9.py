import random
import math


def func(x):
  return x**2 + 4*x*math.sin(x)


def monte_carlo_integration(func, a, b, N):
  s = 0
  for i in range(N):
    x = random.uniform(a, b)
    s += func(x)
  area = (b-a)*s/N
  return area


print(monte_carlo_integration(func, 2, 3, 1000000))
