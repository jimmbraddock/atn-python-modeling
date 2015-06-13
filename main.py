# -*- coding:koi8-r -*-
import scheduler
import pygame
import node
import vector
import mobility

BACKGROUND = (235, 235, 235)
WINDOW_RECT = (800, 600)

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
        self.fps = 100
        self.done = False
        self.timer = scheduler.timerSingleton()

    def setup_pygame(self):
        pygame.init()
        pygame.display.set_caption('ATN моделирование')
        screen = pygame.display.set_mode(WINDOW_RECT)
        screen.fill(BACKGROUND)
        return screen

    def setup_scene(self):
        n = node.Node(450, 50)
        n2 = node.Node(550, 100)
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
            print(self.timer.get_time_modeling())
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
