# -*- coding:koi8-r -*-
import vector
import generator_id


class Node:
    """Высокоскростной узел сети

    """

    def __init__(self, x, y, speed=None):
        self.id = generator_id.GeneratorId.get_id()
        self.pos = vector.Vector(x, y)
        if speed is None:
            self.speed = vector.Vector(0, 0)
        elif isinstance(speed, vector.Vector):
            self.speed = speed
        self.range = 700
