import pygame as pg
from func import *

class Main:
	def __init__(self):
		self.menu = Menu()
		self.page = Page()
		self.exit = Exit()
		self.shape = Shapes()
		#-----------------
		self.draw_rect=False
		self.draw_circle = False
		self.draw_box = False
		self.draw_Tri = False
		#
		self.intro = False
		self.drag =False
		self.select = False
		self.run = True	
		self.is_dragging = False	
	#_________________________
	def check_events(self):
		show_boundary()
		#__Method variables
		self.pos = pg.mouse.get_pos()
		for i in pg.event.get():
			if i.type == pg.QUIT:
				self.run = False
			#__OTHER BUTTONS ____##
			if i.type == pg.MOUSEBUTTONDOWN:
				self.pos
				exit(self.pos,self.run)
			#___MENU AND CONTROLS  _____ ##
			#For btn1
			if self.menu.btn1.collidepoint(self.pos):
				self.draw_box= True
			#For Butn2
			if self.menu.btn2.collidepoint(self.pos):
				print("btn2")
				self.draw_circle = True
			# For btn3
			if self.menu.btn3.collidepoint(self.pos):
				print("btn3")
				self.draw_Tri = True
			#______________________
			
			#__ELEMENTS CONTRLING LOGIC
			#__ FOR Deselection_ #
			if i.type == pg.MOUSEBUTTONUP:
				self.is_dragging = False
				self.move_circle = False
				self.move_box = False
				self.move_tri = False
			#__ FOR Selection _____#	
			if i.type == pg.MOUSEBUTTONDOWN:
				self.pos
				if self.shape.circle.rect.collidepoint(self.pos):
					self.is_dragging = True
					self.move_circle = True
				elif self.shape.box.box.collidepoint(self.pos):
					self.is_dragging = True
					self.move_box = True
				elif self.shape.tri.rect.collidepoint(self.pos):
					self.is_dragging = True
					self.move_tri= True
			#_______________________						
			# __ FOR DRAGGING ELEMENTS ___ #		
			if self.is_dragging and self.move_circle:
				if i.type == pg.MOUSEMOTION:
					self.shape.circle.rect.center = self.pos		
			if self.is_dragging and self.move_box:
				if i.type == pg.MOUSEMOTION:
					self.shape.box.box.center = self.pos
			if self.is_dragging and self.move_tri:
				if i.type == pg.MOUSEMOTION:
					self.shape.tri.rect.center = self.pos
			
	def draw(self):
		win.fill(GREY)	
		self.page.draw()
		self.menu.draw()	
		Show_pos()
		self.exit.draw()
		if self.draw_Tri:
			self.shape.tri.draw()
		if self.draw_circle:
				self.shape.circle.draw()
		if self.draw_box:
				self.shape.box.draw()
						
	def update(self):
		print(clock.get_fps())	
		pg.display.update(),clock.tick(fps)
	
