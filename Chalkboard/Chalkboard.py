#
#Chalkboard 2.3
#
#   Created and Maintained by the Kamakwazee Open Source Team
#           -Tabor Kvasnicka   ]----Currently, only person
#
#Expected Features:
#   Line color changing
#   Circle/Ellipse color changing fix
#   Eraser color fix
#   Shape outline
#   Text
#
#Clip art postponed until 3.0 or later as we need to have access to
#a larger clip art database.
#
#Text tool nearly complete
#Eraser color fix complete
#Ellipse color fix complete
#Brush/Eraser tool now configured to not have gaps
#Shape outline complete
#
#Import dependencies
import pygame, sys, Tkinter, math, os, save_as, open_file, display, wx
from fontTools import ttLib
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
        #Square 30x30 32x32
        xs30 = ("                                ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                "                                ")
        self.xs30cb = pygame.cursors.compile(xs30, white='X', black='.', xor='0')
        self.xs30cw = pygame.cursors.compile(xs30, white='.', black='X', xor='0')
        #Square 32x32 32x32
        xs32 = ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.xs32cb = pygame.cursors.compile(xs32, white='X', black='.', xor='0')
        self.xs32cw = pygame.cursors.compile(xs32, white='.', black='X', xor='0')
        #Square 34x34 40x40
        xs34 = ("                                        ",
                "                                        ",
                "                                        ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "                                        ",
                "                                        ",
                "                                        ")
        self.xs34cb = pygame.cursors.compile(xs34, white='X', black='.', xor='0')
        self.xs34cw = pygame.cursors.compile(xs34, white='.', black='X', xor='0')
        #Square 36x36 40x40
        xs36 = ("                                        ",
                "                                        ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "                                        ",
                "                                        ")
        self.xs36cb = pygame.cursors.compile(xs36, white='X', black='.', xor='0')
        self.xs36cw = pygame.cursors.compile(xs36, white='.', black='X', xor='0')
        #Square 38x38 40x40
        xs38 = ("                                        ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                "                                        ")
        self.xs38cb = pygame.cursors.compile(xs38, white='X', black='.', xor='0')
        self.xs38cw = pygame.cursors.compile(xs38, white='.', black='X', xor='0')
        #Square 40x40 40x40
        xs40 = ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.xs40cb = pygame.cursors.compile(xs40, white='X', black='.', xor='0')
        self.xs40cw = pygame.cursors.compile(xs40, white='.', black='X', xor='0')
        #Square 42x42 48x48
        xs42 = ("                                                ",
                "                                                ",
                "                                                ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ",
                "                                                ",
                "                                                ",
                "                                                ")
        self.xs42cb = pygame.cursors.compile(xs42, white='X', black='.', xor='0')
        self.xs42cw = pygame.cursors.compile(xs42, white='.', black='X', xor='0')
        #Square 44x44 48x48
        xs44 = ("                                                ",
                "                                                ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
                "                                                ",
                "                                                ")
        self.xs44cb = pygame.cursors.compile(xs44, white='X', black='.', xor='0')
        self.xs44cw = pygame.cursors.compile(xs44, white='.', black='X', xor='0')
        #Square 46x46 48x48
        xs46 = ("                                                ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ",
                "                                                ")
        self.xs46cb = pygame.cursors.compile(xs46, white='X', black='.', xor='0')
        self.xs46cw = pygame.cursors.compile(xs46, white='.', black='X', xor='0')
        #Square 48x48 48x48
        xs48 = ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.xs48cb = pygame.cursors.compile(xs48, white='X', black='.', xor='0')
        self.xs48cw = pygame.cursors.compile(xs48, white='.', black='X', xor='0')
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
        #Circle 26x26 32x32
        xc26 = ("                                ",
                "                                ",
                "                                ",
                "            XXXXXXXX            ",
                "          XX        XX          ",
                "        XX            XX        ",
                "       X                X       ",
                "      X                  X      ",
                "     X                    X     ",
                "     X                    X     ",
                "    X                      X    ",
                "    X                      X    ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "   X                        X   ",
                "    X                      X    ",
                "    X                      X    ",
                "     X                    X     ",
                "     X                    X     ",
                "      X                  X      ",
                "       X                X       ",
                "        XX            XX        ",
                "          XX        XX          ",
                "            XXXXXXXX            ",
                "                                ",
                "                                ",
                "                                ")
        self.xc26cb = pygame.cursors.compile(xc26, white='X', black='.', xor='0')
        self.xc26cw = pygame.cursors.compile(xc26, white='.', black='X', xor='0')
        #Circle 28x28 32x32
        xc28 = ("                                ",
                "                                ",
                "            XXXXXXXX            ",
                "          XX        XX          ",
                "        XX            XX        ",
                "       X                X       ",
                "      X                  X      ",
                "     X                    X     ",
                "    X                      X    ",
                "    X                      X    ",
                "   X                        X   ",
                "   X                        X   ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "   X                        X   ",
                "   X                        X   ",
                "    X                      X    ",
                "    X                      X    ",
                "     X                    X     ",
                "      X                  X      ",
                "       X                X       ",
                "        XX            XX        ",
                "          XX        XX          ",
                "            XXXXXXXX            ",
                "                                ",
                "                                ")
        self.xc28cb = pygame.cursors.compile(xc28, white='X', black='.', xor='0')
        self.xc28cw = pygame.cursors.compile(xc28, white='.', black='X', xor='0')
        #Circle 30x30 32x32
        xc30 = ("                                ",
                "            XXXXXXXX            ",
                "         XXX        XXX         ",
                "        X              X        ",
                "      XX                XX      ",
                "     X                    X     ",
                "    X                      X    ",
                "    X                      X    ",
                "   X                        X   ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                "  X                          X  ",
                "  X                          X  ",
                "  X                          X  ",
                "   X                        X   ",
                "    X                      X    ",
                "    X                      X    ",
                "     X                    X     ",
                "      XX                XX      ",
                "        X              X        ",
                "         XXX        XXX         ",
                "            XXXXXXXX            ",
                "                                ")
        self.xc30cb = pygame.cursors.compile(xc30, white='X', black='.', xor='0')
        self.xc30cw = pygame.cursors.compile(xc30, white='.', black='X', xor='0')
        #Circle 32x32 32x32
        xc32 = ("            XXXXXXXX            ",
                "         XXX        XXX         ",
                "       XX              XX       ",
                "      X                  X      ",
                "     X                    X     ",
                "    X                      X    ",
                "   X                        X   ",
                "  X                          X  ",
                "  X                          X  ",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                "X                              X",
                " X                            X ",
                " X                            X ",
                " X                            X ",
                "  X                          X  ",
                "  X                          X  ",
                "   X                        X   ",
                "    X                      X    ",
                "     X                    X     ",
                "      X                  X      ",
                "       XX              XX       ",
                "         XXX        XXX         ",
                "            XXXXXXXX            ")
        self.xc32cb = pygame.cursors.compile(xc32, white='X', black='.', xor='0')
        self.xc32cw = pygame.cursors.compile(xc32, white='.', black='X', xor='0')
        #Circle 34x34 40x40
        xc34 = ("                                        ",
                "                                        ",
                "                                        ",
                "                XXXXXXXX                ",
                "             XXX        XXX             ",
                "           XX              XX           ",
                "          X                  X          ",
                "        XX                    XX        ",
                "       X                        X       ",
                "       X                        X       ",
                "      X                          X      ",
                "     X                            X     ",
                "     X                            X     ",
                "    X                              X    ",
                "    X                              X    ",
                "    X                              X    ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "    X                              X    ",
                "    X                              X    ",
                "    X                              X    ",
                "     X                            X     ",
                "     X                            X     ",
                "      X                          X      ",
                "       X                        X       ",
                "       X                        X       ",
                "        XX                    XX        ",
                "          X                  X          ",
                "           XX              XX           ",
                "             XXX        XXX             ",
                "                XXXXXXXX                ",
                "                                        ",
                "                                        ",
                "                                        ")
        self.xc34cb = pygame.cursors.compile(xc34, white='X', black='.', xor='0')
        self.xc34cw = pygame.cursors.compile(xc34, white='.', black='X', xor='0')
        #Circle 36x36 40x40
        xc36 = ("                                        ",
                "                                        ",
                "                XXXXXXXX                ",
                "             XXX        XXX             ",
                "           XX              XX           ",
                "         XX                  XX         ",
                "        X                      X        ",
                "       X                        X       ",
                "      X                          X      ",
                "     X                            X     ",
                "     X                            X     ",
                "    X                              X    ",
                "    X                              X    ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "   X                                X   ",
                "   X                                X   ",
                "   X                                X   ",
                "    X                              X    ",
                "    X                              X    ",
                "     X                            X     ",
                "     X                            X     ",
                "      X                          X      ",
                "       X                        X       ",
                "        X                      X        ",
                "         XX                  XX         ",
                "           XX              XX           ",
                "             XXX        XXX             ",
                "                XXXXXXXX                ",
                "                                        ",
                "                                        ")
        self.xc36cb = pygame.cursors.compile(xc36, white='X', black='.', xor='0')
        self.xc36cw = pygame.cursors.compile(xc36, white='.', black='X', xor='0')
        #Circle 38x38 40x40
        xc38 = ("                                        ",
                "                XXXXXXXX                ",
                "             XXX        XXX             ",
                "           XX              XX           ",
                "         XX                  XX         ",
                "        X                      X        ",
                "       X                        X       ",
                "      X                          X      ",
                "     X                            X     ",
                "    X                              X    ",
                "    X                              X    ",
                "   X                                X   ",
                "   X                                X   ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                "  X                                  X  ",
                "  X                                  X  ",
                "  X                                  X  ",
                "   X                                X   ",
                "   X                                X   ",
                "    X                              X    ",
                "    X                              X    ",
                "     X                            X     ",
                "      X                          X      ",
                "       X                        X       ",
                "        X                      X        ",
                "         XX                  XX         ",
                "           XX              XX           ",
                "             XXX        XXX             ",
                "                XXXXXXXX                ",
                "                                        ")
        self.xc38cb = pygame.cursors.compile(xc38, white='X', black='.', xor='0')
        self.xc38cw = pygame.cursors.compile(xc38, white='.', black='X', xor='0')
        #Circle 40x40 40x40
        xc40 = ("                XXXXXXXX                ",
                "            XXXX        XXXX            ",
                "          XX                XX          ",
                "         X                    X         ",
                "       XX                      XX       ",
                "      X                          X      ",
                "     X                            X     ",
                "    X                              X    ",
                "    X                              X    ",
                "   X                                X   ",
                "  X                                  X  ",
                "  X                                  X  ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                "X                                      X",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                " X                                    X ",
                "  X                                  X  ",
                "  X                                  X  ",
                "   X                                X   ",
                "    X                              X    ",
                "    X                              X    ",
                "     X                            X     ",
                "      X                          X      ",
                "       XX                      XX       ",
                "         X                    X         ",
                "          XX                XX          ",
                "            XXXX        XXXX            ",
                "                XXXXXXXX                ")
        self.xc40cb = pygame.cursors.compile(xc40, white='X', black='.', xor='0')
        self.xc40cw = pygame.cursors.compile(xc40, white='.', black='X', xor='0')
        #Circle 42x42 48x48
        xc42 = ("                                                ",
                "                                                ",
                "                                                ",
                "                   XXXXXXXXXX                   ",
                "                XXX          XXX                ",
                "              XX                XX              ",
                "            XX                    XX            ",
                "           X                        X           ",
                "          X                          X          ",
                "         X                            X         ",
                "        X                              X        ",
                "       X                                X       ",
                "      X                                  X      ",
                "      X                                  X      ",
                "     X                                    X     ",
                "     X                                    X     ",
                "    X                                      X    ",
                "    X                                      X    ",
                "    X                                      X    ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "    X                                      X    ",
                "    X                                      X    ",
                "    X                                      X    ",
                "     X                                    X     ",
                "     X                                    X     ",
                "      X                                  X      ",
                "      X                                  X      ",
                "       X                                X       ",
                "        X                              X        ",
                "         X                            X         ",
                "          X                          X          ",
                "           X                        X           ",
                "            XX                    XX            ",
                "              XX                XX              ",
                "                XXX          XXX                ",
                "                   XXXXXXXXXX                   ",
                "                                                ",
                "                                                ",
                "                                                ")
        self.xc42cb = pygame.cursors.compile(xc42, white='X', black='.', xor='0')
        self.xc42cw = pygame.cursors.compile(xc42, white='.', black='X', xor='0')
        #Circle 44x44 48x48
        xc44 = ("                                                ",
                "                                                ",
                "                   XXXXXXXXXX                   ",
                "                XXX          XXX                ",
                "              XX                XX              ",
                "            XX                    XX            ",
                "           X                        X           ",
                "         XX                          XX         ",
                "        X                              X        ",
                "       X                                X       ",
                "       X                                X       ",
                "      X                                  X      ",
                "     X                                    X     ",
                "     X                                    X     ",
                "    X                                      X    ",
                "    X                                      X    ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "   X                                        X   ",
                "   X                                        X   ",
                "   X                                        X   ",
                "    X                                      X    ",
                "    X                                      X    ",
                "     X                                    X     ",
                "     X                                    X     ",
                "      X                                  X      ",
                "       X                                X       ",
                "       X                                X       ",
                "        X                              X        ",
                "         XX                          XX         ",
                "           X                        X           ",
                "            XX                    XX            ",
                "              XX                XX              ",
                "                XXX          XXX                ",
                "                   XXXXXXXXXX                   ",
                "                                                ",
                "                                                ")
        self.xc44cb = pygame.cursors.compile(xc44, white='X', black='.', xor='0')
        self.xc44cw = pygame.cursors.compile(xc44, white='.', black='X', xor='0')
        #Circle 46x46 48x48
        xc46 = ("                                                ",
                "                   XXXXXXXXXX                   ",
                "                XXX          XXX                ",
                "              XX                XX              ",
                "            XX                    XX            ",
                "          XX                        XX          ",
                "         X                            X         ",
                "        X                              X        ",
                "       X                                X       ",
                "      X                                  X      ",
                "     X                                    X     ",
                "     X                                    X     ",
                "    X                                      X    ",
                "    X                                      X    ",
                "   X                                        X   ",
                "   X                                        X   ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "   X                                        X   ",
                "   X                                        X   ",
                "    X                                      X    ",
                "    X                                      X    ",
                "     X                                    X     ",
                "     X                                    X     ",
                "      X                                  X      ",
                "       X                                X       ",
                "        X                              X        ",
                "         X                            X         ",
                "          XX                        XX          ",
                "            XX                    XX            ",
                "              XX                XX              ",
                "                XXX          XXX                ",
                "                   XXXXXXXXXX                   ",
                "                                                ")
        self.xc46cb = pygame.cursors.compile(xc46, white='X', black='.', xor='0')
        self.xc46cw = pygame.cursors.compile(xc46, white='.', black='X', xor='0')
        #Circle 48x48 48x48
        xc48 = ("                   XXXXXXXXXX                   ",
                "                XXX          XXX                ",
                "             XXX                XXX             ",
                "            X                      X            ",
                "          XX                        XX          ",
                "         X                            X         ",
                "        X                              X        ",
                "       X                                X       ",
                "      X                                  X      ",
                "     X                                    X     ",
                "    X                                      X    ",
                "    X                                      X    ",
                "   X                                        X   ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                "X                                              X",
                " X                                            X ",
                " X                                            X ",
                " X                                            X ",
                "  X                                          X  ",
                "  X                                          X  ",
                "  X                                          X  ",
                "   X                                        X   ",
                "    X                                      X    ",
                "    X                                      X    ",
                "     X                                    X     ",
                "      X                                  X      ",
                "       X                                X       ",
                "        X                              X        ",
                "         X                            X         ",
                "          XX                        XX          ",
                "            X                      X            ",
                "             XXX                XXX             ",
                "                XXX          XXX                ",
                "                   XXXXXXXXXX                   ")
        self.xc48cb = pygame.cursors.compile(xc48, white='X', black='.', xor='0')
        self.xc48cw = pygame.cursors.compile(xc48, white='.', black='X', xor='0')
        #Circle 50x50 56x56
        xc50 = ("                                                        ",
                "                                                        ",
                "                                                        ",
                "                       XXXXXXXXXX                       ",
                "                   XXXX          XXXX                   ",
                "                 XX                  XX                 ",
                "               XX                      XX               ",
                "              X                          X              ",
                "            XX                            XX            ",
                "           X                                X           ",
                "          X                                  X          ",
                "         X                                    X         ",
                "        X                                      X        ",
                "        X                                      X        ",
                "       X                                        X       ",
                "      X                                          X      ",
                "      X                                          X      ",
                "     X                                            X     ",
                "     X                                            X     ",
                "    X                                              X    ",
                "    X                                              X    ",
                "    X                                              X    ",
                "    X                                              X    ",
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
                "    X                                              X    ",
                "    X                                              X    ",
                "    X                                              X    ",
                "    X                                              X    ",
                "     X                                            X     ",
                "     X                                            X     ",
                "      X                                          X      ",
                "      X                                          X      ",
                "       X                                        X       ",
                "        X                                      X        ",
                "        X                                      X        ",
                "         X                                    X         ",
                "          X                                  X          ",
                "           X                                X           ",
                "            XX                            XX            ",
                "              X                          X              ",
                "               XX                      XX               ",
                "                 XX                  XX                 ",
                "                   XXXX          XXXX                   ",
                "                       XXXXXXXXXX                       ",
                "                                                        ",
                "                                                        ",
                "                                                        ")
        self.xc50cb = pygame.cursors.compile(xc50, white='X', black='.', xor='0')
        self.xc50cw = pygame.cursors.compile(xc50, white='.', black='X', xor='0')
        #Text 16x16
        xt16 = ("XXXX    XXXXXXXX",
                "XXX     XXXXXXXX",
                "XX         XX   ",
                "X          XX   ",
                "           XX   ",
                "           XX   ",
                "           XX   ",
                "           XX   ",
                "           XX   ",
                "           XX   ",
                "                ",
                "                ",
                "                ",
                "                ",
                "                ",
                "                ")
        self.xt16cb = pygame.cursors.compile(xt16, white='X', black='.', xor='0')
        self.xt16cw = pygame.cursors.compile(xt16, white='.', black='X', xor='0')
        self.canContinue = True  #Allow for continuing
    #Initialize fonts
    def setupFonts(self):
        fa = pygame.font.get_fonts()
        i = 0
        while i < len(fa):
            c = list(pygame.font.match_font(fa[i]))
            if (c[len(c)-1] == 'f' or c[len(c)-1] == 'F'):
                fn = self.getFontName(ttLib.TTFont(pygame.font.match_font(fa[i])))[0]
                if (fn != "Wingdings 3" and fn != "Wingdings 2" and fn != "Wingdings" and fn != "Symbol" and fn != "MS Outlook" and fn != "jbn_boot" and fn != "ZWAdobeF" and fn != "kor_boot"
                    and fn != "cht_boot" and fn != "chs_boot" and fn != "wgl4_boot" and fn != "MS Reference Specialty" and fn != "Bookshelf Symbol 7" and fn != "Webdings" and fn != "jpn_boot"):
                    self.fontNames.append(fn)
            i += 1
        ii = 0
        pos = 55
        while ii < ((len(self.fontNames))*20):
            self.fontPositions.append(pos + ii)
            ii += 20
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
            self.last_x = 0
            self.last_y = 0
            self.s = 1 #Size
            self.c = 1 #Point incrementation
            root = Tk() #Tkinter root menu
            self.window_w = root.winfo_screenwidth() #Screen width
            self.window_h = root.winfo_screenheight() #Screen height
            if (float(self.window_w)/float(self.window_h)) == (16/9): #If the width/height ratio is 16/9 (widescreen), set size to 1280,720
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
            self.textClicked = False
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
            self.whiteOutlineSelected = False 
            self.blackOutlineSelected = False
            self.redOutlineSelected = False
            self.orangeOutlineSelected = False
            self.limeOutlineSelected = False
            self.greenOutlineSelected = False
            self.blueOutlineSelected = False
            self.tealOutlineSelected = False
            self.purpleOutlineSelected = False
            self.yellowOutlineSelected = False
            self.noneOutlineSelected = False
            self.outlineArrowClicked = False
            #slider x locations
            self.slider_x = 287
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
            self.hist_font = []
            self.hist_text = []
            self.hist_oc = []
            self.hist_os = []
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
            self.rect_oc = self.black
            self.rect_os = self.s
            self.line_s = 0
            self.line_c = (0,0,0)
            self.cx = self.width-50 #Clear button position
            self.fax = self.cx-22 #Fill arrow position
            self.fx = self.fax-136 #Fill positions
            self.ffx = self.fx-100 #Fill text position
            self.outline_color = "None"
            #Text tool variables
            self.fontNames = []
            self.fontPositions = []
            self.fontArrowClicked = False
            self.selectedFont = "Times New Roman" #May change in properties
            self.font = pygame.font.SysFont(self.selectedFont, 12, False, False)
            self.text = ""
            self.typing = False
            self.shift = False
        else: #Otherwise
            self.main_icon = pygame.image.load(self.icon).convert() #Load icon
            pygame.display.set_icon(self.main_icon) #Apply icon
            pygame.display.set_caption(self.title) #Set caption
    #Scroll font up
    def scrollFontUp(self):
        if self.fontPositions[0] != 55:
            newPos = []
            for i in self.fontPositions:
                newPos.append(i+20)
            self.fontPositions = newPos
    #Scroll font down
    def scrollFontDown(self):
        if self.fontPositions[len(self.fontPositions)-1] != 155:
            newPos = []
            for i in self.fontPositions:
                newPos.append(i-20)
            self.fontPositions = newPos
    #Update Font Menu
    def updateFontGui(self):
        i = 0
        i_l = 0
        while i < len(self.fontNames) and i_l < len(self.fontPositions):
            if self.fontPositions[i_l] >= 55 and self.fontPositions[i_l] <= 155:
                f = pygame.font.SysFont(self.fontNames[i], 12, False, False);
                t = f.render(self.fontNames[i], 1, self.black)
                pygame.draw.rect(self.screen, self.white, Rect(564,self.fontPositions[i_l],200,20))
                self.screen.blit(t, (564, self.fontPositions[i_l]))
                pygame.display.flip()
            i += 1
            i_l += 1
        self.screen.blit(pygame.image.load("gui/up.png").convert_alpha(), (764, 75))
        self.screen.blit(pygame.image.load("gui/down.png").convert_alpha(), (764, 155))
    #Resize screen on video resize
    def resizeScreen(self, s):
        pygame.image.save(self.screen,"gui/fs_screen.png") #Save temporary image
        self.screen = pygame.display.set_mode(s, RESIZABLE, 0) #Resize screen to the size changed by user
        pygame.display.flip() #Update screen
        self.width, self.height = s #set the width and height to the event size for the gui
        if self.width < self.window_w/2: #If the width is less than half of the total screen size
            self.width = self.window_w/2;
            self.screen = pygame.display.set_mode((self.width,self.height), RESIZABLE, 0)
        self.cx = self.width-50 #Clear button position
        self.fax = self.cx-22 #Fill arrow position
        self.fx = self.fax-136 #Fill positions
        self.ffx = self.fx-100 #Fill text position
        if self.height < 185: #If the height is less than 185, set it to 185
            self.height = 185
            self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0)
        #Reset gui and add temp. pic to screen
        self.gui(self.width, self.height)
        self.screen.fill(self.fill)
        self.screen.blit(pygame.image.load("gui/fs_screen.png").convert_alpha(),(0,0))
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
                flf = pygame.font.SysFont("Arial", 17, False, False)
                if self.noneOutlineSelected == False:
                    fl = flf.render("Outline", 1, self.black)
                    self.screen.blit(fl, (240, 34))
                    self.screen.blit(pygame.image.load("gui/slider.png").convert_alpha(), (290,38))
                    self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_x, 44))
                ol = flf.render("Outline Color", 1, self.black)
                self.screen.blit(ol, (360, 35))
                if self.whiteOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (460, 34))
                elif self.blackOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (460,34))
                elif self.redOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (460,34))
                elif self.orangeOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (460,34))
                elif self.limeOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (460,34))
                elif self.greenOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (460,34))
                elif self.blueOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (460,34))
                elif self.tealOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (460,34))
                elif self.purpleOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (460,34))
                elif self.yellowOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (460,34))
                elif self.noneOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/none_box.png").convert_alpha(), (460,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (596, 34))
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
                flf = pygame.font.SysFont("Arial", 17, False, False)
                if self.noneOutlineSelected == False:
                    fl = flf.render("Outline", 1, self.black)
                    self.screen.blit(fl, (240, 34))
                    self.screen.blit(pygame.image.load("gui/slider.png").convert_alpha(), (290,38))
                    self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_x, 44))
                ol = flf.render("Outline Color", 1, self.black)
                self.screen.blit(ol, (360, 35))
                if self.whiteOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (460, 34))
                elif self.blackOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (460,34))
                elif self.redOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (460,34))
                elif self.orangeOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (460,34))
                elif self.limeOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (460,34))
                elif self.greenOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (460,34))
                elif self.blueOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (460,34))
                elif self.tealOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (460,34))
                elif self.purpleOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (460,34))
                elif self.yellowOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (460,34))
                elif self.noneOutlineSelected:
                    self.screen.blit(pygame.image.load("gui/none_box.png").convert_alpha(), (460,34))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (596, 34))
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
                self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_x, 44))
            if self.textClicked == False:
                self.screen.blit(pygame.image.load("gui/text.png").convert_alpha(), (3, 210))
            else:
                self.screen.blit(pygame.image.load("gui/text_clicked.png").convert_alpha(), (3, 210))
                flf = pygame.font.SysFont("Arial", 17, False, False)
                fl = flf.render("Font", 1, self.black)
                self.screen.blit(fl, (527, 34))
                pygame.draw.rect(self.screen, self.black, Rect(563,34,202,22))
                pygame.draw.rect(self.screen, self.white, Rect(564,35,200,20))
                f = pygame.font.SysFont(self.selectedFont, 12, False, False)
                t = f.render(self.selectedFont, 1, self.black)
                self.screen.blit(t, (566, 36))
                self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (770, 34))
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
                self.screen.blit(pygame.image.load("gui/slider_handle.png").convert_alpha(), (self.slider_x, 44))
            self.screen.blit(pygame.image.load("gui/fill_txt.png").convert_alpha(), (self.ffx, 33))
            if self.blackFillSelected:
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (self.fx,34))
            elif self.whiteFillSelected:
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (self.fx,34))
            elif self.redFillSelected:
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (self.fx,34))
            elif self.limeFillSelected:
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (self.fx,34))
            elif self.greenFillSelected:
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (self.fx,34))
            elif self.orangeFillSelected:
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (self.fx,34))
            elif self.blueFillSelected:
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (self.fx,34))
            elif self.yellowFillSelected:
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (self.fx,34))
            elif self.tealFillSelected:
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (self.fx,34))
            elif self.purpleFillSelected:
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (self.fx,34))
            self.screen.blit(pygame.image.load("gui/arrow.png").convert_alpha(), (self.fax, 34))
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
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (self.fx,54))
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (self.fx,74))
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (self.fx,94))
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (self.fx,114))
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (self.fx,134))
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (self.fx,154))
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (self.fx,174))
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (self.fx,194))
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (self.fx,214))
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (self.fx, 234))
            if self.fileClicked:
                self.screen.blit(pygame.image.load("gui/save_as.png").convert_alpha(), (0,25))
                self.screen.blit(pygame.image.load("gui/save.png").convert_alpha(), (0,45))
                self.screen.blit(pygame.image.load("gui/open.png").convert_alpha(), (0, 65))
            if self.outlineArrowClicked:
                self.screen.blit(pygame.image.load("gui/white_box.png").convert_alpha(), (460,54))
                self.screen.blit(pygame.image.load("gui/black_box.png").convert_alpha(), (460,74))
                self.screen.blit(pygame.image.load("gui/red_box.png").convert_alpha(), (460,94))
                self.screen.blit(pygame.image.load("gui/orange_box.png").convert_alpha(), (460,114))
                self.screen.blit(pygame.image.load("gui/lime_box.png").convert_alpha(), (460,134))
                self.screen.blit(pygame.image.load("gui/green_box.png").convert_alpha(), (460,154))
                self.screen.blit(pygame.image.load("gui/blue_box.png").convert_alpha(), (460,174))
                self.screen.blit(pygame.image.load("gui/teal_box.png").convert_alpha(), (460,194))
                self.screen.blit(pygame.image.load("gui/purple_box.png").convert_alpha(), (460,214))
                self.screen.blit(pygame.image.load("gui/yellow_box.png").convert_alpha(), (460, 234))
                self.screen.blit(pygame.image.load("gui/none_box.png").convert_alpha(), (460, 254))
        if self.fontArrowClicked:
            self.updateFontGui()
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
        elif t == "text":
            self.textClicked = True
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
        self.slider_x = 286 + self.s
        if os.path.exists("properties/tool.txt"):
            tf = open("properties/tool.txt", "r")
            t = tf.read()
        else:
            tf = open("properties/tool.txt", "w")
            tf.write("brush")
            t = "brush"
        tf.close()
        self.getTool(t)
        if os.path.exists("properties/font.txt"):
            ft = open("properties/font.txt", "r")
            self.selectedFont = ft.read()
        else:
            ft = open("properties/font.txt", "w")
            ft.write("Times New Roman")
            self.selectedFont = "Times New Roman"
        if os.path.exists("properties/outline_color.txt"):
            oc = open("properties/outline_color.txt", "r")
            ocs = oc.read()
            if ocs == "None":
                self.noneOutlineSelected = True
                self.outline_color = self.white
            else:
                c = self.getColor(ocs)
                if c == self.white:
                    self.whiteOutlineSelected = True
                elif c == self.black:
                    self.blackOutlineSelected = True
                elif c == self.red:
                    self.redOutlineSelected = True
                elif c == self.orange:
                    self.orangeOutlineSelected = True
                elif c == self.lime:
                    self.limeOutlineSelected = True
                elif c == self.green:
                    self.greenOutlineSelected = True
                elif c == self.blue:
                    self.blueOutlineSelected = True
                elif c == self.teal:
                    self.tealOutlineSelected = True
                elif c == self.purple:
                    self.purpleOutlineSelected = True
                elif c == self.yellow:
                    self.yellowOutlineSelected = True
                self.outline_color = c
        self.screen.fill(self.fill)
        pygame.display.flip()
    #Setup application
    def setup(self):
        pygame.init() #Initialize pygame
        self.canContinue = False #declare the self.canContinue variable
        self.setupCursors() #Setup all the mouse cursors
        self.declareVar(False) #Declare variables before screen
        self.setupFonts()
        self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0) #Setup screen
        self.declareVar(True) #Declare variables after screen
        self.getProperties() #Get the property values
        self.gui(self.width, self.height) #Add gui
    #Redraw after fillscreen
    def redraw(self, h, p, c, s, t, f):
        #Incrementation values
        i = 0
        i_p = 0
        i_c = 0
        i_s = 0
        i_t = 0
        i_f = 0
        if self.opened: #If a file is opened
            self.screen.blit(pygame.image.load(self.opened_file),(30,60)) #Add file
        while i < len(self.history) and i_p < len(self.hist_points) and i_c < len(self.hist_color) and i_s < len(self.hist_size) and i_t < len(self.hist_text) and i_f < len(self.hist_font): #While the incr. values below length of arrays
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
            elif h[i] == "text":
                cf = pygame.font.SysFont(f[i_f], s[i_s], False, False)
                ct = cf.render(t[i_t], 1, c[i_c])
                self.screen.blit(ct, (p[i_p], p[i_p+1]))
                i_p += 2
                i_s += 1
            i_c += 1
            i += 1
            i_t += 1
            i_f += 1
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
        self.redraw(self.history, self.hist_points, self.hist_color, self.hist_size, self.hist_text, self.hist_font) #Redraw
    def getFontAtPos(self, p):
        i = 0
        while i < len(self.fontPositions):
            if self.fontPositions[i] == p:
                return self.fontNames[i]
            i += 1
    #Events
    def events(self):
        if self.arrowClicked: #If the color arrow is clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit Program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If the mouse is down
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = pygame.mouse.get_pos() #Get mouse position
                        if (xco not in range(80, 180) or yco not in range(54, 254)) or (xco in range(213,230) and yco in range(34,52)):
                            self.arrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            if xco in range(0,136) and yco in range(0,25):
                                self.fileClicked = True
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                            elif xco in range(self.fax,self.fax+17) and yco in range(34,52):
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
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
        elif self.fillArrowClicked: #If the fill arrow is clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If the mouse is down
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = pygame.mouse.get_pos() #Get mouse position
                        if (xco not in range(self.fx,self.fx+131) or yco not in range(54, 254)) or (xco in range(self.fax,self.fax+17) and yco in range(34,52)):
                            self.fillArrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            if xco in range(0,136) or yco in range(0,25):
                                self.fileClicked = True
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                            elif xco in range(213,230) and yco in range(34,52):
                                self.arrowClicked = True
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                        elif xco in range(self.fx,self.fx+131): #If within fill color options
                            self.fillScreen(yco) #Fill screen
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
        elif self.fileClicked: #If file menu button clicked
            for event in pygame.event.get():
                if event.type == QUIT: #If the X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If mouse is down
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = pygame.mouse.get_pos() #Get mouse position
                        if (xco not in range(0, 136) or yco not in range(0, 85)) or (xco in range(0,136) and yco in range(0,25)):
                            self.fileClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                            if xco in range(213,230) and yco in range(34,52):
                                self.arrowClicked = True
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                            elif xco in range(self.fax,self.fax+17) and yco in range(34,52):
                                self.fillArrowClicked = True
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                        if xco in range(0,136) and yco in range(25,45): #Save as
                            self.save_as()
                        elif xco in range(0,136) and yco in range(45,65): #Save
                            self.save()
                        elif xco in range(0,136) and yco in range(65,85): #Open
                            self.open_it()
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
        elif self.fontArrowClicked:
            for event in pygame.event.get():
                if event.type == QUIT: #If X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If mouse is down
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = event.pos
                        if xco in range(770, 787) and yco in range(34, 60):
                            self.screen.blit(pygame.image.load("gui/t_screen.png").convert_alpha(), (0,0))
                            self.fontArrowClicked = False
                        elif xco in range(565, 765) and yco in range(55, 175):
                            if yco in range(55, 75):
                                self.selectedFont = self.getFontAtPos(55)
                            elif yco in range(75, 95):
                                self.selectedFont = self.getFontAtPos(75)
                            elif yco in range(95, 115):
                                self.selectedFont = self.getFontAtPos(95)
                            elif yco in range(115, 135):
                                self.selectedFont = self.getFontAtPos(115)
                            elif yco in range(135, 155):
                                self.selectedFont = self.getFontAtPos(135)
                            elif yco in range(155, 175):
                                self.selectedFont = self.getFontAtPos(155)
                            self.screen.blit(pygame.image.load("gui/t_screen.png").convert_alpha(), (0,0))
                            self.fontArrowClicked = False
                        elif xco in range(765, 775):
                            if yco in range(75, 85):
                                self.scrollFontUp()
                            elif yco in range(155, 165):
                                self.scrollFontDown()
                            else:
                                self.screen.blit(pygame.image.load("gui/t_screen.png").convert_alpha(), (0,0))
                                self.fontArrowClicked = False
                        else:
                            self.screen.blit(pygame.image.load("gui/t_screen.png").convert_alpha(), (0,0))
                            self.fontArrowClicked = False
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
        elif self.outlineArrowClicked:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = event.pos
                        if xco in range(460,591):
                            if yco in range(54, 74):
                                self.whiteOutlineSelected = True
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.white
                            elif yco in range(75,94):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = True
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.black
                            elif yco in range(95,114):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = True
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.red
                            elif yco in range(115,134):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = True
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.orange
                            elif yco in range(135,154):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = True
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.lime
                            elif yco in range(155, 174):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = True
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.green
                            elif yco in range(175,194):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = True
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.blue
                            elif yco in range(195,214):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = True
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.teal
                            elif yco in range(215, 234):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = True
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.purple
                            elif yco in range(235, 254):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = True
                                self.noneOutlineSelected = False
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                                self.outline_color = self.yellow
                            elif yco in range(255, 274):
                                self.whiteOutlineSelected = False
                                self.blackOutlineSelected = False
                                self.redOutlineSelected = False
                                self.orangeOutlineSelected = False
                                self.limeOutlineSelected = False
                                self.greenOutlineSelected = False
                                self.blueOutlineSelected = False
                                self.tealOutlineSelected = False
                                self.purpleOutlineSelected = False
                                self.yellowOutlineSelected = False
                                self.noneOutlineSelected = True
                                self.outlineArrowClicked = False
                                self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                        if (xco not in range(460,591) or yco not in range(80,274)) or (xco in range(596,613) and yco in range(34,52)):
                            self.outlineArrowClicked = False
                            self.screen.blit(pygame.image.load("gui/menu_screen.png"), (0,0))
                elif event.type == VIDEORESIZE: #If screen resized
                        self.resizeScreen(event.size)
        elif self.typing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.shift = True
                    if event.key == K_a:
                        if self.shift:
                            self.text += 'A'
                        else:
                            self.text += 'a'
                    if event.key == K_b:
                        if self.shift:
                            self.text += 'B'
                        else:
                            self.text += 'b'
                    if event.key == K_c:
                        if self.shift:
                            self.text += 'C'
                        else:
                            self.text += 'c'
                    if event.key == K_d:
                        if self.shift:
                            self.text += 'D'
                        else:
                            self.text += 'd'
                    if event.key == K_e:
                        if self.shift:
                            self.text += 'E'
                        else:
                            self.text += 'e'
                    if event.key == K_f:
                        if self.shift:
                            self.text += 'F'
                        else:
                            self.text += 'f'
                    if event.key == K_g:
                        if self.shift:
                            self.text += 'G'
                        else:
                            self.text += 'g'
                    if event.key == K_h:
                        if self.shift:
                            self.text += 'H'
                        else:
                            self.text += 'h'
                    if event.key == K_i:
                        if self.shift:
                            self.text += 'I'
                        else:
                            self.text += 'i'
                    if event.key == K_j:
                        if self.shift:
                            self.text += 'J'
                        else:
                            self.text += 'j'
                    if event.key == K_k:
                        if self.shift:
                            self.text += 'K'
                        else:
                            self.text += 'k'
                    if event.key == K_l:
                        if self.shift:
                            self.text += 'L'
                        else:
                            self.text += 'l'
                    if event.key == K_m:
                        if self.shift:
                            self.text += 'M'
                        else:
                            self.text += 'm'
                    if event.key == K_n:
                        if self.shift:
                            self.text += 'N'
                        else:
                            self.text += 'n'
                    if event.key == K_o:
                        if self.shift:
                            self.text += 'O'
                        else:
                            self.text += 'o'
                    if event.key == K_p:
                        if self.shift:
                            self.text += 'P'
                        else:
                            self.text += 'p'
                    if event.key == K_q:
                        if self.shift:
                            self.text += 'Q'
                        else:
                            self.text += 'q'
                    if event.key == K_r:
                        if self.shift:
                            self.text += 'R'
                        else:
                            self.text += 'r'
                    if event.key == K_s:
                        if self.shift:
                            self.text += 'S'
                        else:
                            self.text += 's'
                    if event.key == K_t:
                        if self.shift:
                            self.text += 'T'
                        else:
                            self.text += 't'
                    if event.key == K_u:
                        if self.shift:
                            self.text += 'U'
                        else:
                            self.text += 'u'
                    if event.key == K_v:
                        if self.shift:
                            self.text += 'V'
                        else:
                            self.text += 'v'
                    if event.key == K_w:
                        if self.shift:
                            self.text += 'W'
                        else:
                            self.text += 'w'
                    if event.key == K_x:
                        if self.shift:
                            self.text += 'X'
                        else:
                            self.text += 'x'
                    if event.key == K_y:
                        if self.shift:
                            self.text += 'Y'
                        else:
                            self.text += 'y'
                    if event.key == K_z:
                        if self.shift:
                            self.text += 'Z'
                        else:
                            self.text += 'z'
                    if event.key == K_0 or event.key == K_KP0:
                        if self.shift:
                            self.text += ')'
                        else:
                            self.text += '0'
                    if event.key == K_1 or event.key == K_KP1:
                        if self.shift:
                            self.text += '!'
                        else:
                            self.text += '1'
                    if event.key == K_2 or event.key == K_KP2:
                        if self.shift:
                            self.text += '@'
                        else:
                            self.text += '2'
                    if event.key == K_3 or event.key == K_KP3:
                        if self.shift:
                            self.text += '#'
                        else:
                            self.text += '3'
                    if event.key == K_4 or event.key == K_KP4:
                        if self.shift:
                            self.text += '$'
                        else:
                            self.text += '4'
                    if event.key == K_5 or event.key == K_KP5:
                        if self.shift:
                            self.text += '%'
                        else:
                            self.text += '5'
                    if event.key == K_6 or event.key == K_KP6:
                        if self.shift:
                            self.text += '^'
                        else:
                            self.text += '6'
                    if event.key == K_7 or event.key == K_KP7:
                        if self.shift:
                            self.text += '&'
                        else:
                            self.text += '7'
                    if event.key == K_8 or event.key == K_KP8:
                        if self.shift:
                            self.text += '*'
                        else:
                            self.text += '8'
                    if event.key == K_9 or event.key == K_KP9:
                        if self.shift:
                            self.text += '('
                        else:
                            self.text += '9'
                    if event.key == K_MINUS or event.key == K_KP_MINUS:
                        if self.shift:
                            self.text += '_'
                        else:
                            self.text += '-'
                    if event.key == K_EQUALS:
                        if self.shift:
                            self.text += '+'
                        else:
                            self.text += '='
                    if event.key == K_BACKQUOTE:
                        if self.shift:
                            self.text += '~'
                        else:
                            self.text += '`'
                    if event.key == K_LEFTBRACKET:
                        if self.shift:
                            self.text += '{'
                        else:
                            self.text += '['
                    if event.key == K_RIGHTBRACKET:
                        if self.shift:
                            self.text += '}'
                        else:
                            self.text += ']'
                    if event.key == K_BACKSLASH:
                        if self.shift:
                            self.text += '|'
                        else:
                            self.text += '\\'
                    if event.key == K_SEMICOLON:
                        if self.shift:
                            self.text += ':'
                        else:
                            self.text += ';'
                    if event.key == K_QUOTE:
                        if self.shift:
                            self.text += '"'
                        else:
                            self.text += '\''
                    if event.key == K_COMMA:
                        if self.shift:
                            self.text += '<'
                        else:
                            self.text += ','
                    if event.key == K_PERIOD or event.key == K_KP_PERIOD:
                        if self.shift:
                            self.text += '>'
                        else:
                            self.text += '.'
                    if event.key == K_SLASH or event.key == K_KP_DIVIDE:
                        if self.shift:
                            self.text += '?'
                        else:
                            self.text += '/'
                    if event.key == K_KP_MULTIPLY:
                        self.text += '*'
                    if event.key == K_KP_PLUS:
                        self.text += '+'
                    if event.key == K_SPACE:
                        self.text += ' '
                    if event.key == K_BACKSPACE:
                        c = list(self.text)
                        self.text = ""
                        i = 0
                        while i < len(c)-1:
                            self.text += c[i]
                            i += 1
                    if event.key == K_RETURN:
                        self.history.append("text")
                        self.hist_points.append(self.points[0][0])
                        self.hist_points.append(self.points[0][1])
                        self.hist_text.append(self.text)
                        self.hist_font.append(self.selectedFont)
                        self.hist_color.append(self.color)
                        self.hist_size.append(self.s)
                        self.points = []
                        self.text = ""
                        self.typing = False
                elif event.type == KEYUP:
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        self.shift = False
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
        else: #Normal events
            for event in pygame.event.get():
                if event.type == QUIT: #If X is clicked
                    self.updateFiles() #Update files
                    pygame.quit() #Quit program
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN: #If mouse is down
                    (button1, button2, button3) = pygame.mouse.get_pressed()
                    if button1:
                        xco, yco = event.pos #Get the event position
                        if xco in range(30,self.width) and yco in range(60,self.height): #If in canvas
                            if self.saved: #If saved
                                self.saved = False #saved set to false
                                self.title = self.title + "*" #Add * to title to symbolize edit
                                pygame.display.set_caption(self.title)
                        elif xco in range(0, 50) and yco in range(0, 30): #File clicked
                            self.fileClicked = True
                            pygame.image.save(self.screen, "gui/menu_screen.png") #Save temporary image
                        #Drawing events
                        if self.rectClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.points.append(event.pos)
                            self.dragging = True
                        elif self.ellipseClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.points.append(event.pos)
                            self.dragging = True
                        elif self.brushClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.dragging = True
                            self.last_x = xco
                            self.last_y = yco
                            if self.mode == "square":
                                if self.s == 1:
                                    pygame.draw.circle(self.screen, self.color, (xco,yco), self.s/2)
                                else:
                                    pygame.draw.rect(self.screen, self.color, (xco-(self.s/2), yco-(self.s/2), self.s, self.s))
                            else:
                                pygame.draw.circle(self.screen, self.color, (xco,yco), self.s/2)
                        elif self.eraserClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.dragging = True
                            self.last_x = xco
                            self.last_y = yco
                            if self.mode == "square":
                                if self.s == 1:
                                    pygame.draw.circle(self.screen, self.fill, (xco,yco), self.s/2)
                                else:
                                    pygame.draw.rect(self.screen, self.fill, (xco-(self.s/2), yco-(self.s/2), self.s, self.s))
                            else:
                                pygame.draw.circle(self.screen, self.fill, (xco,yco), self.s/2)
                        elif self.lineClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.points.append(event.pos)
                            self.dragging = True
                        elif self.textClicked and xco not in range(0,30) and yco not in range(0,60):
                            self.points.append(event.pos)
                            pygame.image.save(self.screen, "gui/typing.png")
                            self.typing = True
                        #Tool changing events
                        elif xco in range(3, 30) and yco in range(120, 150): #Rectangle
                            self.rectClicked = True
                            self.brushClicked = False
                            self.eraserClicked = False
                            self.lineClicked = False
                            self.ellipseClicked = False
                            self.textClicked = False
                        elif xco in range(3,30) and yco in range(60, 87): #Brush
                            self.rectClicked = False
                            self.brushClicked = True
                            self.eraserClicked = False
                            self.lineClicked = False
                            self.ellipseClicked = False
                            self.textClicked = False
                        elif xco in range(3,30) and yco in range(90, 117): #Eraser
                            self.rectClicked = False
                            self.brushClicked = False
                            self.eraserClicked = True
                            self.lineClicked = False
                            self.ellipseClicked = False
                            self.textClicked = False
                        elif xco in range(3,30) and yco in range(150, 175): #Ellipse
                            self.rectClicked = False
                            self.brushClicked = False
                            self.eraserClicked = False
                            self.lineClicked = False
                            self.ellipseClicked = True
                            self.textClicked = False
                        elif xco in range(3,30) and yco in range(180, 206): #Line
                            self.rectClicked = False
                            self.brushClicked = False
                            self.eraserClicked = False
                            self.lineClicked = True
                            self.ellipseClicked = False
                            self.textClicked = False
                        elif xco in range(3,30) and yco in range(210,236): #Text
                            self.rectClicked = False
                            self.brushClicked = False
                            self.eraserClicked = False
                            self.lineClicked = False
                            self.ellipseClicked = False
                            self.textClicked = True
                        elif xco in range(213,230) and yco in range(34,52): #Color arrow clicked
                            if self.eraserClicked == False: #If eraser isn't selected
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                                self.arrowClicked = True
                        elif xco in range(596,613) and yco in range(34,52): #Outline arrow clicked
                            if self.rectClicked or self.ellipseClicked or self.lineClicked:
                                pygame.image.save(self.screen, "gui/menu_screen.png")
                                self.outlineArrowClicked = True
                        elif xco in range(self.fax,self.fax+17) and yco in range(34,52): #Fill arrow clicked
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
                            self.hist_text = []
                            self.hist_font = []
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
                            elif xco in range(168, 194) and yco in range(33,59): #Circle mode selected, change eraser
                                self.circleClicked = True
                                self.circleBrushClicked = True
                                self.squareClicked = False
                                self.squareBrushClicked = False
                                self.mode = "circle"
                        elif self.brushClicked: #If brush selected
                            if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
                                self.sh_moving = True
                            elif xco in range(350, 376) and yco in range(33,59): #Square mode selected, change brush
                                self.squareBrushClicked = True
                                self.squareClicked = True
                                self.circleBrushClicked = False
                                self.circleClicked = False
                                self.mode = "square"
                            elif xco in range(380,406) and yco in range(33,59): #Circle mode selected, change brush
                                self.circleBrushClicked = True
                                self.circleClicked = True
                                self.squareBrushClicked = False
                                self.squareClicked = False
                                self.mode = "circle"
                        elif self.lineClicked: #If line selected
                            if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
                                self.sh_moving = True
                        elif self.textClicked: #If text selected
                            if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
                                self.sh_moving = True
                            elif xco in range(770, 787) and yco in range(34, 60):
                                pygame.image.save(self.screen, "gui/t_screen.png")
                                self.fontArrowClicked = True
                        elif self.rectClicked: #If rectangle selected
                            if self.noneOutlineSelected == False:
                                if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
                                    self.sh_moving = True
                        elif self.ellipseClicked: #If ellipse selected
                            if self.noneOutlineSelected == False:
                                if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51): #slider handle clicked
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
                        self.hist_oc.append(self.rect_oc)
                        self.hist_os.append(self.rect_os)
                        self.hist_text.append("none")
                        self.hist_font.append("none")
                    elif self.ellipseClicked:
                        if self.ell_type != 2:
                            self.history.append("ellipse")
                            self.hist_points.append(self.point1)
                            self.hist_points.append(self.point2)
                            self.hist_size.append(self.rect_w)
                            self.hist_size.append(self.rect_h)
                            self.hist_color.append(self.rect_c)
                            self.hist_text.append("none")
                            self.hist_font.append("none")
                        else:
                            self.history.append("line")
                            self.hist_points.append(self.point1)
                            self.hist_points.append(self.point2)
                            self.hist_points.append(self.point3)
                            self.hist_points.append(self.point4)
                            self.hist_size.append(4)
                            self.hist_color.append(self.line_c)
                            self.hist_text.append("none")
                    elif self.lineClicked:
                        self.history.append("line")
                        self.hist_points.append(self.point1)
                        self.hist_points.append(self.point2)
                        self.hist_points.append(self.point3)
                        self.hist_points.append(self.point4)
                        self.hist_size.append(self.line_s)
                        self.hist_color.append(self.line_c)
                        self.hist_text.append("none")
                        self.hist_font.append("none")
                    #Reset draw points
                    self.point1 = 0
                    self.point2 = 0
                    self.point3 = 0
                    self.point4 = 0
                    self.rect_w = 0
                    self.rect_h = 0
                    self.line_s = 0
                elif event.type == VIDEORESIZE: #If screen resized
                    self.resizeScreen(event.size)
    def rect_drag(self): #Rectangle dragging
        if self.placed == True:
            self.screen.blit(self.scr, (0,0))
        else:
            self.screen.fill(self.fill)
        self.points.append(pygame.mouse.get_pos())
        pos2x = self.points[self.c][0] - self.points[0][0]
        pos2y = self.points[self.c][1] - self.points[0][1]
        if self.noneOutlineSelected == False:
            if pos2x > 0 and pos2y > 0:
                if pos2x > self.s and pos2y > self.s:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(self.points[0][0], self.points[0][1], pos2x, pos2y))
                    pygame.draw.rect(self.screen, self.color, Rect(self.points[0][0] + (self.s/2), self.points[0][1] + (self.s/2), pos2x - self.s, pos2y - self.s))
                else:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(self.points[0][0], self.points[0][1], pos2x, pos2y))
                self.point1 = self.points[0][0]
                self.point2 = self.points[0][1]
                self.rect_w = pos2x
                self.rect_h = pos2y
            elif pos2x < 0 and pos2y > 0:
                x = pos2x + self.points[0][0]
                y = self.points[0][1]
                w = self.points[0][0]-x
                h = pos2y
                if w > self.s and h > self.s:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                    pygame.draw.rect(self.screen, self.color, Rect(x + (self.s/2), y + (self.s/2), w - self.s, h - self.s))
                else:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                self.point1 = x
                self.point2 = y
                self.rect_w = w
                self.rect_h = h
            elif pos2x > 0 and pos2y < 0:
                x = self.points[0][0]
                y = pos2y + self.points[0][1]
                w = pos2x
                h = self.points[0][1]-y
                if w > self.s and h > self.s:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                    pygame.draw.rect(self.screen, self.color, Rect(x + (self.s/2), y + (self.s/2), w - self.s, h - self.s))
                else:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                self.point1 = x
                self.point2 = y
                self.rect_w = w
                self.rect_h = h
            elif pos2x < 0 and pos2y < 0:
                x = pos2x + self.points[0][0]
                y = pos2y + self.points[0][1]
                w = self.points[0][0]-x
                h = self.points[0][1]-y
                if w > self.s and h > self.s:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                    pygame.draw.rect(self.screen, self.color, Rect(x + (self.s/2), y + (self.s/2), w - self.s, h - self.s))
                else:
                    pygame.draw.rect(self.screen, self.outline_color, Rect(x,y,w,h))
                self.point1 = x
                self.point2 = y
                self.rect_w = w
                self.rect_h = h
        else:
            pygame.draw.rect(self.screen, self.color, Rect(self.points[0][0], self.points[0][1], pos2x, pos2y))
            self.point1 = self.points[0][0]
            self.point2 = self.points[0][1]
            self.rect_w = pos2x
            self.rect_h = pos2y
        self.rect_c = self.color
        self.rect_oc = self.outline_color
        self.rect_os = self.s
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
        if self.noneOutlineSelected == False:
            if rect_height < 0 and rect_width > 0:
                rect_corner = [self.points[0][0], self.points[self.c][1]]
                rect_bottom = [self.points[self.c][0], self.points[0][1]]
                rect_width = rect_bottom[0] - rect_corner[0]
                rect_height = rect_bottom[1] - rect_corner[1]
                if rect_width > self.s and rect_height > self.s:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((rect_corner),(rect_width,rect_height)))
                    pygame.draw.ellipse(self.screen, self.color, Rect((rect_corner[0]+(self.s/2),rect_corner[1]+(self.s/2)), (rect_width-self.s, rect_height-self.s)))
                else:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((rect_corner),(rect_width,rect_height)))
                self.point1 = rect_corner[0]
                self.point2 = rect_corner[1]
            elif rect_height < 0 and rect_width < 0:
                rect_width = self.points[0][0] - self.points[self.c][0]
                rect_height = self.points[0][1] - self.points[self.c][1]
                if rect_width > self.s and rect_height > self.s:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((self.points[self.c]), (rect_width, rect_height)))
                    pygame.draw.ellipse(self.screen, self.color, Rect((self.points[self.c][0]+(self.s/2), self.points[self.c][1]+(self.s/2)), (rect_width-self.s, rect_height-self.s)))
                else:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((self.points[self.c]), (rect_width, rect_height)))
                self.point1 = self.points[self.c][0]
                self.point2 = self.points[self.c][1]
            elif rect_height > 0 and rect_width < 0:
                rect_corner = [self.points[self.c][0], self.points[0][1]]
                rect_bottom = [self.points[0][0], self.points[self.c][1]]
                rect_width = rect_bottom[0] - rect_corner[0]
                rect_height = rect_bottom[1] - rect_corner[1]
                if rect_width > self.s and rect_height > self.s:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((rect_corner), (rect_width, rect_height)))
                    pygame.draw.ellipse(self.screen, self.color, Rect((rect_corner[0]+(self.s/2), rect_corner[1]+(self.s/2)), (rect_width-self.s, rect_height-self.s)))
                else:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((rect_corner), (rect_width, rect_height)))
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
                if rect_width > self.s and rect_height > self.s:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((self.points[0]), (rect_width, rect_height)))
                    pygame.draw.ellipse(self.screen, self.color, Rect((self.points[0][0]+(self.s/2), self.points[0][1]+(self.s/2)), (rect_width-self.s, rect_height-self.s)))
                else:
                    pygame.draw.ellipse(self.screen, self.outline_color, Rect((self.points[0]), (rect_width, rect_height)))
                self.point1 = self.points[0][0]
                self.point2 = self.points[0][1]
        else:
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
        end = pygame.mouse.get_pos()
        start = (self.last_x, self.last_y)
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            if self.mode == "square":
                if self.s == 1:
                    pygame.draw.circle(self.screen, self.color, (x, y), self.s/2)
                else:
                    pygame.draw.rect(self.screen, self.color, Rect(x-(self.s/2), y-(self.s/2), self.s, self.s))
                self.history.append("brush_square")
            else:
                pygame.draw.circle(self.screen, self.color, (x, y), self.s/2)
                self.history.append("brush_circle")
            self.hist_points.append(x)
            self.hist_points.append(y)
            self.hist_size.append(self.s)
            self.hist_color.append(self.color)
            self.hist_text.append("none")
            self.hist_font.append("none")
            self.last_x = x
            self.last_y = y
        pygame.display.flip()
    def eraser_drag(self): #Eraser dragging
        end = pygame.mouse.get_pos()
        start = (self.last_x, self.last_y)
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int( start[0]+float(i)/distance*dx)
            y = int( start[1]+float(i)/distance*dy)
            if self.mode == "square":
                if self.s == 1:
                    pygame.draw.circle(self.screen, self.fill, (x, y), self.s/2)
                else:
                    pygame.draw.rect(self.screen, self.fill, Rect(x-(self.s/2), y-(self.s/2), self.s, self.s))
                self.history.append("eraser_square")
            else:
                pygame.draw.circle(self.screen, self.fill, (x, y), self.s/2)
                self.history.append("eraser_circle")
            self.hist_points.append(x)
            self.hist_points.append(y)
            self.hist_size.append(self.s)
            self.hist_color.append(self.fill)
            self.hist_text.append("none")
            self.hist_font.append("none")
            self.last_x = x
            self.last_y = y
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
    def slider(self): #Slider
        if self.eraserClicked:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= 80 and mouse_x <= 129:
                self.slider_eraser_x = mouse_x
                self.slider_x = mouse_x + 207
            else:
                if mouse_x < 80:
                    self.slider_eraser_x = 80
                    self.slider_x = 287
                elif mouse_x > 129:
                    self.slider_eraser_x = 129
                    self.slider_x = 336
            self.s = self.slider_eraser_x - 79
            self.outline_s = self.slider_eraser_x -79
        else:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= 287 and mouse_x <= 336:
                self.slider_x = mouse_x
                self.slider_eraser_x = mouse_x - 207
            else:
                if mouse_x < 287:
                    self.slider_x = 287
                    self.slider_eraser_x = 80
                elif mouse_x > 336:
                    self.slider_x = 336
                    self.slider_eraser_x = 129
            self.s = self.slider_x - 286
            self.outline_s = self.slider_x - 286
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
        elif self.textClicked:
            return "text"
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
        bg = open("properties/bgColor.txt", "w")
        bg.write(self.colorToString(self.fill))
        bg.close()
        fg = open("properties/fgColor.txt", "w")
        fg.write(self.colorToString(self.color))
        fg.close()
        sh = open("properties/shape.txt", "w")
        sh.write(self.mode)
        sh.close()
        sz = open("properties/size.txt", "w")
        sz.write(str(self.s))
        sz.close()
        tl = open("properties/tool.txt", "w")
        tl.write(self.getToolString())
        tl.close()
        ft = open("properties/font.txt", "w")
        ft.write(self.selectedFont)
        ft.close()
        osf = open("properties/outline_size.txt", "w")
        osf.write(str(self.s))
        osf.close()
        self.oc = open("properties/outline_color.txt", "w")
        if self.noneOutlineSelected:
            self.oc.write("None")
        else:
            self.oc.write(self.colorToString(self.outline_color))
        self.oc.close()
        if os.path.exists("gui/fs_screen.png"):
            os.remove("gui/fs_screen.png")
        if os.path.exists("gui/menu_screen.png"):
            os.remove("gui/menu_screen.png")
        if os.path.exists("gui/screen.png"):
            os.remove("gui/screen.png")
        if os.path.exists("gui/t_screen.png"):
            os.remove("gui/t_screen.png")
        if os.path.exists("gui/typing.png"):
            os.remove("gui/typing.png")
    def update(self): #Delete existing java files
        if os.path.exists("javaTest.bat"):
            os.remove("javaTest.bat")
        if os.path.exists("jre-7u10-windows-i586-iftw.exe"):
            os.remove("jre-7u10-windows-i586-iftw.exe")
    def absval(self, val):
        if val < 0:
            val *= -1
        return val
    def elliptical_equation(self, a, b, h, k, x):
        y = []
        y.append((b * self.absval(math.sqrt(1-(float((x-h)**2)/float(a**2))))) + k)
        y.append(((-1 * b) * self.absval(math.sqrt(1-(float((x-h)**2)/float(a**2))))) + k)
        return y
    def inEllipse(self, a, b, h, k, x, y):
        #Precautions
        a = self.absval(a)
        b = self.absval(b)
        #Rectangle checks
        if x < (h-a) or x > (h+a) or y < (k-b) or y > (k+b):
            return False
        yval = self.elliptical_equation(a,b,h,k,x)
        if y >= yval[1] and y <= yval[0]:
            return True
        return False
    def notInBlackComp(self, xco, yco): #Mouse not in black
        if len(self.history) == 0:
            if self.fill == self.black or self.fill == self.blue:
                return "Nothing, dark"
            else:
                return "Nothing, light"
        i = len(self.history)-1
        i_p = len(self.hist_points)-1
        i_c = len(self.hist_color)-1
        i_s = len(self.hist_size)-1
        i_t = len(self.hist_text)-1
        i_f = len(self.hist_font)-1
        while i >= 0 and i_p >= 0 and i_c >= 0 and i_s >= 0 and i_t >= 0 and i_f >= 0:
            h = self.history
            p = self.hist_points
            c = self.hist_color
            s = self.hist_size
            if h[i] == "ellipse":
                if self.inEllipse(s[i_s-1]/2, s[i_s]/2, p[i_p-1]+(s[i_s-1]/2), p[i_p]+(s[i_s]/2), xco, yco):
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i -= 1
                i_p -= 2
                i_s -= 2
                i_c -= 1
            elif h[i] == "rect":
                if xco in range(p[i_p-1],p[i_p-1]+s[i_s-1]) and yco in range(p[i_p],p[i_p]+s[i_s]):
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i -= 1
                i_p -= 2
                i_s -= 2
                i_c -= 1
            elif h[i] == "line":
                #Unknown how to code line currently
                i -= 1
                i_p -= 4
                i_s -= 2
                i_c -= 1
            elif h[i] == "brush_square":
                if xco in range(p[i_p-1],p[i_p-1]+s[i_s]) and yco in range(p[i_p],p[i_p]+s[i_s]):
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i -= 1
                i_p -= 2
                i_s -= 1
                i_c -= 1
            elif h[i] == "brush_circle":
                if xco in range(p[i_p-1],p[i_p-1]+s[i_s]) and yco in range(p[i_p],p[i_p]+s[i_s]):
                    if c[i_c] == self.black or c[i_c] == self.blue:
                        return "Color dark"
                    else:
                        return "In range"
                i -= 1
                i_p -= 2
                i_s -= 1
                i_c -= 1
            elif h[i] == "eraser_square" or h[i] == "eraser_circle":
                if xco in range(p[i_p-1],p[i_p-1]+s[i_s]) and yco in range(p[i_p],p[i_p]+s[i_s]):
                    if self.fill == self.black or self.fill == self.blue:
                        return "Eraser dark"
                    else:
                        return "Eraser light"
                i -= 1
                i_p -= 2
                i_s -= 1
                i_c -= 1
            elif h[i] == "text":
                i -= 1
                i_p -= 2
                i_c -= 1
            i_t += 1
            i_f += 1
        if self.fill != self.black and self.fill != self.blue:
            return "Fill light, not in range"
        else:
            return "Fill dark, not in range"
    def notInBlack(self, xco, yco): #Convert string values from notInBlackComp(not in black compilation) to boolean
        xibc = self.notInBlackComp(xco,yco)
        if xibc == "Nothing, dark":
            return False
        elif xibc == "Nothing, light":
            return True
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
            if xco in range(0,30) or yco in range(0,60) or self.fileClicked or self.arrowClicked or self.fillArrowClicked or self.fontArrowClicked or self.outlineArrowClicked:
                pygame.mouse.set_cursor((16, 19), (0, 0),
                                        (128,0,192,0,160,0,144,0,136,0,132,0,130,0,129,0,128,128,128,64,128,32,128,16,129,240,137,0,148,128,164,128,194,64,2,64,1,128),
                                        (128,0,192,0,224,0,240,0,248,0,252,0,254,0,255,0,255,128,255,192,255,224,255,240,255,240,255,0,247,128,231,128,195,192,3,192,1,128))
            else:
                if self.notInBlack(xco, yco):
                    #Black cursors
                    if self.ellipseClicked or self.rectClicked or self.lineClicked:
                        pygame.mouse.set_cursor((8,8),(4,4),*self.xxcb)
                    elif self.textClicked:
                        pygame.mouse.set_cursor((16,16),(0,0),*self.xt16cb)
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
                            elif self.s == 25 or self.s == 26:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs26cb)
                            elif self.s == 27 or self.s == 28:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs28cb)
                            elif self.s == 29 or self.s == 30:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs30cb)
                            elif self.s == 31 or self.s == 32:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs32cb)
                            elif self.s == 33 or self.s == 34:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs34cb)
                            elif self.s == 35 or self.s == 36:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs36cb)
                            elif self.s == 37 or self.s == 38:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs38cb)
                            elif self.s == 39 or self.s == 40:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs40cb)
                            elif self.s == 41 or self.s == 42:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs42cb)
                            elif self.s == 43 or self.s == 44:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs44cb)
                            elif self.s == 45 or self.s == 46:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs46cb)
                            elif self.s == 47 or self.s == 48:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs48cb)
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
                            elif self.s == 25 or self.s == 26:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc26cb)
                            elif self.s == 27 or self.s == 28:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc28cb)
                            elif self.s == 29 or self.s == 30:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc30cb)
                            elif self.s == 31 or self.s == 32:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc32cb)
                            elif self.s == 33 or self.s == 34:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc34cb)
                            elif self.s == 35 or self.s == 36:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc36cb)
                            elif self.s == 37 or self.s == 38:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc38cb)
                            elif self.s == 39 or self.s == 40:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc40cb)
                            elif self.s == 41 or self.s == 42:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc42cb)
                            elif self.s == 43 or self.s == 44:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc44cb)
                            elif self.s == 45 or self.s == 46:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc46cb)
                            elif self.s == 47 or self.s == 48:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc48cb)
                            elif self.s == 49 or self.s == 50:
                                pygame.mouse.set_cursor((56,56),(28,28),*self.xc50cb)
                else:
                    #White cursors
                    if self.ellipseClicked or self.rectClicked or self.lineClicked:
                        pygame.mouse.set_cursor((8,8),(4,4),*self.xxcw)
                    elif self.textClicked:
                        pygame.mouse.set_cursor((16,16),(0,0),*self.xt16cw)
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
                            elif self.s == 25 or self.s == 26:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs26cw)
                            elif self.s == 27 or self.s == 28:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs28cw)
                            elif self.s == 29 or self.s == 30:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs30cw)
                            elif self.s == 31 or self.s == 32:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xs32cw)
                            elif self.s == 33 or self.s == 34:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs34cw)
                            elif self.s == 35 or self.s == 36:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs36cw)
                            elif self.s == 37 or self.s == 38:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs38cw)
                            elif self.s == 39 or self.s == 40:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xs40cw)
                            elif self.s == 41 or self.s == 42:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs42cw)
                            elif self.s == 43 or self.s == 44:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs44cw)
                            elif self.s == 45 or self.s == 46:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs46cw)
                            elif self.s == 47 or self.s == 48:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xs48cw)
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
                            elif self.s == 25 or self.s == 26:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc26cw)
                            elif self.s == 27 or self.s == 28:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc28cw)
                            elif self.s == 29 or self.s == 30:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc30cw)
                            elif self.s == 31 or self.s == 32:
                                pygame.mouse.set_cursor((32,32),(16,16),*self.xc32cw)
                            elif self.s == 33 or self.s == 34:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc34cw)
                            elif self.s == 35 or self.s == 36:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc36cw)
                            elif self.s == 37 or self.s == 38:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc38cw)
                            elif self.s == 39 or self.s == 40:
                                pygame.mouse.set_cursor((40,40),(20,20),*self.xc40cw)
                            elif self.s == 41 or self.s == 42:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc42cw)
                            elif self.s == 43 or self.s == 44:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc44cw)
                            elif self.s == 45 or self.s == 46:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc46cw)
                            elif self.s == 47 or self.s == 48:
                                pygame.mouse.set_cursor((48,48),(24,24),*self.xc48cw)
                            elif self.s == 49 or self.s == 50:
                                pygame.mouse.set_cursor((56,56),(28,28),*self.xc50cw)
    def getFontName(self, font):
        #Taken from: http://www.starrhorne.com/2012/01/18/how-to-extract-font-names-from-ttf-files-using-python-and-our-old-friend-the-command-line.html
        FONT_SPECIFIER_NAME_ID = 4
        FONT_SPECIFIER_FAMILY_ID = 1
        name = ""
        family = ""
        for record in font['name'].names:
            if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
                    if '\000' in record.string:
                            name = unicode(record.string, 'utf-16-be').encode('utf-8')
                    else:
                            name = record.string
            elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
                    if '\000' in record.string:
                            family = unicode(record.string, 'utf-16-be').encode('utf-8')
                    else:
                            family = record.string
            if name and family:
                    break
        return name, family
    def typer(self):
        self.screen.blit(pygame.image.load("gui/typing.png").convert_alpha(), (0,0))
        self.typePos = (self.points[0][0],self.points[0][1])
        self.font = pygame.font.SysFont(self.selectedFont, self.s, False, False)
        tr = self.font.render(self.text, 1, self.color)
        self.screen.blit(tr, self.typePos)
    def __init__(self):
        self.update()   #deletes possible existing update files
        self.setup()    #sets up everything for program
        i = 0
        while True:    #Holds program methods
            if self.canContinue:    #If mouse cursors completely initialized. They should be, but it just makes sure.
                self.updateMouse() #Update mouse cursors
                self.events()     #Program events
                if self.dragging == True:  #mouse dragging
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
                if self.typing == True:
                    self.typer()
                pygame.display.flip()         #Update screen
                if self.sh_moving == True:    #slider moving
                    self.slider()
                self.gui(self.width, self.height)   #Update gui
                pygame.display.flip()         #update screen again
main()    #initialize program
