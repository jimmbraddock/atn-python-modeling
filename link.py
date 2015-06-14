# -*- coding:koi8-r -*-



# class Link:
#     def __init__(self):
#         pass

import numpy
import matplotlib.pyplot as plt


def bezie(points, delta):
    x = []
    y = []
    d = numpy.linspace(0, 1, delta)
    for i in d:
        x.append(
            points[0][0] * i ** 2 + points[1][0] * 2 * i * (1 - i) + points[2][
                0] * (1 - i) ** 2)
        y.append(
            points[0][1] * i ** 2 + points[1][1] * 2 * i * (1 - i) + points[2][
                1] * (1 - i) ** 2)
    return x, y


xr, yr = bezie([[3, 3], [8, 3], [5, 4]], 20)
print(xr)
print(yr)

plt.plot(xr, yr)
plt.show()
