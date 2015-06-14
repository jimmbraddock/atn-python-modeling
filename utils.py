import numpy

import point


def bezie(points, delta):
    new_points = []
    d = numpy.linspace(0, 1, delta)
    for i in d:
        new_points.append(
            point.Point(
                points[0].x * i ** 2 + points[1].x * 2 * i * (1 - i) + points[
                    2].x * (1 - i) ** 2,
                points[0].y * i ** 2 + points[1].y * 2 * i * (1 - i) + points[
                    2].y * (1 - i) ** 2))
    return new_points
