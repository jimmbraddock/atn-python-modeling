# -*- coding:koi8-r -*-
import pygame

import scheduler
import node
import point

BACKGROUND = (235, 235, 235)
WINDOW_RECT = [800, 600]

params = {}




class Scene:
    def __init__(self, nodes):
        self.mobility  = []
        if isinstance(nodes, list):
            self.nodes = nodes

        else:
            self.nodes = []

    def update(self):
        for n in self.nodes:
            n.update()

    def draw(self, screen):
        screen.fill(BACKGROUND)
        for n in self.nodes:
            n.draw(screen)

class Modeling:
    def __init__(self):
        self.screen = self.setup_pygame()
        self.scene = self.setup_scene()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.timer = scheduler.timerSingleton()

    def setup_pygame(self):
        pygame.init()
        pygame.display.set_caption('ATN моделирование')
        screen = pygame.display.set_mode(WINDOW_RECT)
        screen.fill(BACKGROUND)
        return screen

    def setup_scene(self):
        n = node.Node(450, 250, point.Point(100, 100), bound=[800, 600])
        n2 = node.Node(550, 200, point.Point(80, 80), bound=[800, 600])
        nodes = [n, n2]
        return Scene(nodes)

    def update(self):
        """Updates entire game"""
        while not self.done:
            self.get_user_event()

            # работа протокола
            self.scene.update()
            # отрисовка нодов
            self.scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def get_user_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True


if __name__ == '__main__':
    m = Modeling()
    m.update()
    pygame.quit()
