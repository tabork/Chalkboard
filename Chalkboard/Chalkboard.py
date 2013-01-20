#
#Chalkboard 2.2
#
#   Created and Maintained by the Kamakwazee Open Source Team
#           -Tabor Kvasnicka   ]----Currently, only person
#
#Expected Features:
#   Custom Cursors -- Will be finished in about a weak
#                       Currently an eraser cover problem                                ]
#                       Line cursor color change not complete                            ]---------Will be completed in 2.3 along with additional unknown features
#                       Circle and ellipses treated as rectangles in cursor color change ]
#
#Import dependencies
import pygame, sys, Tkinter, math, os, tkFileDialog, tkMessageBox, save_as, open_file, display, wx
from pygame.locals import *
from Tkinter import *
class main:
    #Declare mouse cursors
    def setupCursors(self):
        #Cross 8x8
        xx = ("   XX   ",
              "   XX   ",
              "   XX   ",
              "XXX  XXX",
              "XXX  XXX",
              "   XX   ",
              "   XX   ",
              "   XX   ")
        self.xxcb = pygame.cursors.compile(xx, white='X', black='.',xor='0')
        self.xxcw = pygame.cursors.compile(xx, white='.', black='X', xor='0')
        #---NOTE--- For the following, the first size is the size displayed,
        #---NOTE--- and the second size is the size of string.
        #Square 4x4 8x8
        xs4 = ("        ",
               "        ",
               "  XXXX  ",
               "  X  X  ",
               "  X  X  ",
               "  XXXX  ",
               "        ",
               "        ")
        self.xs4cb = pygame.cursors.compile(xs4, white='X', black='.', xor='0')
        self.xs4cw = pygame.cursors.compile(xs4, white='.', black='X', xor='0')
        #Square 6x6 8x8
        xs6 = ("        ",
               " XXXXXX ",
               " X    X ",
               " X    X ",
               " X    X ",
               " X    X ",
               " XXXXXX ",
               "        ")
        self.xs6cb = pygame.cursors.compile(xs6, white='X', black='.', xor='0')
        self.xs6cw = pygame.cursors.compile(xs6, white='.', black='X', xor='0')
        #Square 8x8 8x8
        xs8 = ("XXXXXXXX",
               "X      X",
               "X      X",
               "X      X",
               "X      X",
               "X      X",
               "X      X",
               "XXXXXXXX")
        self.xs8cb = pygame.cursors.compile(xs8, white='X', black='.', xor='0')
        self.xs8cw = pygame.cursors.compile(xs8, white='.', black='X', xor='0')
        #Square 10x10 16x16
        xs10 = ("                ",
                "                ",
                "                ",
                "   XXXXXXXXXX   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   XXXXXXXXXX   ",
                "                ",
                "                ",
                "                ")
        self.xs10cb = pygame.cursors.compile(xs10, white='X', black='.', xor='0')
        self.xs10cw = pygame.cursors.compile(xs10, white='.', black='X', xor='0')
        #Square 12x12 16x16
        xs12 = ("                ",
                "                ",
                "  XXXXXXXXXXXX  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  XXXXXXXXXXXX  ",
                "                ",
                "                ")
        self.xs12cb = pygame.cursors.compile(xs12, white='X', black='.', xor='0')
        self.xs12cw = pygame.cursors.compile(xs12, white='.', black='X', xor='0')
        #Square 14x14 16x16
        xs14 = ("                ",
                " XXXXXXXXXXXXXX ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " XXXXXXXXXXXXXX ",
                "                ")
        self.xs14cb = pygame.cursors.compile(xs14, white='X', black='.', xor='0')
        self.xs14cw = pygame.cursors.compile(xs14, white='.', black='X', xor='0')
        #Square 16x16 16x16
        xs16 = ("XXXXXXXXXXXXXXXX",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "XXXXXXXXXXXXXXXX")
        self.xs16cb = pygame.cursors.compile(xs16, white='X', black='.', xor='0')
        self.xs16cw = pygame.cursors.compile(xs16, white='.', black='X', xor='0')
        #Square 18x18 24x24
        xs18 = ("                        ",
                "                        ",
                "                        ",
                "   XXXXXXXXXXXXXXXXXX   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   XXXXXXXXXXXXXXXXXX   ",
                "                        ",
                "                        ",
                "                        ")
        self.xs18cb = pygame.cursors.compile(xs18, white='X', black='.', xor='0')
        self.xs18cw = pygame.cursors.compile(xs18, white='.', black='X', xor='0')
        #Square 20x20 24x24
        xs20 = ("                        ",
                "                        ",
                "  XXXXXXXXXXXXXXXXXXXX  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  XXXXXXXXXXXXXXXXXXXX  ",
                "                        ",
                "                        ")
        self.xs20cb = pygame.cursors.compile(xs20, white='X', black='.', xor='0')
        self.xs20cw = pygame.cursors.compile(xs20, white='.', black='X', xor='0')
        #Square 22x22 24x24
        xs22 = ("                        ",
                " XXXXXXXXXXXXXXXXXXXXXX ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " XXXXXXXXXXXXXXXXXXXXXX ",
                "                        ")
        self.xs22cb = pygame.cursors.compile(xs22, white='X', black='.', xor='0')
        self.xs22cw = pygame.cursors.compile(xs22, white='.', black='X', xor='0')
        #Square 24x24 24x24
        xs24 = ("XXXXXXXXXXXXXXXXXXXXXXXX",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "XXXXXXXXXXXXXXXXXXXXXXXX")
        self.xs24cb = pygame.cursors.compile(xs24, white='X', black='.', xor='0')
        self.xs24cw = pygame.cursors.compile(xs24, white='.', black='X', xor='0')
        #Square 26x26 32x32
        xs26 = ("                                ",
                "                                ",
                "                                ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "                                ",
                "                                ",
                "                                ")
        self.xs26cb = pygame.cursors.compile(xs26, white='X', black='.', xor='0')
        self.xs26cw = pygame.cursors.compile(xs26, white='.', black='X', xor='0')
        #Square 28x28 32x32
        xs28 = ("                                ",
                "                                ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "                                ",
                "                                ")
        self.xs28cb = pygame.cursors.compile(xs28, white='X', black='.', xor='0')
        self.xs28cw = pygame.cursors.compile(xs28, white='.', black='X', xor='0')
        #Square 50x50 56x56
        xs50 = ("                                                        ",
                "                                                        ",
                "                                                        ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   X                                                X   ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "                                                        ",
                "                                                        ",
                "                                                        ")
        self.xs50cb = pygame.cursors.compile(xs50, white='X', black='.', xor='0')
        self.xs50cw = pygame.cursors.compile(xs50, white='.', black='X', xor='0')
        #Circle 4x4 8x8
        xc4 = ("        ",
               "        ",
               "   XX   ",
               "  X  X  ",
               "  X  X  ",
               "   XX   ",
               "        ",
               "        ")
        self.xc4cb = pygame.cursors.compile(xc4, white='X', black='.', xor='0')
        self.xc4cw = pygame.cursors.compile(xc4, white='.', black='X', xor='0')
        #Circle 6x6 8x8
        xc6 = ("        ",
               "  XXXX  ",
               " X    X ",
               " X    X ",
               " X    X ",
               " X    X ",
               "  XXXX  ",
               "        ")
        self.xc6cb = pygame.cursors.compile(xc6, white='X', black='.', xor='0')
        self.xc6cw = pygame.cursors.compile(xc6, white='.', black='X', xor='0')
        #Circle 8x8 8x8
        xc8 = ("  XXXX  ",
               " X    X ",
               "X      X",
               "X      X",
               "X      X",
               "X      X",
               " X    X ",
               "  XXXX  ")
        self.xc8cb = pygame.cursors.compile(xc8, white='X', black='.', xor='0')
        self.xc8cw = pygame.cursors.compile(xc8, white='.', black='X', xor='0')
        #Circle 10x10 16x16
        xc10 = ("                ",
                "                ",
                "                ",
                "      XXXX      ",
                "    XX    XX    ",
                "    X      X    ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "   X        X   ",
                "    X      X    ",
                "    XX    XX    ",
                "      XXXX      ",
                "                ",
                "                ",
                "                ")
        self.xc10cb = pygame.cursors.compile(xc10, white='X', black='.', xor='0')
        self.xc10cw = pygame.cursors.compile(xc10, white='.', black='X', xor='0')
        #Circle 12x12 16x16
        xc12 = ("                ",
                "                ",
                "      XXXX      ",
                "    XX    XX    ",
                "   X        X   ",
                "   X        X   ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "  X          X  ",
                "   X        X   ",
                "   X        X   ",
                "    XX    XX    ",
                "      XXXX      ",
                "                ",
                "                ")
        self.xc12cb = pygame.cursors.compile(xc12, white='X', black='.', xor='0')
        self.xc12cw = pygame.cursors.compile(xc12, white='.', black='X', xor='0')
        #Circle 14x14 16x16
        xc14 = ("                ",
                "     XXXXXX     ",
                "    X      X    ",
                "   X        X   ",
                "  X          X  ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                " X            X ",
                "  X          X  ",
                "   X        X   ",
                "    X      X    ",
                "     XXXXXX     ",
                "                ")
        self.xc14cb = pygame.cursors.compile(xc14, white='X', black='.', xor='0')
        self.xc14cw = pygame.cursors.compile(xc14, white='.', black='X', xor='0')
        #Circle 16x16 16x16
        xc16 = ("     XXXXXX     ",
                "   XX      XX   ",
                "  X          X  ",
                " X            X ",
                " X            X ",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                "X              X",
                " X            X ",
                " X            X ",
                "  X          X  ",
                "   XX      XX   ",
                "     XXXXXX     ")
        self.xc16cb = pygame.cursors.compile(xc16, white='X', black='.', xor='0')
        self.xc16cw = pygame.cursors.compile(xc16, white='.', black='X', xor='0')
        #Circle 18x18 24x24
        xc18 = ("                        ",
                "                        ",
                "                        ",
                "         XXXXXX         ",
                "       XX      XX       ",
                "      X          X      ",
                "     X            X     ",
                "    X              X    ",
                "    X              X    ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "   X                X   ",
                "    X              X    ",
                "    X              X    ",
                "     X            X     ",
                "      X          X      ",
                "       XX      XX       ",
                "         XXXXXX         ",
                "                        ",
                "                        ",
                "                        ")
        self.xc18cb = pygame.cursors.compile(xc18, white='X', black='.', xor='0')
        self.xc18cw = pygame.cursors.compile(xc18, white='.', black='X', xor='0')
        #Circle 20x20 24x24
        xc20 = ("                        ",
                "                        ",
                "         XXXXXX         ",
                "       XX      XX       ",
                "     XX          XX     ",
                "    X              X    ",
                "    X              X    ",
                "   X                X   ",
                "   X                X   ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "   X                X   ",
                "   X                X   ",
                "    X              X    ",
                "    X              X    ",
                "     XX          XX     ",
                "       XX      XX       ",
                "         XXXXXX         ",
                "                        ",
                "                        ")
        self.xc20cb = pygame.cursors.compile(xc20, white='X', black='.', xor='0')
        self.xc20cw = pygame.cursors.compile(xc20, white='.', black='X', xor='0')
        #Circle 22x22 24x24
        xc22 = ("                        ",
                "         XXXXXX         ",
                "      XXX      XXX      ",
                "     X            X     ",
                "    X              X    ",
                "   X                X   ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                "  X                  X  ",
                "  X                  X  ",
                "  X                  X  ",
                "   X                X   ",
                "    X              X    ",
                "     X            X     ",
                "      XXX      XXX      ",
                "         XXXXXX         ",
                "                        ")
        self.xc22cb = pygame.cursors.compile(xc22, white='X', black='.', xor='0')
        self.xc22cw = pygame.cursors.compile(xc22, white='.', black='X', xor='0')
        #Circle 24x24 24x24
        xc24 = ("         XXXXXX         ",
                "      XXX      XXX      ",
                "     X            X     ",
                "    X              X    ",
                "   X                X   ",
                "  X                  X  ",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                "X                      X",
                " X                    X ",
                " X                    X ",
                " X                    X ",
                "  X                  X  ",
                "   X                X   ",
                "    X              X    ",
                "     X            X     ",
                "      XXX      XXX      ",
                "         XXXXXX         ")
        self.xc24cb = pygame.cursors.compile(xc24, white='X', black='.', xor='0')
        self.xc24cw = pygame.cursors.compile(xc24, white='.', black='X', xor='0')
        self.canContinue = True  #Allow for continuing
    #Open file
    def open_it(self):
        self.fileClicked = False #First make the file menu go away
        if self.saved == False:  #If it is already saved,
            yn = display.disp().display() #ask if user wants to save
            if yn: #If yes,
                self.save() #run self.save method
        self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0)) #Place the temporary menu_screen.png file on screen.
        pygame.display.flip() #Update screen
        fn = open_file.open_f().openfile() #Display open dialog and store file in fn
        if fn != None: #If fn equals something,
            self.opened = True #set self.opened to True
            self.opened_file = fn #Make the self.opened_file equal to the file in fn
            self.savedname = fn  #Also make fn the saved name
            loaded = pygame.image.load(fn) #Load the image user opened
            pygame.transform.scale(loaded,(self.width-30,self.height-60)) #Scale the image to fit in the editing screen
            self.screen.blit(loaded,(30,60)) #Add to screen
            self.saved = True #Make it marked as saved
            self.title = "Chalkboard  |  " + fn #Change the title variable to apply to opened file
            pygame.display.set_caption(self.title) #Apply changed title
            pygame.display.flip() #Update screen
    #Save file
    def save(self):
        self.fileClicked = False #Make file menu go away
        self.screen.blit(pygame.image.load("gui/menu_screen.png"),(0,0)) #Add the temporary menu_screen.png file to screen
        self.saving = True #Set saving to True to stop gui from adding
        if self.saved == False: #If it isn't already saved
            if self.savedname == "Untitled.png": #If the current saved name is Untitled.png
                self.save_as() #Go to self.save_as. This is necessary so that the user can pick a name.
            else: #Otherwise
                pygame.image.save(self.screen, "tmp.png") #Save a temporary image
                self.screen = pygame.display.set_mode((self.width-30,self.height-60),0,0) #Change screen size to size without gui
                pygame.display.flip() #Update
                self.screen.blit(pygame.image.load("tmp.png"),(-30,-60)) #Add the temporary image to screen to where gui isn't displayed.
                pygame.display.flip() #Update
                pygame.image.save(self.screen,self.savedname) #Save as selected name
                self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0) #Change screen back to normal
                self.screen.blit(pygame.image.load("tmp.png"),(0,0)) #Add the temporary image back to screen
                self.gui(self.width,self.height) #Update gui
                self.saved = True #Set self.saved to True
                self.title = "Chalkboard  |  " + self.savedname #Change the title variable to apply to saved name
                pygame.display.set_caption(self.title) #Apply changed title
                os.remove("tmp.png") #Delete temporary image
        self.saving = False #Set saving to False so gui can proceed to update
    #Save as dialog
    def save_as(self):
        self.fileClicked = False #Make the file menu go away
        self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0)) #Add temporary menu_screen.png image to screen
        self.saving = True #Set self.saving to True so gui won't update
        fn = save_as.save().saveas() #Display save as dialog
        if fn != None: #If the file equals something
            pygame.image.save(self.screen, "tmp.png") #Save a temporary image
            self.screen = pygame.display.set_mode((self.width-30,self.height-60),0,0) #Change screen size to size without gui
            pygame.display.flip() #Update screen
            self.screen.blit(pygame.image.load("tmp.png"),(-30,-60)) #Add temporary image without gui
            pygame.display.flip() #Update screen
            pygame.image.save(self.screen,fn) #save image as selected file name
            self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0) #Restore screen
            self.screen.blit(pygame.image.load("tmp.png"),(0,0)) #Add temporary image to screen
            self.gui(self.width,self.height) #Update gui
            self.saved = True #Set self.saved to True
            self.title = "Chalkboard  |  " + fn #Change the title variable to apply to saved name
            pygame.display.set_caption(self.title) #Apply changed title
            os.remove("tmp.png") #Delete temporary image
            self.savedname = fn #Set saved name to selected file name
        self.saving = False #Set saving to True so gui can proceed to update
    #Declare all the global variables used in the application-----Most self explanatory.
    def declareVar(self, setup_true_false):
        if setup_true_false == False: #If pygame and the screen aren't initialized
            self.saved = True
            self.saving = False
            self.opened = False
            self.opened_file = "Untitled.png"
            self.title = "Chalkboard  |  Untitled.png"
            self.savedname = "Untitled.png"
            self.icon = "gui/icon.gif"
            #Colors
            self.white=(255,255,255)
            self.black=(0, 0, 0)
            self.red=(255, 0, 0)
            self.blue = (0, 0, 255)
            self.green = (0, 100, 0)
            self.yellow = (255, 255, 0)
            self.lime = (0, 255, 0)
            self.purple = (204, 0, 255)
            self.teal = (0, 255, 255)
            self.orange = (255, 102, 0)
            self.fill = self.black
            self.color = self.white
            self.mode = "square" #Brush/eraser mode
            self.points=[]
            self.s = 1 #Size
            self.c = 1 #Point incrementation
            root = Tk() #Tkinter root menu
            self.window_w = root.winfo_screenwidth() #Screen width
            self.window_h = root.winfo_screenheight() #Screen height
            if (float(self.window_w)/float(self.window_h)) == (16/9): #If the width/height ration is 16/9 (widescreen), set size to 1280,720
                self.width = 1280
                self.height = 720
            else: #Otherwise set it to 1080,720
                self.width = 1080
                self.height = 720
            self.dragging = False #Mouse dragging
            self.placed = False #Shape placed
            #Menu/tool selection clicked/selected
            self.brushClicked = False
            self.eraserClicked = False
            self.rectClicked = False
            self.lineClicked = False
            self.ellipseClicked = False
            self.arrowClicked = False
            self.fillArrowClicked = False
            self.fileClicked = False
            self.whiteSelected = False
            self.blackSelected = False
            self.redSelected = False
            self.orangeSelected = False
            self.limeSelected = False
            self.greenSelected = False
            self.blueSelected = False
            self.tealSelected = False
            self.purpleSelected = False
            self.yellowSelected = False
            self.blackFillSelected = False
            self.whiteFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.yellowFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            #slider x locations
            self.slider_x = 287
            self.slider_line_x = 287
            self.slider_eraser_x = 80
            self.sh_moving = False #Slider handle moving
            #Whether or not the square or circle is brush/eraser mode is selected
            self.squareClicked = False
            self.circleClicked = False
            self.squareBrushClicked = False
            self.circleBrushClicked = False
            #Values involving self.redraw() and shape creation
            self.history = []
            self.hist_points = []
            self.hist_color = []
            self.hist_size = []
            self.ell_type = 0
            self.rc = 0
            self.rw = 0
            self.rh = 0
            self.point1 = 0
            self.point2 = 0
            self.point3 = 0
            self.point4 = 0
            self.rect_w = 0
            self.rect_h = 0
            self.rect_c = self.black
            self.line_s = 0
            self.line_c = (0,0,0)
            self.cx = 810
        else: #Otherwise
            self.main_icon = pygame.image.load(self.icon).convert() #Load icon
            pygame.display.set_icon(self.main_icon) #Apply icon
            pygame.display.set_caption("Chalkboard", "Chalkboard") #Set caption
    #Update gui
    def gui(self, width, height):
        if self.saving == False:
            pygame.display.flip()
            #Gui background
            pygame.draw.rect(self.screen, (206,206,206), Rect(0,0,width,30))
            pygame.draw.rect(self.screen, (233,236,157), Rect(0,30,30,height))
            pygame.draw.rect(self.screen, (233,236,157), Rect(0,30,width,30))
            self.screen.blit(pygame.image.load("gui/File.png").convert_alpha(), (5,5)) #File button
            if self.brushClicked == False: #If the brush tool isn't selected,
                self.screen.blit(pygame.image.load("gui/brush.png").convert_alpha(), (3,60)) #add the nonselected brush picture
            else: #Otherwise
                self.screen.blit(pygame.image.load("gui/brush_clicked.png").convert_alpha(), (3,60)) #Add the clicked brush picture
