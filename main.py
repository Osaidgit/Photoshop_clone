import unittest
import pygame as pg
from App import *

app = Main()
while run:	
	app.draw()
	app.check_events()
	app.update()
	

if __name__ == '__main__':
	Main()

