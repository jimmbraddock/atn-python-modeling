# -*- coding: koi8-r -*-
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