#----------The rest are self explanatory if you look at names
                self.screen.blit(pygame.image.load("gui/color_txt.png").convert_alpha(), (33,34))
                if self.whiteSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (80, 34))
                elif self.blackSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (80,34))
                elif self.redSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (80,34))
                elif self.orangeSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (80,34))
                elif self.limeSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (80,34))
                elif self.greenSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (80,34))
                elif self.blueSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (80,34))
                elif self.tealSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (80,34))
                elif self.purpleSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (80,34))
                elif self.yellowSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (80,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (213,34))
                self.screen.blit(pygame.image.load("gui/size_txt.png").convert_alpha(), (240, 35))
                self.screen.blit(pygame.image.load("gui/slider.png").convert_alpha(), (290,38))
                self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_x, 44))
                if self.squareBrushClicked:
                    self.screen.blit(pygame.image.load("gui/square_clicked.png").convert_alpha(), (350, 33))
                else:
                    self.screen.blit(pygame.image.load("gui/square.png").convert_alpha(), (350,33))
                if self.circleBrushClicked:
                    self.screen.blit(pygame.image.load("gui/circle_clicked.png").convert_alpha(), (380, 33))
                else:
                    self.screen.blit(pygame.image.load("gui/circle.png").convert_alpha(), (380, 33))
            if self.eraserClicked == False:
                self.screen.blit(pygame.image.load("gui/eraser.png").convert_alpha(), (3, 90))
            else:
                self.screen.blit(pygame.image.load("gui/eraser_clicked.png").convert_alpha(), (3, 90))
                self.screen.blit(pygame.image.load("gui/size_txt.png").convert_alpha(), (33, 35))
                self.screen.blit(pygame.image.load("gui/slider.png").convert_alpha(), (83,38))
                self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_eraser_x, 44))
                if self.squareClicked:
                    self.screen.blit(pygame.image.load("gui/square_clicked.png").convert_alpha(), (138, 33))
                else:
                    self.screen.blit(pygame.image.load("gui/square.png").convert_alpha(), (138,33))
                if self.circleClicked:
                    self.screen.blit(pygame.image.load("gui/circle_clicked.png").convert_alpha(), (168, 33))
                else:
                    self.screen.blit(pygame.image.load("gui/circle.png").convert_alpha(), (168, 33))
            if self.rectClicked == False:
                self.screen.blit(pygame.image.load("gui/rectangle.png").convert_alpha(), (3,120))
            else:
                self.screen.blit(pygame.image.load("gui/rectangle_clicked.png").convert_alpha(), (3,120))
                self.screen.blit(pygame.image.load("gui/color_txt.png").convert_alpha(), (33,34))
                if self.whiteSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (80, 34))
                elif self.blackSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (80,34))
                elif self.redSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (80,34))
                elif self.orangeSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (80,34))
                elif self.limeSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (80,34))
                elif self.greenSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (80,34))
                elif self.blueSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (80,34))
                elif self.tealSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (80,34))
                elif self.purpleSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (80,34))
                elif self.yellowSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (80,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (213,34))
            if self.ellipseClicked == False:
                self.screen.blit(pygame.image.load("gui/ellipse.png").convert_alpha(), (3,150))
            else:
                self.screen.blit(pygame.image.load("gui/ellipse_clicked.png").convert_alpha(), (3,150))
                self.screen.blit(pygame.image.load("gui/color_txt.png").convert_alpha(), (33,34))
                if self.whiteSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (80, 34))
                elif self.blackSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (80,34))
                elif self.orangeSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (80,34))
                elif self.redSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (80,34))
                elif self.limeSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (80,34))
                elif self.greenSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (80,34))
                elif self.blueSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (80,34))
                elif self.tealSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (80,34))
                elif self.purpleSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (80,34))
                elif self.yellowSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (80,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (213,34))
            if self.lineClicked == False:
                self.screen.blit(pygame.image.load("gui/line.png").convert_alpha(), (3, 180))
            else:
                self.screen.blit(pygame.image.load("gui/line_clicked.png").convert_alpha(), (3,180))
                self.screen.blit(pygame.image.load("gui/color_txt.png").convert_alpha(), (33,34))
                if self.whiteSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (80, 34))
                elif self.blackSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (80,34))
                elif self.orangeSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (80,34))
                elif self.redSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (80,34))
                elif self.limeSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (80,34))
                elif self.greenSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (80,34))
                elif self.blueSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (80,34))
                elif self.tealSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (80,34))
                elif self.purpleSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (80,34))
                elif self.yellowSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (80,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (213,34))
                self.screen.blit(pygame.image.load("gui/size_txt.png").convert_alpha(), (240, 35))
                self.screen.blit(pygame.image.load("gui/slider.png").convert_alpha(), (290,38))
                self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_line_x, 44))
            self.screen.blit(pygame.image.load("gui/fill_txt.png").convert_alpha(), (450, 33))
            if self.blackFillSelected:
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (540,34))
            elif self.whiteFillSelected:
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (540,34))
            elif self.redFillSelected:
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (540,34))
            elif self.limeFillSelected:
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (540,34))
            elif self.greenFillSelected:
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (540,34))
            elif self.orangeFillSelected:
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (540,34))
            elif self.blueFillSelected:
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (540,34))
            elif self.yellowFillSelected:
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (540,34))
            elif self.tealFillSelected:
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (540,34))
            elif self.purpleFillSelected:
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (540,34))
            self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (673, 34))
            self.screen.blit(pygame.image.load("gui/clear.png").convert_alpha(), (self.cx,34))
            if self.arrowClicked:
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (80,54))
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (80,74))
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (80,94))
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (80,114))
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (80,134))
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (80,154))
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (80,174))
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (80,194))
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (80,214))
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (80, 234))
            if self.fillArrowClicked:
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (540,54))
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (540,74))
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (540,94))
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (540,114))
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (540,134))
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (540,154))
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (540,174))
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (540,194))
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (540,214))
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (540, 234))
                pygame.display.set_caption(self.title)
            if self.fileClicked:
                self.screen.blit(pygame.image.load("gui/save_as.png").convert_alpha(), (0,25))
                self.screen.blit(pygame.image.load("gui/save.png").convert_alpha(), (0,45))
                self.screen.blit(pygame.image.load("gui/open.png").convert_alpha(), (0, 65))
        pygame.display.flip()
    #Get the value of the tool property sheet
    def getTool(self, t):
        if t == "brush":
            self.brushClicked = True
        elif t == "eraser":
            self.eraserClicked = True
        elif t == "rect":
            self.rectClicked = True
        elif t == "ellipse":
            self.ellipseClicked = True
        elif t == "line":
            self.lineClicked = True
    #Determine which color and fill color menu items are clicked
    def setClicked(self, bg):
        if bg: #if background is true
            if self.fill == self.black:
                self.blackFillSelected = True
            elif self.fill == self.white:
                self.whiteFillSelected = True
            elif self.fill == self.red:
                self.redFillSelected = True
            elif self.fill == self.blue:
                self.blueFillSelected = True
            elif self.fill == self.green:
                self.greenFillSelected = True
            elif self.fill == self.yellow:
                self.yellowFillSelected = True
            elif self.fill == self.lime:
                self.limeFillSelected = True
            elif self.fill == self.purple:
                self.purpleFillSelected = True
            elif self.fill == self.teal:
                self.tealFillSelected = True
            elif self.fill == self.orange:
                self.orangeFillSelected = True
        else: #otherwise
            if self.color == self.black:
                self.blackSelected = True
            elif self.color == self.white:
                self.whiteSelected = True
            elif self.color == self.red:
                self.redSelected = True
            elif self.color == self.blue:
                self.blueSelected = True
            elif self.color == self.green:
                self.greenSelected = True
            elif self.color == self.yellow:
                self.yellowSelected = True
            elif self.color == self.lime:
                self.limeSelected = True
            elif self.color == self.purple:
                self.purpleSelected = True
            elif self.color == self.teal:
                self.tealSelected = True
            elif self.color == self.orange:
                self.orangeSelected = True
    #Get what the color property value is
    def getColor(self, c):
        if c == "black":
            return self.black
        elif c == "white":
            return self.white
        elif c == "red":
            return self.red
        elif c == "blue":
            return self.blue
        elif c == "green":
            return self.green
        elif c == "yellow":
            return self.yellow
        elif c == "lime":
            return self.lime
        elif c == "purple":
            return self.purple
        elif c == "teal":
            return self.teal
        elif c == "orange":
            return self.orange
    #Get property values. Self explanatory
    def getProperties(self):
        if os.path.exists("properties/bgColor.txt"):
            bgcf = open("properties/bgColor.txt", "r")
            bgc = bgcf.read()
        else:
            bgcf = open("properties/bgColor.txt", "w")
            bgcf.write("black")
            bgc = "black"
        bgcf.close()
        self.fill = self.getColor(bgc)
        self.setClicked(True)
        if os.path.exists("properties/fgColor.txt"):
            fgcf = open("properties/fgColor.txt", "r")
            fgc = fgcf.read()
        else:
            fgcf = open("properties/fgColor.txt", "w")
            fgcf.write("white")
            fgc = "white"
        fgcf.close()
        self.color = self.getColor(fgc)
        self.setClicked(False)
        if os.path.exists("properties/shape.txt"):
            sf = open("properties/shape.txt", "r")
            s = sf.read()
        else:
            sf = open("properties/shape.txt", "w")
            sf.write("square")
            s = "square"
        sf.close()
        self.mode = s
        self.mode = s
        if s == "square":
            self.squareClicked = True
            self.squareBrushClicked = True
        else:
            self.circleClicked = True
            self.circleBrushClicked = True
        if os.path.exists("properties/size.txt"):
            szf = open("properties/size.txt", "r")
            sz = szf.read()
        else:
            szf = open("properties/size.txt", "w")
            szf.write("1")
            sz = "1"
        szf.close()
        self.s = int(sz)
        self.s = int(sz)
        self.s = int(sz)
        self.slider_x = 286 + self.s
        self.slider_eraser_x = 79 + self.s
        self.slider_line_x = 286 + self.s
        if os.path.exists("properties/tool.txt"):
            tf = open("properties/tool.txt", "r")
            t = tf.read()
        else:
            tf = open("properties/tool.txt", "w")
            tf.write("brush")
            t = "brush"
        tf.close()
        self.getTool(t)
        self.screen.fill(self.fill)
        pygame.display.flip()
    #Setup application
    def setup(self):
        pygame.init() #Initialize pygame
        self.canContinue = False #declare the self.canContinue variable
        self.setupCursors() #Setup all the mouse cursors
        self.declareVar(False) #Declare variables before screen
        self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0) #Setup screen
        self.declareVar(True) #Declare variables after screen
        self.getProperties() #Get the property values
        self.gui(self.width, self.height) #Add gui
    #Redraw after fillscreen
    def redraw(self, h, p, c, s):
        #Incrementation values
        i = 0
        i_p = 0
        i_c = 0
        i_s = 0
        if self.opened: #If a file is opened
            self.screen.blit(pygame.image.load(self.opened_file),(30,60)) #Add file
        while i < len(self.history) and i_p < len(self.hist_points) and i_c < len(self.hist_color) and i_s < len(self.hist_size): #While the incr. values below length of arrays
            #Smaller array names
            h = self.history
            p = self.hist_points
            c = self.hist_color
            s = self.hist_size
            #Detect history value
            if h[i] == "brush_square":
                if s[i_s] == 1:
                    pygame.draw.circle(self.screen, c[i_c], (p[i_p], p[i_p+1]), s[i_s]/2)
                else:
                    pygame.draw.rect(self.screen, c[i_c], Rect(p[i_p], p[i_p+1], s[i_s], s[i_s]))
                i_p += 2
                i_s += 1
            elif h[i] == "brush_circle":
                pygame.draw.circle(self.screen, c[i_c], (p[i_p], p[i_p+1]), s[i_s]/2)
                i_p += 2
                i_s += 1
            elif h[i] == "eraser_square":
                if s[i_s] == 1:
                    pygame.draw.circle(self.screen, self.fill, (p[i_p], p[i_p+1]), s[i_s]/2)
                else:
                    pygame.draw.rect(self.screen, self.fill, Rect(p[i_p], p[i_p+1], s[i_s], s[i_s]))
                i_p += 2
                i_s += 1
            elif h[i] == "eraser_circle":
                pygame.draw.circle(self.screen, self.fill, (p[i_p], p[i_p+1]), s[i_s]/2)
                i_p += 2
                i_s += 1
            elif h[i] == "rect":
                pygame.draw.rect(self.screen,c[i_c], Rect(p[i_p], p[i_p+1], s[i_s], s[i_s+1]))
                i_p += 2
                i_s += 2
            elif h[i] == "ellipse":
                pygame.draw.ellipse(self.screen, c[i_c], Rect(p[i_p],p[i_p+1], s[i_s], s[i_s+1]))
                i_p += 2
                i_s += 2
            elif h[i] == "line":
                pygame.draw.line(self.screen, c[i_c], (p[i_p], p[i_p+1]), (p[i_p+2], p[i_p+3]), s[i_s])
                i_p += 4
                i_s += 1
            i_c += 1
            i += 1
    #Fill screen
    def fillScreen(self, yco):
        #Detects which color selected then fills screen with the color.
        if yco in range(54, 74):
            self.whiteFillSelected = True
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.white
            self.screen.fill(self.fill)
        elif yco in range(75,94):
            self.whiteFillSelected = False
            self.blackFillSelected = True
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.black
            self.screen.fill(self.fill)
        elif yco in range(95,114):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = True
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.red
            self.screen.fill(self.fill)
        elif yco in range(115,134):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = True
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.orange
            self.screen.fill(self.fill)
        elif yco in range(135,154):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = True
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.lime
            self.screen.fill(self.fill)
        elif yco in range(155, 174):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = True
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.green
            self.screen.fill(self.fill)
        elif yco in range(175,194):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = True
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.blue
            self.screen.fill(self.fill)
        elif yco in range(195,214):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = True
            self.purpleFillSelected = False
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.teal
            self.screen.fill(self.fill)
        elif yco in range(215, 234):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = True
            self.yellowFillSelected = False
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.purple
            self.screen.fill(self.fill)
        elif yco in range(235, 254):
            self.whiteFillSelected = False
            self.blackFillSelected = False
            self.redFillSelected = False
            self.orangeFillSelected = False
            self.limeFillSelected = False
            self.greenFillSelected = False
            self.blueFillSelected = False
            self.tealFillSelected = False
            self.purpleFillSelected = False
            self.yellowFillSelected = True
            self.fillArrowClicked = False
            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
            self.fill = self.yellow
            self.screen.fill(self.fill)
        if self.saved: #If saved
            self.saved = False #Set saved to false
            self.title = self.title + "*" #Add * to title to symbolize edit
            pygame.display.set_caption(self.title)
        self.redraw(self.history, self.hist_points, self.hist_color, self.hist_size) #Redraw
    #Events
    def events(self):
        if self.arrowClicked: #If the color arrow is clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit Program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If the mouse is down
                    xco, yco = pygame.mouse.get_pos() #Get mouse position
                    if (xco not in range(80, 180) or yco not in range(54, 254)) or (xco in range(213,230) and yco in range(34,52)):
                        self.arrowClicked = False
                        self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                        if xco in range(0,136) and yco in range(0,25):
                            self.fileClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                        elif xco in range(673,690) and yco in range(34,52):
                            self.fillArrowClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                    elif xco in range(80,180): #if within the color choices
                        #Change the color of the brush to selected color
                        if yco in range(54, 74):
                            self.whiteSelected = True
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.white
                            self.changeBrush()
                        elif yco in range(75,94):
                            self.whiteSelected = False
                            self.blackSelected = True
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.black
                            self.changeBrush()
                        elif yco in range(95,114):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = True
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.red
                            self.changeBrush()
                        elif yco in range(115,134):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = True
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.orange
                            self.changeBrush()
                        elif yco in range(135,154):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = True
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.lime
                            self.changeBrush()
                        elif yco in range(155, 174):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = True
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.green
                            self.changeBrush()
                        elif yco in range(175,194):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = True
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.blue
                            self.changeBrush()
                        elif yco in range(195,214):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = True
                            self.purpleSelected = False
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.teal
                            self.changeBrush()
                        elif yco in range(215, 234):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = True
                            self.yellowSelected = False
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.purple
                            self.changeBrush()
                        elif yco in range(235, 254):
                            self.whiteSelected = False
                            self.blackSelected = False
                            self.redSelected = False
                            self.orangeSelected = False
                            self.limeSelected = False
                            self.greenSelected = False
                            self.blueSelected = False
                            self.tealSelected = False
                            self.purpleSelected = False
                            self.yellowSelected = True
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            self.color = self.yellow
                            self.changeBrush()
        elif self.fillArrowClicked: #If the fill arrow is clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If the mouse is down
                    xco, yco = pygame.mouse.get_pos() #Get mouse position
                    if (xco not in range(540, 640) or yco not in range(54, 254)) or (xco in range(673,690) and yco in range(34,52)):
                        self.fillArrowClicked = False
                        self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                        if xco in range(0,136) or yco in range(0,25):
                            self.fileClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                        elif xco in range(213,230) and yco in range(34,52):
                            self.arrowClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                    elif xco in range(540,640): #If within fill color options
                        self.fillScreen(yco) #Fill screen
        elif self.fileClicked: #If file menu button clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If mouse is down
                    xco, yco = pygame.mouse.get_pos() #Get mouse position
                    if (xco not in range(0, 136) or yco not in range(0, 85)) or (xco in range(0,136) and yco in range(0,25)):
                        self.fileClicked = False
                        self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                        if xco in range(213,230) and yco in range(34,52):
                            self.arrowClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                        elif xco in range(673,690) and yco in range(34,52):
                            self.fillArrowClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                    if xco in range(0,136) and yco in range(25,45): #Save as
                        self.save_as()
                    elif xco in range(0,136) and yco in range(45,65): #Save
                        self.save()
                    elif xco in range(0,136) and yco in range(65,85): #Open
                        self.open_it()
        else: #Normal events
            for event in pygame.event.get():
                if event.type == QUIT: #If X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If mouse is down
                    xco, yco = event.pos #Get the event position
                    if xco in range(30,self.width) and yco in range(60,self.height): #If in canvas
                        if self.saved: #If saved
                            self.saved = False #saved set to false
                            self.title = self.title + "*" #Add * to title to symbolize edit
                            pygame.display.set_caption(self.title)
                    if xco in range(0, 50) and yco in range(0, 30): #File clicked
                        self.fileClicked = True
                        pygame.image.save(self.screen, "gui/menu_screen.png") #Save temporary image
                    #Drawing events
                    elif self.rectClicked and xco not in range(0,30) and yco not in range(0,60):
                        self.points.append(event.pos)
                        self.dragging = True
                    elif self.ellipseClicked and xco not in range(0,30) and yco not in range(0,60):
                        self.points.append(event.pos)
                        self.dragging = True
                    elif self.brushClicked and xco not in range(0,30) and yco not in range(0,60):
                        self.dragging = True
                    elif self.eraserClicked and xco not in range(0,30) and yco not in range(0,60):
                        self.dragging = True
                    elif self.lineClicked and xco not in range(0,30) and yco not in range(0,60):
                        self.points.append(event.pos)
                        self.dragging = True
                    #Tool changing events
                    elif xco in range(3, 30) and yco in range(120, 150): #Rectangle
                        self.rectClicked = True
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(60, 87): #Brush
                        self.rectClicked = False
                        self.brushClicked = True
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(90, 117): #Eraser
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = True
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(150, 175): #Ellipse
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = True
                    elif xco in range(3,30) and yco in range(180, 206): #Line
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = True
                        self.ellipseClicked = False
                    elif xco in range(213,230) and yco in range(34,52): #Color arrow clicked
                        if self.eraserClicked == False: #If eraser isn't selected
                            pygame.image.save(self.screen, "gui/menu_screen.png")
                            self.arrowClicked = True
                    elif xco in range(673,690) and yco in range(34,52): #Fill arrow clicked
                        pygame.image.save(self.screen, "gui/menu_screen.png")
                        self.fillArrowClicked = True
                    #Clear
                    elif xco in range(self.cx,self.cx+50) and yco in range(34,54):
                        if self.saved == False:
                            yn = display.disp().display() #Display the save question
                            if yn: #If yes, save
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                                self.save()
                        #Reset redraw and shape creation variables
                        self.history = []
                        self.hist_points = []
                        self.hist_color = []
                        self.hist_size = []
                        self.ell_type = 0
                        self.point1 = 0
                        self.point2 = 0
                        self.point3 = 0
                        self.point4 = 0
                        self.rect_w = 0
                        self.rect_h = 0
                        self.rect_c = self.black
                        self.line_s = 0
                        self.line_c = (0,0,0)
                        #Reset screen, title, opened, saved, and placed variables
                        self.screen.fill(self.fill)
                        self.opened = False
                        self.saved = True
                        self.title = "Chalkboard  |  Untitled.png"
                        self.placed = False
                        pygame.display.set_caption(self.title)
                        pygame.display.flip()
                    elif self.eraserClicked: #if the eraser is selected
                        if xco in range(self.slider_eraser_x, self.slider_eraser_x + 9) and yco in range(44, 51): #slider handle clicked
                            self.sh_moving = True
                        elif xco in range(138, 164) and yco in range(33,59): #Square mode selected, change eraser
                            self.squareClicked = True
                            self.squareBrushClicked = True
                            self.circleClicked = False
                            self.circleBrushClicked = False
                            self.mode = "square"
                            self.changeEraser()
                        elif xco in range(168, 194) and yco in range(33,59): #Circle mode selected, change eraser
                            self.circleClicked = True
                            self.circleBrushClicked = True
                            self.squareClicked = False
                            self.squareBrushClicked = False
                            self.mode = "circle"
                            self.changeEraser()
                    elif self.brushClicked: #If brush selected
                        if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
                            self.sh_moving = True
                        elif xco in range(350, 376) and yco in range(33,59): #Square mode selected, change brush
                            self.squareBrushClicked = True
                            self.squareClicked = True
                            self.circleBrushClicked = False
                            self.circleClicked = False
                            self.mode = "square"
                            self.changeBrush()
                        elif xco in range(380,406) and yco in range(33,59): #Circle mode selected, change brush
                            self.circleBrushClicked = True
                            self.circleClicked = True
                            self.squareBrushClicked = False
                            self.squareClicked = False
                            self.mode = "circle"
                            self.changeBrush()
                    elif self.lineClicked: #If line selected
                        if xco in range(self.slider_line_x, self.slider_line_x + 9) and yco in range(44, 51): #slider handle clicked
                            self.sh_moving = True   
                elif event.type == MOUSEBUTTONUP: #If mouse up
                    #Reset dragging and moving
                    self.dragging = False
                    self.sh_moving = False
                    self.placed = True
                    self.points = [] #reset points[] used in drawing
                    self.c = 1
                    pygame.image.save(self.screen, "gui/screen.png")
                    self.scr = pygame.image.load("gui/screen.png").convert_alpha()
                    #Write to history corresponding to what tool selected
                    if self.rectClicked:
                        self.history.append("rect")
                        self.hist_points.append(self.point1)
                        self.hist_points.append(self.point2)
                        self.hist_size.append(self.rect_w)
                        self.hist_size.append(self.rect_h)
                        self.hist_color.append(self.rect_c)
                    elif self.ellipseClicked:
                        if self.ell_type != 2:
                            self.history.append("ellipse")
                            self.hist_points.append(self.point1)
                            self.hist_points.append(self.point2)
                            self.hist_size.append(self.rect_w)
                            self.hist_size.append(self.rect_h)
                            self.hist_color.append(self.rect_c)
                        else:
                            self.history.append("line")
                            self.hist_points.append(self.point1)
                            self.hist_points.append(self.point2)
                            self.hist_points.append(self.point3)
                            self.hist_points.append(self.point4)
                            self.hist_size.append(4)
                            self.hist_color.append(self.line_c)
                    elif self.lineClicked:
                        self.history.append("line")
                        self.hist_points.append(self.point1)
                        self.hist_points.append(self.point2)
                        self.hist_points.append(self.point3)
                        self.hist_points.append(self.point4)
                        self.hist_size.append(self.line_s)
                        self.hist_color.append(self.line_c)
                    #Reset draw points
                    self.point1 = 0
                    self.point2 = 0
                    self.point3 = 0
                    self.point4 = 0
                    self.rect_w = 0
                    self.rect_h = 0
                    self.line_s = 0
                elif event.type == VIDEORESIZE: #If screen resized
                    pygame.image.save(self.screen,"gui/fs_screen.png") #Save temporary image
                    self.screen = pygame.display.set_mode(event.size, RESIZABLE, 0) #Resize screen to the size changed by user
                    pygame.display.flip() #Update screen
                    self.width, self.height = event.size #set the width and height to the event size for the gui
                    if self.width < self.window_w/2: #If the width is less than half of the total screen size
                        #Set it to half of the default screen size so the clear button isn't compressed
                        self.cx = self.window_w/2-70
                        self.cx = int(self.cx)
                        self.width = self.window_w/2;
                        self.screen = pygame.display.set_mode((self.width,self.height), RESIZABLE, 0)
                    elif self.width < 1080: #If the width is below 1080
                        self.cx = self.width*.90 #Place the clear x at 90% of the current window
                        self.cx = int(math.floor(self.cx)) #Round down
                    else:
                        #Otherwise set it to 75% and round down
                        self.cx = self.width*0.75
                        self.cx = math.floor(self.cx)
                        self.cx = int(self.cx)
                    if self.height < 185: #If the height is less than 185, set it to 185
                        self.height = 185
                        self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0)
                    #Reset gui and add temp. pic to screen
                    self.gui(self.width, self.height)
                    self.screen.fill(self.fill)
                    self.screen.blit(pygame.image.load("gui/fs_screen.png").convert_alpha(),(0,0))
    def rect_drag(self): #Rectangle dragging
        if self.placed == True:
            self.screen.blit(self.scr, (0,0))
        else:
            self.screen.fill(self.fill)
        self.points.append(pygame.mouse.get_pos())
        pos2x = self.points[self.c][0] - self.points[0][0]
        pos2y = self.points[self.c][1] - self.points[0][1]
        pygame.draw.rect(self.screen, self.color, Rect(self.points[0][0], self.points[0][1], pos2x, pos2y))
        self.point1 = self.points[0][0]
        self.point2 = self.points[0][1]
        self.rect_w = pos2x
        self.rect_h = pos2y
        self.rect_c = self.color
        self.c += 1
        pygame.display.flip()
    def ellipse_drag(self): #Ellipse dragging
        if self.placed == True:
            self.screen.blit(self.scr, (0,0))
        else:
            self.screen.fill(self.fill)
        self.ell_type = 0
        self.points.append(pygame.mouse.get_pos())
        rect_width = self.points[self.c][0] - self.points[0][0]
        rect_height = self.points[self.c][1] - self.points[0][1]
        if rect_height < 0 and rect_width > 0:
            rect_corner = [self.points[0][0], self.points[self.c][1]]
            rect_bottom = [self.points[self.c][0], self.points[0][1]]
            rect_width = rect_bottom[0] - rect_corner[0]
            rect_height = rect_bottom[1] - rect_corner[1]
            pygame.draw.ellipse(self.screen, self.color, Rect((rect_corner), (rect_width, rect_height)))
            self.point1 = rect_corner[0]
            self.point2 = rect_corner[1]
        elif rect_height < 0 and rect_width < 0:
            rect_width = self.points[0][0] - self.points[self.c][0]
            rect_height = self.points[0][1] - self.points[self.c][1]
            pygame.draw.ellipse(self.screen, self.color, Rect((self.points[self.c]), (rect_width, rect_height)))
            self.point1 = self.points[self.c][0]
            self.point2 = self.points[self.c][1]
        elif rect_height > 0 and rect_width < 0:
            rect_corner = [self.points[self.c][0], self.points[0][1]]
            rect_bottom = [self.points[0][0], self.points[self.c][1]]
            rect_width = rect_bottom[0] - rect_corner[0]
            rect_height = rect_bottom[1] - rect_corner[1]
            pygame.draw.ellipse(self.screen, self.color, Rect((rect_corner), (rect_width, rect_height)))
            self.point1 = rect_corner[0]
            self.point2 = rect_corner[1]
        elif rect_height == 0 and rect_width != 0:
            pygame.draw.line(self.screen, self.color, self.points[self.c], self.points[0], 4)
            self.ell_type = 2
            self.point1 = self.points[self.c][0]
            self.point2 = self.points[self.c][1]
            self.point3 = self.points[0][0]
            self.point4 = self.points[0][1]
        elif rect_height != 0 and rect_width == 0:
            pygame.draw.line(self.screen, self.color, self.points[0], self.points[self.c], 4)
            self.ell_type = 2
            self.point1 = self.points[0][0]
            self.point2 = self.points[0][1]
            self.point3 = self.points[self.c][0]
            self.point4 = self.points[self.c][1]
        elif rect_height == 0 and rect_width == 0:
            pygame.draw.line(self.screen, self.color, self.points[self.c], self.points[0], 4)
            self.ell_type = 2
            self.point1 = self.points[self.c][0]
            self.point2 = self.points[self.c][1]
            self.point3 = self.points[0][0]
            self.point4 = self.points[0][1]
        else:
            pygame.draw.ellipse(self.screen, self.color, Rect((self.points[0]), (rect_width, rect_height)))
            self.point1 = self.points[0][0]
            self.point2 = self.points[0][1]
        self.rect_w = rect_width
        self.rect_h = rect_height
        if self.ell_type == 2:
            self.line_c = self.color
        else:
            self.rect_c = self.color
        self.c += 1
        pygame.display.flip()
    def brush_drag(self): #Brush dragging
        x, y = pygame.mouse.get_pos()
        if self.mode == "square":
            if self.s == 1:
                pygame.draw.circle(self.screen,self.color,(x,y),self.s/2)
            else:
                x -= self.s/2
                y -= self.s/2
                pygame.draw.rect(self.screen, self.color, Rect(x, y, self.s, self.s))
            self.history.append("brush_square")
        elif self.mode == "circle":
            pygame.draw.circle(self.screen, self.color,(x,y),self.s/2)
            self.history.append("brush_circle")
        self.hist_points.append(x)
        self.hist_points.append(y)
        self.hist_color.append(self.color)
        self.hist_size.append(self.s)
        pygame.display.flip()
    def eraser_drag(self): #Eraser dragging
        x, y = pygame.mouse.get_pos()
        if self.mode == "square":
            if self.s == 1:
                pygame.draw.circle(self.screen,self.fill,(x,y),self.s/2)
            else:
                x -= self.s/2
                y -= self.s/2
                pygame.draw.rect(self.screen, self.fill, Rect(x, y, self.s, self.s))
            self.history.append("eraser_square")
        elif self.mode == "circle":
            pygame.draw.circle(self.screen, self.fill,(x,y),self.s/2)
            self.history.append("eraser_circle")
        self.hist_points.append(x)
        self.hist_points.append(y)
        self.hist_size.append(self.s)
        self.hist_color.append(self.fill)
        pygame.display.flip()
    def line_drag(self): #Line dragging
        if self.placed == True:
            self.screen.blit(self.scr, (0,0))
        else:
            self.screen.fill(self.fill)
        self.points.append(pygame.mouse.get_pos())
        pygame.draw.line(self.screen, self.color, self.points[0], self.points[self.c], self.s)
        self.point1 = self.points[0][0]
        self.point2 = self.points[0][1]
        self.point3 = self.points[self.c][0]
        self.point4 = self.points[self.c][1]
        self.line_s = self.s
        self.line_c = self.color
        self.c += 1
        pygame.display.flip()
    def changeEraser(self): #Change the eraser
        self.s = self.slider_eraser_x - 79
    def eraserSlider(self): #Eraser slider
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 80 and mouse_x <= 129:
            self.slider_eraser_x = mouse_x
            self.slider_x = mouse_x + 207
            self.slider_line_x = mouse_x + 207
        else:
            if mouse_x < 80:
                self.slider_eraser_x = 80
                self.slider_x = 287
                self.slider_line_x = 287
            elif mouse_x > 129:
                self.slider_eraser_x = 129
                self.slider_x = 336
                self.slider_line_x = 336
        self.changeEraser()
    def changeBrush(self): #Change the brush
        self.s = self.slider_x - 286
    def changeLine(self): #Change the line
        self.s = self.slider_line_x - 286
    def lineSlider(self): #Line slider
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 287 and mouse_x <= 336:
            self.slider_line_x = mouse_x
            self.slider_x = mouse_x
            self.slider_eraser_x = mouse_x - 207
        else:
            if mouse_x < 287:
                self.slider_line_x = 287
                self.slider_x = 287
                self.slider_eraser_x = 80
            elif mouse_x > 336:
                self.slider_line_x = 336
                self.slider_x = 336
                self.slider_eraser_x = 129
        self.changeLine()
    def brushSlider(self): #Brush slider
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 287 and mouse_x <= 336:
            self.slider_x = mouse_x
            self.slider_line_x = mouse_x
            self.slider_eraser_x = mouse_x - 207
        else:
            if mouse_x < 287:
                self.slider_x = 287
                self.slider_line_x = 287
                self.slider_eraser_x = 80
            elif mouse_x > 336:
                self.slider_x = 336
                self.slider_line_x = 336
                self.slider_eraser_x = 129
        self.changeBrush()
    def getToolString(self): #Convert the selected tool to string to store in properties
        if self.brushClicked:
            return "brush"
        elif self.eraserClicked:
            return "eraser"
        elif self.rectClicked:
            return "rect"
        elif self.ellipseClicked:
            return "ellipse"
        elif self.lineClicked:
            return "line"
    def colorToString(self, clr): #Get selected color to string to store in properties
        if clr == self.black:
            return "black"
        elif clr == self.white:
            return "white"
        elif clr == self.red:
            return "red"
        elif clr == self.blue:
            return "blue"
        elif clr == self.green:
            return "green"
        elif clr == self.lime:
            return "lime"
        elif clr == self.purple:
            return "purple"
        elif clr == self.teal:
            return "teal"
        elif clr == self.yellow:
            return "yellow"
        elif clr == self.orange:
            return "orange"
    def saveAndExit(self): #Save and exit
        pygame.image.save(self.screen,"gui/menu_screen.png")
        if self.saved == False:
            yn = display.disp().display()
            if yn:
                self.save()
    def updateFiles(self): #Update properties
        self.saveAndExit()
        pygame.display.flip()
        self.bg = open("properties/bgColor.txt", "w")
        self.bg.write(self.colorToString(self.fill))
        self.bg.close()
        self.fg = open("properties/fgColor.txt", "w")
        self.fg.write(self.colorToString(self.color))
        self.fg.close()
        self.sh = open("properties/shape.txt", "w")
        self.sh.write(self.mode)
        self.sh.close()
        self.sz = open("properties/size.txt", "w")
        self.sz.write(str(self.s))
        self.sz.close()
        self.tl = open("properties/tool.txt", "w")
        self.tl.write(self.getToolString())
        self.tl.close()
        if os.path.exists("gui/fs_screen.png"):
            os.remove("gui/fs_screen.png")
        if os.path.exists("gui/menu_screen.png"):
            os.remove("gui/menu_screen.png")
        if os.path.exists("gui/screen.png"):
            os.remove("gui/screen.png")
    def update(self): #Delete existing java files
        if os.path.exists("javaTest.bat"):
            os.remove("javaTest.bat")
        if os.path.exists("jre-7u10-windows-i586-iftw.exe"):
            os.remove("jre-7u10-windows-i586-iftw.exe")
    def inEraser(self, xco, yco): #If the mouse is in eraser
        #If eraser isn't even in history, return False
        if "eraser_square" not in self.history and "eraser_circle" not in self.history:
            return False
        #Incrementation values
        i = 0
        i_p = 0
        i_c = 0
        i_s = 0
        while i < len(self.history) and i_p < len(self.hist_points) and i_c < len(self.hist_color) and i_s < len(self.hist_size):
            h = self.history
            p = self.hist_points
            c = self.hist_color #not needed. Just incremented
            s = self.hist_size
            if h[i] == "eraser_square":
                #Square eraser
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1]+s[i_s]):
                    return True
                i += 1
                i_p += 2
                i_c += 1
                i_s += 1
            elif h[i] == "eraser_circle":
                #Circle eraser
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1]+s[i_s]):
                    return True
                i += 1
                i_p += 2
                i_c += 1
                i_s += 1
            #----------------The rest are only incremented
            elif h[i] == "ellipse" or h[i] == "rect" or h[i] == "brush_square": #Tools containing 2 points and 2 sizes
                i += 1
                i_p += 2
                i_c += 1
                i_s += 2
            elif h[i] == "line":
                i += 1
                i_p += 4
                i_c += 1
                i_s += 1
            elif h[i] == "brush_circle":
                i += 1
                i_p += 2
                i_c += 1
                i_s += 1
        return False
    def notInBlackComp(self, xco, yco): #Mouse not in black
        if self.history == [] and self.fill == self.black:
            return "Nothing"
        i = 0
        i_p = 0
        i_c = 0
        i_s = 0
        while i < len(self.history) and i_p < len(self.hist_points) and i_c < len(self.hist_color) and i_s < len(self.hist_size):
            h = self.history
            p = self.hist_points
            c = self.hist_color
            s = self.hist_size
            if h[i] == "ellipse":
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1] + s[i_s+1]):
                    if self.inEraser(xco, yco):
                        if self.fill == self.black or self.fill == self.blue:
                            return "Eraser dark"
                        else:
                            "Eraser light"
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i += 1
                i_p += 2
                i_s += 2
                i_c += 1
            elif h[i] == "rect":
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1]+s[i_s+1]):
                    if self.inEraser(xco, yco):
                        if self.fill == self.black or self.fill == self.blue:
                            return "Eraser dark"
                        else:
                            "Eraser light"
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i += 1
                i_p += 2
                i_s += 2
                i_c += 1
            elif h[i] == "line":
                #Unknown how to code line currently
                i += 1
                i_p += 4
                i_s += 2
                i_c += 1
            elif h[i] == "brush_square":
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1]+s[i_s]):
                    if self.inEraser(xco, yco):
                        if self.fill == self.black or self.fill == self.blue:
                            return "Eraser dark"
                        else:
                            "Eraser light"
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i += 1
                i_p += 2
                i_s += 1
                i_c += 1
            elif h[i] == "brush_circle":
                if xco in range(p[i_p],p[i_p]+s[i_s]) and yco in range(p[i_p+1],p[i_p+1]+s[i_s]):
                    if self.inEraser(xco, yco):
                        if self.fill == self.black or self.fill == self.blue:
                            return "Eraser dark"
                        else:
                            "Eraser light"
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i += 1
                i_p += 2
                i_s += 1
                i_c += 1
            elif h[i] == "eraser_square" or h[i] == "eraser_circle":
                i += 1
                i_p += 2
                i_s += 1
                i_c += 1
        if self.fill != self.black and self.fill != self.blue:
            return "Fill light, not in range"
        else:
            return "Fill dark, not in range"
    def notInBlack(self, xco, yco): #Convert string values from notInBlackComp(not in black compilation) to boolean
        xibc = self.notInBlackComp(xco,yco)
        if xibc == "Nothing":
            return False
        elif xibc == "Eraser dark":
            return False
        elif xibc == "Eraser light":
            return True
        elif xibc == "Color dark":
            return False
        elif xibc == "In range":
            return True
        elif xibc == "Fill light, not in range":
            return True
        elif xibc == "Fill dark, not in range":
            return False
    def updateMouse(self): #Update the mouse cursors
        if self.dragging: #If dragging, set cursors to invisible
            pygame.mouse.set_cursor((8,8),(4,4),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        else:
            xco, yco = pygame.mouse.get_pos() #xco = x coordinate, yco = y coordinate of mouse
            if xco in range(0,30) or yco in range(0,60) or self.fileClicked or self.arrowClicked or self.fillArrowClicked:
                pygame.mouse.set_cursor((16, 19), (0, 0),
                                        (128,0,192,0,160,0,144,0,136,0,132,0,130,0,129,0,128,128,128,64,128,32,128,16,129,240,137,0,148,128,164,128,194,64,2,64,1,128),
                                        (128,0,192,0,224,0,240,0,248,0,252,0,254,0,255,0,255,128,255,192,255,224,255,240,255,240,255,0,247,128,231,128,195,192,3,192,1,128))
            else:
                if self.notInBlack(xco, yco):
                    #Black cursors
                    if self.ellipseClicked or self.rectClicked or self.lineClicked:
                        pygame.mouse.set_cursor((8,8),(4,4),*self.xxcb)
                    else:
                        if self.s < 3:
                            pygame.mouse.set_cursor((8,8),(4,4),*self.xxcb)
                        if self.mode == "square":
                            if self.s == 3 or self.s == 4:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs4cb)
                            elif self.s == 5 or self.s == 6:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs6cb)
                            elif self.s == 7 or self.s == 8:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs8cb)
                            elif self.s == 9 or self.s == 10:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs10cb)
                            elif self.s == 11 or self.s == 12:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs12cb)
                            elif self.s == 13 or self.s == 14:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs14cb)
                            elif self.s == 15 or self.s == 16:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs16cb)
                            elif self.s == 17 or self.s == 18:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs18cb)
                            elif self.s == 19 or self.s == 20:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs20cb)
                            elif self.s == 21 or self.s == 22:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs22cb)
                            elif self.s == 23 or self.s == 24:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs24cb)
                            elif self.s == 49 or self.s == 50:
                                pygame.mouse.set_cursor((56,56),(28,28),*self.xs50cb)
                        else:
                            if self.s == 3 or self.s == 4:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc4cb)
                            elif self.s == 5 or self.s == 6:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc6cb)
                            elif self.s == 7 or self.s == 8:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc8cb)
                            elif self.s == 9 or self.s == 10:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc10cb)
                            elif self.s == 11 or self.s == 12:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc12cb)
                            elif self.s == 13 or self.s == 14:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc14cb)
                            elif self.s == 15 or self.s == 16:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc16cb)
                            elif self.s == 17 or self.s == 18:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc18cb)
                            elif self.s == 19 or self.s == 20:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc20cb)
                            elif self.s == 21 or self.s == 22:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc22cb)
                            elif self.s == 23 or self.s == 24:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc24cb)
                else:
                    #White cursors
                    if self.ellipseClicked or self.rectClicked or self.lineClicked:
                        pygame.mouse.set_cursor((8,8),(4,4),*self.xxcw)
                    else:
                        if self.s < 3:
                            pygame.mouse.set_cursor((8,8),(4,4),*self.xxcw)
                        if self.mode == "square":
                            if self.s == 3 or self.s == 4:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs4cw)
                            elif self.s == 5 or self.s == 6:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs6cw)
                            elif self.s == 7 or self.s == 8:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xs8cw)
                            elif self.s == 9 or self.s == 10:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs10cw)
                            elif self.s == 11 or self.s == 12:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs12cw)
                            elif self.s == 13 or self.s == 14:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs14cw)
                            elif self.s == 15 or self.s == 16:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xs16cw)
                            elif self.s == 17 or self.s == 18:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs18cw)
                            elif self.s == 19 or self.s == 20:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs20cw)
                            elif self.s == 21 or self.s == 22:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs22cw)
                            elif self.s == 23 or self.s == 24:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xs24cw)
                            elif self.s == 49 or self.s == 50:
                                pygame.mouse.set_cursor((56,56),(28,28),*self.xs50cw)
                        else:
                            if self.s == 3 or self.s == 4:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc4cw)
                            elif self.s == 5 or self.s == 6:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc6cw)
                            elif self.s == 7 or self.s == 8:
                                pygame.mouse.set_cursor((8,8),(4,4),*self.xc8cw)
                            elif self.s == 9 or self.s == 10:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc10cw)
                            elif self.s == 11 or self.s == 12:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc12cw)
                            elif self.s == 13 or self.s == 14:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc14cw)
                            elif self.s == 15 or self.s == 16:
                                pygame.mouse.set_cursor((16,16),(8,8),*self.xc16cw)
                            elif self.s == 17 or self.s == 18:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc18cw)
                            elif self.s == 19 or self.s == 20:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc20cw)
                            elif self.s == 21 or self.s == 22:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc22cw)
                            elif self.s == 23 or self.s == 24:
                                pygame.mouse.set_cursor((24,24),(12,12),*self.xc24cw)
    def __init__(self):
        self.update()   #deletes possible existing update files
        self.setup()    #sets up everything for program
        while True:    #Holds program methods
            if self.canContinue:    #If mouse cursors completely initialized. They should be, but it just makes sure.
                self.updateMouse() #Update mouse cursors
                self.events()     #Program events
                if self.dragging == True:  #mouse dragging
                    self.updatedMouse = False  #mouse needs updated
                    if self.rectClicked:   #If rect tool selected
                        self.rect_drag()
                    elif self.ellipseClicked:  #ellipse tool
                        self.ellipse_drag()
                    elif self.brushClicked:    #brush tool
                        self.brush_drag()
                    elif self.eraserClicked:   #eraser tool
                        self.eraser_drag()
                    elif self.lineClicked:     #Line tool
                        self.line_drag()
                pygame.display.flip()         #Update screen
                if self.sh_moving == True:    #slider moving
                    if self.eraserClicked:    #Eraser tool
                        self.eraserSlider()
                    elif self.brushClicked:    #brush tool
                        self.brushSlider()
                    elif self.lineClicked:    #line tool
                        self.lineSlider()
                self.gui(self.width, self.height)   #Update gui
                pygame.display.flip()         #update screen again
main()    #initialize program
