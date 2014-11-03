import pygame, sys, random
from pygame.locals import *
from random import randint

class main:

    def getRandstart(self):
        return randint(5,1275),randint(5,715)

    def update_color(self):
        self.r = randint(0,255)
        self.g = randint(0,255)
        self.b = randint(0,255)
        self.color = (self.r,self.g,self.b)

    def drawLines(self):
        s = self.getRandstart()
        #s = self.points[0][0]
        lp = s
        for p in self.points:
            if p[0] != s:
                pygame.draw.line(self.screen,p[1],s,p[0],1)
                self.update_color()
                pygame.draw.line(self.screen,p[1],lp,p[0],1)
            lp = p[0]

    def getRandpoint(self):
        x = randint(5,1275)
        y = randint(5,715)
        self.points.append(((x,y),self.color))

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    self.started = True
                    self.points = []
                    self.screen.fill((0,0,0))

    def defineVars(self):
        self.points = []
        self.color = (255,255,255)
        self.r = 255
        self.g = 255
        self.b = 255
        self.started = False
        self.screen = pygame.display.set_mode((1280,720),0,0)

    def __init__(self):
        pygame.init()
        self.defineVars()
        self.getRandpoint()

        while True:
            self.events()
            if self.started:
                self.getRandpoint()
                self.update_color()
                self.drawLines()
            pygame.display.flip()

main()
            
