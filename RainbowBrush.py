import pygame, sys
from pygame.locals import *


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
        if self.cs == 0:
            self.g += self.inc
            if self.g == 255:
                self.cs = 1
        elif self.cs == 1:
            self.r -= self.inc
            if self.r == 0:
                self.cs = 2
        elif self.cs == 2:
            self.b += self.inc
            if self.b == 255:
                self.cs = 3
        elif self.cs == 3:
            self.g -= self.inc
            if self.g == 0:
                self.cs = 4
        elif self.cs == 4:
            self.r += self.inc
            if self.r == 255:
                self.cs = 5
        elif self.cs == 5:
            self.b -= self.inc
            if self.b == 0:
                self.cs = 0
        print(str(self.r) + "\t" + str(self.g) + "\t" + str(self.b))
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
