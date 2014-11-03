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
                pygame.draw.circle(self.draws, self.color, (self.last_x,self.last_y), 25)
            elif event.type == MOUSEBUTTONUP:
                self.drawing = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.screen.fill((0,0,0))

    def fade(self):
        self.a -= self.inc
        if self.a == 0:
            self.faded = True
        self.color = (self.r,self.g,self.b,self.a)

    def unfade(self, ii):
        if ii == 0:
            self.update_color()
        self.a += 5
        print(str(self.a))
        if self.a == 255:
            self.unfaded = True
        self.color = (self.r,self.g,self.b,self.a)

    def update_color(self):
        self.r = randint(0,255)
        self.g = randint(0,255)
        self.b = randint(0,255)
        self.color = (self.r,self.g,self.b,self.a)

    def brush_drag(self):
        end = pygame.mouse.get_pos()
        start = (self.last_x, self.last_y)
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            pygame.draw.circle(self.draws, self.color, (x, y), 25)
            self.last_x = x
            self.last_y = y

    def defineVars(self):
        self.drawing = False
        self.color = (255,0,0,255)
        self.r = 255
        self.g = 0
        self.b = 0
        self.a = 255
        self.screen = pygame.display.set_mode((1280,720),0,0)
        self.last_x = self.last_y = 0
        self.cs = 0 #Color section
        self.inc = 5
        self.draws = pygame.Surface((1280,720),0,32).convert_alpha()
        self.faded = False
        self.unfaded = False

    def __init__(self):
        pygame.init()
        self.defineVars()
        i = 0
        ii = 0
        self.draws.fill(self.color)
        while True:
            self.screen.fill((0,0,0))
            self.events()
            if i >= 20:
                if self.faded:
                    self.unfade(ii)
                    ii += 1
                    if self.unfaded:
                        self.faded = False
                        self.unfaded = False
                        i = 0
                        ii = 0
                else:
                    self.fade()
                self.draws.fill(self.color)
            if self.drawing:
                self.brush_drag()
                self.update_color()
            self.screen.blit(self.draws,(0,0))
            pygame.display.flip()
            i += 1

main()
