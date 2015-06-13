# -*- coding:koi8-r -*-
import math
import vector
import random
import scheduler


class Mobility:
    """ Модель движения узлов сети пытается описать правила движения объектов с
        высокой скоростью. Т.е. траектории не могут меняться резко, а плавно происходит
        разворот.

    """

    def __init__(self, node, **kwargs):
        self.rnd_mean_velocity = kwargs['mean_velocity']
        self.rnd_mean_direction = kwargs['mean_direction']
        self.rnd_mean_pitch = kwargs['mean_pitch']
        self.delay = kwargs['delay']
        self.alpha = kwargs['alpha']
        self.rnd_normal_velocity = kwargs['normal_velocity']
        self.rnd_normal_pitch = kwargs['normal_pitch']
        self.rnd_normal_direction = kwargs['normal_direction']
        self.bound = kwargs['bound']
        self.node = node
        self.mean_velocity = random.uniform(self.rnd_mean_velocity[0], self.rnd_mean_velocity[1])
        if self.mean_velocity == 0.0:
            self.mean_direction = random.uniform(self.rnd_mean_direction[0], self.rnd_mean_direction[1])
            self.mean_pitch = random.uniform(self.rnd_mean_pitch[0], self.rnd_mean_pitch[1])
            cosD = math.cos(self.mean_direction)
            cosP = math.cos(self.mean_pitch)
            sinD = math.sin(self.mean_direction)
            #sinP = math.sin(self.mean_pitch)
            self.velocity = self.mean_velocity
            self.direction = self.mean_direction
            self.pitch = self.mean_pitch
            self.node.speed = vector.Vector (self.velocity*cosD*cosP, self.velocity*sinD*cosP)
            self.start()

    def start(self):
        rv = random.uniform(self.rnd_normal_velocity[0], self.rnd_normal_velocity[1])
        rd = random.uniform(self.rnd_mean_direction[0], self.rnd_mean_direction[1])
        rp = random.uniform(self.rnd_mean_pitch[0], self.rnd_mean_pitch[1])

        one_minus_alpha = 1 - self.alpha
        sqrt_alpha = math.sqrt (1 - self.alpha*self.alpha)
        self.velocity  = self.alpha * self.velocity  + one_minus_alpha * self.mean_velocity  + sqrt_alpha * rv
        self.direction = self.alpha * self.direction + one_minus_alpha * self.mean_direction + sqrt_alpha * rd
        self.pitch     = self.alpha * self.pitch     + one_minus_alpha * self.mean_pitch     + sqrt_alpha * rp

        cosDir = math.cos (self.direction)
        cosPit = math.cos (self.pitch)
        sinDir = math.sin (self.direction)
        vx = self.velocity * cosDir * cosPit
        vy = self.velocity * sinDir * cosPit
        self.node.speed = vector.Vector (vx, vy)

        self.walk (self.delay)

    def walk(self, delay):
     position = self.node.pos
     speed = self.node.speed
     nextPosition = position
     nextPosition.x += speed.x * delay
     nextPosition.y += speed.y * delay
     timer = scheduler.timerSingleton()
     if (delay < 0.0):
         delay = 1.0

     if self.bound.x > nextPosition.x and self.bound.y > nextPosition.y:

        timer.scheduler (delay, self.start)
     else:
         if nextPosition.x > self.bound.x or nextPosition.x < self.bound.x:
             speed.x = -speed.x
             self.mean_direction = math.pi - self.mean_direction

         if nextPosition.y > self.bound.y or nextPosition.y < self.bound.y:
             speed.y = -speed.y
             self.mean_direction = -self.mean_direction

         self.direction = self.mean_direction
         self.pitch = self.mean_pitch
         self.node.speed  = speed
         timer.scheduler(delay, self.start)
