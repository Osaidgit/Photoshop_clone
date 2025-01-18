import pygame as pg
import random as ran
pg.init()

win = pg.display.set_mode((0,0),pg.RESIZABLE)
width,height = win.get_width(),win.get_height()
#COLORS
red,black,h_white,white,grey,blue,green=(250, 0,0),(0,0,0),(200,200,200),(255,255,255),(100,100,100),(0,0,255),(0,200,0)
#App colors
GREY = 168,195,242
PURPLE = 130,87,242
DARKBLUE = 87,193,242
SKYBLUE = 87,242,242
#_____________________________
fps = 30
clock = pg.time.Clock()
run = True
#  _____ FOR CIRCLE  ______##
cir_w,cir_h =100, 100
C_rect = pg.Rect(ran.randint(100,400), ran.randint(10, 400), cir_w,cir_h)
class Circle:
	def __init__(self):
		self.rect = C_rect
	def draw(self):
		pg.draw.circle(win,blue,(self.rect.center[0],self.rect.center[1]),cir_w // 2)
		pg.draw.rect(win,black,self.rect,2)
# ____ FOR TRIANGLE  ___ ##
class Triangle:
    def __init__(self):
        self.rect = pg.Rect(ran.randint(200, 500), ran.randint(10, 500), 100, 100)

    @property
    def points(self):
        """Calculate points dynamically based on the rectangle."""
        p1 = self.rect.centerx, self.rect.top  # Top center
        p2 = self.rect.left, self.rect.bottom  # Bottom left
        p3 = self.rect.right, self.rect.bottom  # Bottom right
        return [p1, p2, p3]

    def draw(self):
        pg.draw.polygon(win, red, self.points)  # Use dynamically calculated points
        pg.draw.rect(win, black,self.rect, 2)  # Draw the bounding rectangle

		
# ____ FOR HEXAGON _____ #
class Hexagon:
	def __init__(self):
		pass
# ______ PEN5AGON _______##
class Pentagon:
	def __init__(self):
		pass
	def draw(self):
		pass
# ____ FOR Ecllipse ______#

class Ecllipse:
	def __init__(self):
		pass
	def draw(self):
		pass
#____ FOR BOX ______#
bw,bh = 100,100
box = pg.Rect(ran.randint(100,400),ran.randint(100,400),bw,bh)

class Box:
	def __init__(self):
		self.box = box
	def draw(self):
		pg.draw.rect(win,green,self.box)

# ___ DEFAULT FUNCTIONS _#
font = pg.font.SysFont(None ,30)
text = font.render('pos: ',True, black)
def Show_pos():
	font = pg.font.SysFont(None, 30)
	pos =pg.mouse.get_pos()
	text1 = font.render(str(pos), True,red)
	win.blit(text1, (160,1210)),win.blit(text, (110,1210))
