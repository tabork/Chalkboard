#
#Chalkboard 2.1
#
#Expected Features:
#   Saving and loading images
#   Property saves
#
#--GUI repositioned
#--Need to design Menu pics at top
#
import pygame, sys, Tkinter, math, os, urllib
from pygame.locals import *
from Tkinter import *
class main:
    def declareVar(self, setup_true_false):
        if setup_true_false == False:
            self.icon = "gui\\icon.gif"
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
            self.brush_mode = "square"
            self.eraser_mode = "square"
            self.points=[]
            self.ls = 1
            self.c = 1
            self.es = 1
            self.bs = 1
            root = Tk()
            self.window_w = root.winfo_screenwidth()
            self.window_h = root.winfo_screenheight()
            if (float(self.window_w)/float(self.window_h)) == (16/9):
                self.width = 1280
                self.height = 720
            else:
                self.width = 1080
                self.height = 720
            self.dragging = False
            self.placed = False
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
            self.slider_x = 287
            self.slider_line_x = 287
            self.slider_eraser_x = 80
            self.sh_moving = False
            self.squareClicked = False
            self.circleClicked = False
            self.squareBrushClicked = False
            self.circleBrushClicked = False
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
        else:
            self.main_icon = pygame.image.load(self.icon).convert()
            pygame.display.set_icon(self.main_icon)
            pygame.display.set_caption("Chalkboard", "Chalkboard")
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
    def setClicked(self, bg):
        if bg:
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
        else:
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
        self.brush_mode = s
        self.eraser_mode = s
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
        self.ls = int(sz)
        self.es = int(sz)
        self.bs = int(sz)
        self.slider_x = 286 + self.bs
        self.slider_eraser_x = 79 + self.es
        self.slider_line_x = 286 + self.ls
        if os.path.exists("properties/tool.txt"):
            tf = open("properties/tool.txt", "r")
            t = tf.read()
        else:
            tf = open("properties/tool.txt", "w")
            tf.write("brush")
            t = "brush"
        tf.close()
        self.getTool(t)
        print(self.fill)
        self.screen.fill(self.fill)
        pygame.display.flip()
    def gui(self, width, height):
        pygame.display.flip()
        pygame.draw.rect(self.screen, (206,206,206), Rect(0,0,width,30))
        pygame.draw.rect(self.screen, (233,236,157), Rect(0,30,30,height))
        pygame.draw.rect(self.screen, (233,236,157), Rect(0,30,width,30))
        self.screen.blit(pygame.image.load("gui\\File.png").convert_alpha(), (5,5))
        if self.brushClicked == False:
            self.screen.blit(pygame.image.load("gui\\brush.png").convert_alpha(), (3,60))
        else:
            self.screen.blit(pygame.image.load("gui\\brush_clicked.png").convert_alpha(), (3,60))
            self.screen.blit(pygame.image.load("gui\\color_txt.png").convert_alpha(), (33,34))
            if self.whiteSelected:
                self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (80, 34))
            elif self.blackSelected:
                self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (80,34))
            elif self.redSelected:
                self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (80,34))
            elif self.orangeSelected:
                self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (80,34))
            elif self.limeSelected:
                self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (80,34))
            elif self.greenSelected:
                self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (80,34))
            elif self.blueSelected:
                self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (80,34))
            elif self.tealSelected:
                self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (80,34))
            elif self.purpleSelected:
                self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (80,34))
            elif self.yellowSelected:
                self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (80,34))
            self.screen.blit(pygame.image.load("gui\\arrow.png").convert_alpha(), (213,34))
            self.screen.blit(pygame.image.load("gui\\size_txt.png").convert_alpha(), (240, 35))
            self.screen.blit(pygame.image.load("gui\\slider.png").convert_alpha(), (290,38))
            self.screen.blit(pygame.image.load("gui\\slider_handle.png").convert_alpha(), (self.slider_x, 44))
            if self.squareBrushClicked:
                self.screen.blit(pygame.image.load("gui\\square_clicked.png").convert_alpha(), (350, 33))
            else:
                self.screen.blit(pygame.image.load("gui\\square.png").convert_alpha(), (350,33))
            if self.circleBrushClicked:
                self.screen.blit(pygame.image.load("gui\\circle_clicked.png").convert_alpha(), (380, 33))
            else:
                self.screen.blit(pygame.image.load("gui\\circle.png").convert_alpha(), (380, 33))
        if self.eraserClicked == False:
            self.screen.blit(pygame.image.load("gui\\eraser.png").convert_alpha(), (3, 90))
        else:
            self.screen.blit(pygame.image.load("gui\\eraser_clicked.png").convert_alpha(), (3, 90))
            self.screen.blit(pygame.image.load("gui\\size_txt.png").convert_alpha(), (33, 35))
            self.screen.blit(pygame.image.load("gui\\slider.png").convert_alpha(), (83,38))
            self.screen.blit(pygame.image.load("gui\\slider_handle.png").convert_alpha(), (self.slider_eraser_x, 44))
            if self.squareClicked:
                self.screen.blit(pygame.image.load("gui\\square_clicked.png").convert_alpha(), (138, 33))
            else:
                self.screen.blit(pygame.image.load("gui\\square.png").convert_alpha(), (138,33))
            if self.circleClicked:
                self.screen.blit(pygame.image.load("gui\\circle_clicked.png").convert_alpha(), (168, 33))
            else:
                self.screen.blit(pygame.image.load("gui\\circle.png").convert_alpha(), (168, 33))
        if self.rectClicked == False:
            self.screen.blit(pygame.image.load("gui\\rectangle.png").convert_alpha(), (3,120))
        else:
            self.screen.blit(pygame.image.load("gui\\rectangle_clicked.png").convert_alpha(), (3,120))
            self.screen.blit(pygame.image.load("gui\\color_txt.png").convert_alpha(), (33,34))
            if self.whiteSelected:
                self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (80, 34))
            elif self.blackSelected:
                self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (80,34))
            elif self.redSelected:
                self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (80,34))
            elif self.orangeSelected:
                self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (80,34))
            elif self.limeSelected:
                self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (80,34))
            elif self.greenSelected:
                self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (80,34))
            elif self.blueSelected:
                self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (80,34))
            elif self.tealSelected:
                self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (80,34))
            elif self.purpleSelected:
                self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (80,34))
            elif self.yellowSelected:
                self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (80,34))
            self.screen.blit(pygame.image.load("gui\\arrow.png").convert_alpha(), (213,34))
        if self.ellipseClicked == False:
            self.screen.blit(pygame.image.load("gui\\ellipse.png").convert_alpha(), (3,150))
        else:
            self.screen.blit(pygame.image.load("gui\\ellipse_clicked.png").convert_alpha(), (3,150))
            self.screen.blit(pygame.image.load("gui\\color_txt.png").convert_alpha(), (33,34))
            if self.whiteSelected:
                self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (80, 34))
            elif self.blackSelected:
                self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (80,34))
            elif self.orangeSelected:
                self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (80,34))
            elif self.redSelected:
                self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (80,34))
            elif self.limeSelected:
                self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (80,34))
            elif self.greenSelected:
                self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (80,34))
            elif self.blueSelected:
                self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (80,34))
            elif self.tealSelected:
                self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (80,34))
            elif self.purpleSelected:
                self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (80,34))
            elif self.yellowSelected:
                self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (80,34))
            self.screen.blit(pygame.image.load("gui\\arrow.png").convert_alpha(), (213,34))
        if self.lineClicked == False:
            self.screen.blit(pygame.image.load("gui\\line.png").convert_alpha(), (3, 180))
        else:
            self.screen.blit(pygame.image.load("gui\\line_clicked.png").convert_alpha(), (3,180))
            self.screen.blit(pygame.image.load("gui\\color_txt.png").convert_alpha(), (33,34))
            if self.whiteSelected:
                self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (80, 34))
            elif self.blackSelected:
                self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (80,34))
            elif self.orangeSelected:
                self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (80,34))
            elif self.redSelected:
                self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (80,34))
            elif self.limeSelected:
                self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (80,34))
            elif self.greenSelected:
                self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (80,34))
            elif self.blueSelected:
                self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (80,34))
            elif self.tealSelected:
                self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (80,34))
            elif self.purpleSelected:
                self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (80,34))
            elif self.yellowSelected:
                self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (80,34))
            self.screen.blit(pygame.image.load("gui\\arrow.png").convert_alpha(), (213,34))
            self.screen.blit(pygame.image.load("gui\\size_txt.png").convert_alpha(), (240, 35))
            self.screen.blit(pygame.image.load("gui\\slider.png").convert_alpha(), (290,38))
            self.screen.blit(pygame.image.load("gui\\slider_handle.png").convert_alpha(), (self.slider_line_x, 44))
        self.screen.blit(pygame.image.load("gui\\fill_txt.png").convert_alpha(), (450, 33))
        if self.blackFillSelected:
            self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (540,34))
        elif self.whiteFillSelected:
            self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (540,34))
        elif self.redFillSelected:
            self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (540,34))
        elif self.limeFillSelected:
            self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (540,34))
        elif self.greenFillSelected:
            self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (540,34))
        elif self.orangeFillSelected:
            self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (540,34))
        elif self.blueFillSelected:
            self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (540,34))
        elif self.yellowFillSelected:
            self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (540,34))
        elif self.tealFillSelected:
            self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (540,34))
        elif self.purpleFillSelected:
            self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (540,34))
        self.screen.blit(pygame.image.load("gui\\arrow.png").convert_alpha(), (673, 34))
        self.screen.blit(pygame.image.load("gui\\clear.png").convert_alpha(), (self.cx,34))
        if self.arrowClicked:
            self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (80,54))
            self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (80,74))
            self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (80,94))
            self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (80,114))
            self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (80,134))
            self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (80,154))
            self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (80,174))
            self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (80,194))
            self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (80,214))
            self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (80, 234))
        if self.fillArrowClicked:
            self.screen.blit(pygame.image.load("gui\\white_box.png").convert_alpha(), (540,54))
            self.screen.blit(pygame.image.load("gui\\black_box.png").convert_alpha(), (540,74))
            self.screen.blit(pygame.image.load("gui\\red_box.png").convert_alpha(), (540,94))
            self.screen.blit(pygame.image.load("gui\\orange_box.png").convert_alpha(), (540,114))
            self.screen.blit(pygame.image.load("gui\\lime_box.png").convert_alpha(), (540,134))
            self.screen.blit(pygame.image.load("gui\\green_box.png").convert_alpha(), (540,154))
            self.screen.blit(pygame.image.load("gui\\blue_box.png").convert_alpha(), (540,174))
            self.screen.blit(pygame.image.load("gui\\teal_box.png").convert_alpha(), (540,194))
            self.screen.blit(pygame.image.load("gui\\purple_box.png").convert_alpha(), (540,214))
            self.screen.blit(pygame.image.load("gui\\yellow_box.png").convert_alpha(), (540, 234))
        pygame.display.flip()
    def setup(self):
        pygame.init()
        self.declareVar(False)
        self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0)
        self.declareVar(True)
        self.getProperties()
        self.gui(self.width, self.height)
    def redraw(self, h, p, c, s):
        i = 0
        i_p = 0
        i_c = 0
        i_s = 0
        while i < len(self.history) and i_p < len(self.hist_points) and i_c < len(self.hist_color) and i_s < len(self.hist_size):
            h = self.history
            p = self.hist_points
            c = self.hist_color
            s = self.hist_size
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
    def fillScreen(self, yco):
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
            self.fill = self.yellow
            self.screen.fill(self.fill)
        self.redraw(self.history, self.hist_points, self.hist_color, self.hist_size)
    def events(self):
        if self.arrowClicked:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.updateFiles()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    xco, yco = pygame.mouse.get_pos()
                    if (xco not in range(80, 180) or yco not in range(54, 254)) or (xco in range(213,230) and yco in range(34,52)):
                        self.arrowClicked = False
                        self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
                    elif xco in range(80,180):
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
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
                            self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
                            self.color = self.yellow
                            self.changeBrush()
        elif self.fillArrowClicked:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.updateFiles()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    xco, yco = pygame.mouse.get_pos()
                    if (xco not in range(540, 640) or yco not in range(54, 254)) or (xco in range(673,690) and yco in range(34,52)):
                        self.fillArrowClicked = False
                        self.screen.blit(pygame.image.load("gui\\menu_screen.png"), (0,0))
                    elif xco in range(540,640):
                        self.fillScreen(yco)
        elif self.fileClicked:
            self.fileClicked = False
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.updateFiles()
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    xco, yco = event.pos
                    if xco in range(0, 50) and yco in range(0, 30):
                        self.fileClicked = True
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
                    elif xco in range(3, 30) and yco in range(120, 150):
                        self.rectClicked = True
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(60, 87):
                        self.rectClicked = False
                        self.brushClicked = True
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(90, 117):
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = True
                        self.lineClicked = False
                        self.ellipseClicked = False
                    elif xco in range(3,30) and yco in range(150, 175):
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = False
                        self.ellipseClicked = True
                    elif xco in range(3,30) and yco in range(180, 206):
                        self.rectClicked = False
                        self.brushClicked = False
                        self.eraserClicked = False
                        self.lineClicked = True
                        self.ellipseClicked = False
                    elif xco in range(213,230) and yco in range(34,52):
                        pygame.image.save(self.screen, "gui\\menu_screen.png")
                        self.arrowClicked = True
                    elif xco in range(673,690) and yco in range(34,52):
                        pygame.image.save(self.screen, "gui\\menu_screen.png")
                        self.fillArrowClicked = True
                    elif xco in range(self.cx,self.cx+50) and yco in range(34,54):
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
                        self.screen.fill(self.fill)
                    elif self.eraserClicked:
                        if xco in range(self.slider_eraser_x, self.slider_eraser_x + 9) and yco in range(44, 51):
                            self.sh_moving = True
                        elif xco in range(138, 164) and yco in range(33,59):
                            self.squareClicked = True
                            self.circleClicked = False
                            self.eraser_mode = "square"
                            self.changeEraser()
                        elif xco in range(168, 194) and yco in range(33,59):
                            self.circleClicked = True
                            self.squareClicked = False
                            self.eraser_mode = "circle"
                            self.changeEraser()
                    elif self.brushClicked:
                        if xco in range(self.slider_x, self.slider_x + 9) and yco in range(44, 51):
                            self.sh_moving = True
                        elif xco in range(350, 376) and yco in range(33,59):
                            self.squareBrushClicked = True
                            self.circleBrushClicked = False
                            self.brush_mode = "square"
                            self.changeBrush()
                        elif xco in range(380,406) and yco in range(33,59):
                            self.circleBrushClicked = True
                            self.squareBrushClicked = False
                            self.brush_mode = "circle"
                            self.changeBrush()
                    elif self.lineClicked:
                        if xco in range(self.slider_line_x, self.slider_line_x + 9) and yco in range(44, 51):
                            self.sh_moving = True
                    
                elif event.type == MOUSEBUTTONUP:
                    self.dragging = False
                    self.sh_moving = False
                    self.placed = True
                    self.points = []
                    self.c = 1
                    pygame.image.save(self.screen, "gui\\screen.png")
                    self.scr = pygame.image.load("gui\\screen.png").convert_alpha()
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
                    self.point1 = 0
                    self.point2 = 0
                    self.point3 = 0
                    self.point4 = 0
                    self.rect_w = 0
                    self.rect_h = 0
                    self.line_s = 0
                elif event.type == VIDEORESIZE:
                    pygame.image.save(self.screen,"gui\\fs_screen.png")
                    self.screen = pygame.display.set_mode(event.size, RESIZABLE, 0)
                    pygame.display.flip()
                    self.width, self.height = event.size
                    if self.width < self.window_w/2:
                        self.cx = self.window_w/2-70
                        self.cx = int(self.cx)
                        self.width = self.window_w/2;
                        self.screen = pygame.display.set_mode((self.width,self.height), RESIZABLE, 0)
                    elif self.width < 1080:
                        self.cx = self.width*.90
                        self.cx = int(math.floor(self.cx))
                    else:
                        self.cx = self.width*0.75
                        self.cx = math.floor(self.cx)
                        self.cx = int(self.cx)
                    if self.height < 185:
                        self.height = 185
                        self.screen = pygame.display.set_mode((self.width,self.height),RESIZABLE,0)
                    self.gui(self.width, self.height)
                    self.screen.fill(self.fill)
                    self.screen.blit(pygame.image.load("gui\\fs_screen.png").convert_alpha(),(0,0))
    def rect_drag(self):
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
    def ellipse_drag(self):
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
    def brush_drag(self):
        x, y = pygame.mouse.get_pos()
        if self.brush_mode == "square":
            if self.bs == 1:
                pygame.draw.circle(self.screen,self.color,(x,y),self.bs/2)
            else:
                x -= self.bs/2
                y -= self.bs/2
                pygame.draw.rect(self.screen, self.color, Rect(x, y, self.bs, self.bs))
            self.history.append("brush_square")
        elif self.brush_mode == "circle":
            pygame.draw.circle(self.screen, self.color,(x,y),self.bs/2)
            self.history.append("brush_circle")
        self.hist_points.append(x)
        self.hist_points.append(y)
        self.hist_color.append(self.color)
        self.hist_size.append(self.bs)
        pygame.display.flip()
    def eraser_drag(self):
        x, y = pygame.mouse.get_pos()
        if self.eraser_mode == "square":
            if self.es == 1:
                pygame.draw.circle(self.screen,self.fill,(x,y),self.es/2)
            else:
                x -= self.es/2
                y -= self.es/2
                pygame.draw.rect(self.screen, self.fill, Rect(x, y, self.es, self.es))
            self.history.append("eraser_square")
        elif self.eraser_mode == "circle":
            pygame.draw.circle(self.screen, self.fill,(x,y),self.es/2)
            self.history.append("eraser_circle")
        self.hist_points.append(x)
        self.hist_points.append(y)
        self.hist_size.append(self.es)
        self.hist_color.append(self.fill)
        pygame.display.flip()
    def line_drag(self):
        if self.placed == True:
            self.screen.blit(self.scr, (0,0))
        else:
            self.screen.fill(self.fill)
        self.points.append(pygame.mouse.get_pos())
        pygame.draw.line(self.screen, self.color, self.points[0], self.points[self.c], self.ls)
        self.point1 = self.points[0][0]
        self.point2 = self.points[0][1]
        self.point3 = self.points[self.c][0]
        self.point4 = self.points[self.c][1]
        self.line_s = self.ls
        self.line_c = self.color
        self.c += 1
        pygame.display.flip()
    def changeEraser(self):
        self.es = self.slider_eraser_x - 79
    def eraserSlider(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 80 and mouse_x <= 129:
            self.slider_eraser_x = mouse_x
        else:
            if mouse_x < 80:
                self.slider_eraser_x = 80
            elif mouse_x > 129:
                self.slider_eraser_x = 129
        self.changeEraser()
    def changeBrush(self):
        self.bs = self.slider_x - 286
    def changeLine(self):
        self.ls = self.slider_line_x - 286
    def lineSlider(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 287 and mouse_x <= 336:
            self.slider_line_x = mouse_x
        else:
            if mouse_x < 287:
                self.slider_line_x = 287
            elif mouse_x > 336:
                self.slider_line_x = 336
        self.changeLine()
    def brushSlider(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= 287 and mouse_x <= 336:
            self.slider_x = mouse_x
        else:
            if mouse_x < 287:
                self.slider_x = 287
            elif mouse_x > 336:
                self.slider_x = 336
        self.changeBrush()
    def getToolString(self):
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
    def colorToString(self, clr):
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
    def updateFiles(self):
        self.bg = open("properties/bgColor.txt", "w")
        self.bg.write(self.colorToString(self.fill))
        self.bg.close()
        self.fg = open("properties/fgColor.txt", "w")
        self.fg.write(self.colorToString(self.color))
        self.fg.close()
        self.sh = open("properties/shape.txt", "w")
        self.sh.write(self.brush_mode)
        self.sh.close()
        self.sz = open("properties/size.txt", "w")
        self.sz.write(str(self.bs))
        self.sz.close()
        self.tl = open("properties/tool.txt", "w")
        self.tl.write(self.getToolString())
        self.tl.close()
    def __init__(self):
        self.setup()
        while True:
            pygame.display.flip()
            self.events()
            if self.dragging == True:
                if self.rectClicked:
                    self.rect_drag()
                elif self.ellipseClicked:
                    self.ellipse_drag()
                elif self.brushClicked:
                    self.brush_drag()
                elif self.eraserClicked:
                    self.eraser_drag()
                elif self.lineClicked:
                    self.line_drag()
            pygame.display.flip()
            if self.sh_moving == True:
                if self.eraserClicked:
                    self.eraserSlider()
                elif self.brushClicked:
                    self.brushSlider()
                elif self.lineClicked:
                    self.lineSlider()
            self.gui(self.width, self.height)
            pygame.display.flip()
main()
