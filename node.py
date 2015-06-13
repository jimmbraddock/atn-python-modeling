# -*- coding:koi8-r -*-
import vector
import generator_id
import pygame
import mobility


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
        self.mobility = mobility.Mobility(self, bound=vector.Vector(600, 400), mean_direction=[0, 6]
                                                  , mean_pitch=[0.05, 0.05], mean_velocity=[0.0, 0.0],
                                                  normal_direction=[0.2, 0.4],normal_pitch=[0.02, 0.04],
                                                  normal_velocity=[1, 10], alpha=0.85,
                                                  delay=0.5)

    def update(self):
        self.pos.x += self.speed.x/10
        self.pos.y += self.speed.y/10

    def draw(self, screen):
        pygame.draw.circle(screen, (87, 194, 158), (round(self.pos.x), round(self.pos.y)), 10)
        font = pygame.font.SysFont("Inconsolata Bold", 24)
        node_id_txt = font.render(str(self.id), 1, (0, 0, 0))
        text_pos = node_id_txt.get_rect()
        text_pos.center = (self.pos.x, self.pos.y - 15)
        screen.blit(node_id_txt, text_pos)
