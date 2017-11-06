#! /usr/bin/env python
import os, sys
import pygame
import random
from pygame.locals import *

def load_image_trans(name, colorkey=None):
	path = os.path.dirname(os.path.abspath(__file__)) + "/images/"+os.path.join(name)
	#message = 'Cannot load image:', path
	try:
		image = pygame.image.load(path)
	except (pygame.error, message):

		raise Exception(SystemExit, message)
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image

def get_rand_item(list):

	num = len(list) - 1
	itemNum = random.randint(0,num)
	return list[itemNum]
