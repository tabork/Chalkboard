import pygame, sys, random
from pygame.locals import *
from random import randint


class main():

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.drawing = True
                self.last_x, self.last_y = event.pos
                pygame.draw.circle(self.screen, self.color, (self.last_x,self.last_y), 25)
            elif event.type == MOUSEBUTTONUP:
                self.drawing = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.screen.fill((0,0,0))

    def update_color(self):
        if self.faded:
            self.rand_r = randint(0,255)
            self.rand_g = randint(0,255)
            self.rand_b = randint(0,255)
            self.faded = False
        if self.cs == 0:
            if self.r < self.rand_r:
                if (self.rand_r - self.r) < self.inc:
                    self.r = self.rand_r
                else:
                    self.r += self.inc
            elif self.r > self.rand_r:
                if (self.r - self.rand_r) < self.inc:
                    self.r = self.rand_r
                else:
                    self.r -= self.inc
            if self.r == self.rand_r:
                self.cs = 1
        if self.cs == 1:
            if self.g < self.rand_g:
                if (self.rand_g - self.g) < self.inc:
                    self.g = self.rand_g
                else:
                    self.g += self.inc
            elif self.g > self.rand_g:
                if (self.g - self.rand_g) < self.inc:
                    self.g = self.rand_g
                else:
                    self.g -= self.inc
            if self.g == self.rand_g:
                self.cs = 2
        if self.cs == 2:
            if self.b < self.rand_b:
                if (self.rand_b - self.b) < self.inc:
                    self.b = self.rand_b
                else:
                    self.b += self.inc
            elif self.b > self.rand_b:
                if (self.b - self.rand_b) < self.inc:
                    self.b = self.rand_b
                else:
                    self.b -= self.inc
            if self.b == self.rand_b:
                self.cs = 0
        if self.r == self.rand_r and self.g == self.rand_g and self.b == self.rand_b:
            self.faded = True
        self.color = (self.r,self.g,self.b)

    def brush_drag(self):
        end = pygame.mouse.get_pos()
        start = (self.last_x, self.last_y)
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            pygame.draw.circle(self.screen, self.color, (x, y), 25)
            self.last_x = x
            self.last_y = y

    def defineVars(self):
        self.drawing = False
        self.color = (255,0,0)
        self.r = 255
        self.g = 0
        self.b = 0
        self.screen = pygame.display.set_mode((1280,720),0,0)
        self.last_x = self.last_y = 0
        self.cs = 0 #Color section
        self.inc = 5
        self.rand_r = 0
        self.rand_g = 0
        self.rand_b = 0
        self.faded = True

    def __init__(self):
        pygame.init()
        self.defineVars()
        while True:
            self.events()
            if self.drawing:
                self.brush_drag()
                self.update_color()
            pygame.display.flip()


main()
