# -*- coding:koi8-r -*-
import math

import scheduler


class Mobility:
    """ Модель движения узлов сети пытается описать правила движения объектов с
        высокой скоростью. Т.е. траектории не могут меняться резко, а плавно происходит
        разворот.

    """

    def __init__(self, node, **kwargs):
        self.rnd_speed = kwargs['rnd_speed']
        self.delay = kwargs['delay']
        self.rotation = 0.0
        self.node = node
        self.walk(self.delay)

    def walk(self, delay):
        self.rotation += 50 * delay
        self.node.pos.x += 10 * math.cos(-math.radians(self.rotation)) * delay
        self.node.pos.y += 10 * math.sin(-math.radians(self.rotation)) * delay
        timer = scheduler.timerSingleton()
        timer.scheduler(delay, self.walk)
        # if k[pyglet.window.key.LEFT]:
        #     ship.rotation -= 50*dt
        #     ship.x += 100 * math.cos(-math.radians(ship.rotation)) * delay
        #     ship.y += 100 * math.sin(-math.radians(ship.rotation)) * delay
        # rotation = math.radians(ship.rotation)
        # rotation_x = math.cos(-rotation)
        # rotation_y = math.sin(-rotation)
        #
        # if k[pyglet.window.key.UP]:
        #     ship.x += 200 * rotation_x * dt
        #     ship.y += 200 * rotation_y * dt
