import pygame, sys, os
from pygame.locals import *

class ColorDialog:

    def typer(self):
        self.screen.blit(pygame.image.load("gui/typing.png"),(0,0))
        self.screen.blit(self.font.render(self.text, 1, (0,0,0)), self.typePos)
    
    def showDialog(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200,300),0,0)
        self.screen.fill((255,255,255))
        self.font = pygame.font.SysFont("Times New Roman", 12, False, False)
        self.redTyping = False
        self.greenTyping = False
        self.blueTyping = False
        self.r = 0
        self.g = 0
        self.b = 0
        self.text = ""
        
        self.screen.blit(self.font.render("red: ", 1, (0,0,0)),(10,10))
        pygame.draw.rect(self.screen, (0,0,0), Rect(50,10,50,30))
        pygame.draw.rect(self.screen, (255,255,255), Rect(52,12,46,26))
        self.screen.blit(self.font.render("0", 1, (0,0,0)),(53,13))
        self.screen.blit(self.font.render("green: ", 1, (0,0,0)),(10,75))
        pygame.draw.rect(self.screen, (0,0,0), Rect(50,75,50,30))
        pygame.draw.rect(self.screen, (255,255,255), Rect(52,77,46,26))
        self.screen.blit(self.font.render("0", 1, (0,0,0)),(53,78))
        self.screen.blit(self.font.render("blue: ", 1, (0,0,0)),(10,140))
        pygame.draw.rect(self.screen, (0,0,0), Rect(50,140,50,30))
        pygame.draw.rect(self.screen, (255,255,255), Rect(52,142,46,26))
        self.screen.blit(self.font.render("0", 1, (0,0,0)),(53,143))
        pygame.draw.rect(self.screen, (0,0,0), Rect(50,250,50,30))
        pygame.draw.rect(self.screen, (255,255,255), Rect(52,252,46,26))
        self.screen.blit(self.font.render("Okay", 1, (0,0,0)),(53,253))

        
        while True:
            pygame.draw.rect(self.screen, (self.r,self.g,self.b), Rect(10,180,100,20))
            if self.redTyping or self.greenTyping or self.blueTyping:
                self.typer()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if len(self.text) < 3:
                            if event.key == K_0 or event.key == K_KP0:
                                self.text += '0'
                            if event.key == K_1 or event.key == K_KP1:
                                self.text += '1'
                            if event.key == K_2 or event.key == K_KP2:
                                self.text += '2'
                            if event.key == K_3 or event.key == K_KP3:
                                self.text += '3'
                            if event.key == K_4 or event.key == K_KP4:
                                self.text += '4'
                            if event.key == K_5 or event.key == K_KP5:
                                self.text += '5'
                            if event.key == K_6 or event.key == K_KP6:
                                self.text += '6'
                            if event.key == K_7 or event.key == K_KP7:
                                self.text += '7'
                            if event.key == K_8 or event.key == K_KP8:
                                self.text += '8'
                            if event.key == K_9 or event.key == K_KP9:
                                self.text += '9'
                        if event.key == K_BACKSPACE:
                            c = list(self.text)
                            self.text = ""
                            i = 0
                            while i < len(c)-1:
                                self.text += c[i]
                                i += 1
                        if event.key == K_RETURN or event.key == K_KP_ENTER:
                            if self.redTyping:
                                self.r = int(self.text)
                                if self.r > 255:
                                    self.r = 255
                                    self.text = "255"
                                    self.typer()
                            elif self.greenTyping:
                                self.g = int(self.text)
                                if self.g > 255:
                                    self.g = 255
                                    self.text = "255"
                                    self.typer()
                            elif self.blueTyping:
                                self.b = int(self.text)
                                if self.b > 255:
                                    self.b = 255
                                    self.text = "255"
                                    self.typer()
                            self.text = ""
                            self.redTyping = self.greenTyping = self.blueTyping =  False
                            os.remove("gui/typing.png")
                            
            else:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if x in range(50,100) and y in range(10,40):
                            self.redTyping = True
                            self.typePos = (53,13)
                            pygame.draw.rect(self.screen, (255,255,255), Rect(52,12,46,26))
                            pygame.image.save(self.screen, "gui/typing.png")
                        elif x in range(50,100) and y in range(75,105):
                            self.greenTyping = True
                            self.typePos = (53,78)
                            pygame.draw.rect(self.screen, (255,255,255), Rect(52,77,46,26))
                            pygame.image.save(self.screen, "gui/typing.png")
                        elif x in range(50,100) and y in range(140,180):
                            self.blueTyping = True
                            self.typePos = (53,143)
                            pygame.draw.rect(self.screen, (255,255,255), Rect(52,142,46,26))
                            pygame.image.save(self.screen, "gui/typing.png")
                        elif x in range(50,100) and y in range(250,280):
                            return (self.r,self.g,self.b)

            pygame.display.flip()

