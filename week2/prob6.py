c = 2


def Square_root_3(g):
    i = 0
    while (abs(g*g-c) > 0.00000000001):
        g = (g + c / g) / 2
        i = i + 1
        print("%d:%.13f" % (i, g))


Square_root_3(c)
Square_root_3(c / 2)
Square_root_3(c / 3)