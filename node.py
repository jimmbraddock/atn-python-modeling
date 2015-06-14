# -*- coding:koi8-r -*-
import random

import pygame

import point
import generator_id
import utils


class Node:
    """Высокоскростной узел сети

    """

    def __init__(self, x, y, speed, bound=None):
        self.id = generator_id.GeneratorId.get_id()
        self.pos = point.Point(x, y)
        self.bound = bound
        self.speed = speed
        self.range = 700
        self.path = [self.pos]
        self.bezie_center_index = 1

    def update(self):
        self.pos.x = int(round(self.path[-1].x))
        self.pos.y = int(round(self.path[-1].y))
        if len(self.path) == self.bezie_center_index:
            self.change_position()
        else:
            self.path = self.path[:-1]

    def change_position(self):
        next_point = point.Point(random.randint(0, self.bound[0]),
                                 random.randint(0, self.bound[1]))
        points = [self.path[self.bezie_center_index - 1], self.path[0],
                  next_point]
        speed_vector_len = (self.speed.x ** 2 + self.speed.y ** 2) ** 0.5
        self.path = utils.bezie(points, speed_vector_len)
        self.bezie_center_index = int(len(self.path) / 2)


    def draw(self, screen):
        pygame.draw.circle(screen, (87, 194, 158), (self.pos.x, self.pos.y), 10)
        path = []
        for p in self.path:
            path.append([p.x, p.y])
        pygame.draw.polygon(screen, (0, 0, 255), path, 2)
        font = pygame.font.SysFont("Inconsolata Bold", 24)
        node_id_txt = font.render(str(self.id), 1, (0, 0, 0))
        text_pos = node_id_txt.get_rect()
        text_pos.center = (self.pos.x, self.pos.y - 15)
        screen.blit(node_id_txt, text_pos)
