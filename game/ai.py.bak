import pygame
import random
from math import *
from pygame.locals import *

class BasicAI(pygame.sprite.Sprite):
    def __init__(self, centerPoint, image, data):
	pygame.sprite.Sprite.__init__(self)
	self.image = image
	self.rect = image.get_rect()
	self.rect.center = centerPoint

	self.move_ai_data, self.fire_ai_data, self.health, self.end_level = data
	self.xMove,self.yMove = 0,0
	self.firing_timer = 0
	self.firing_timer_old = 0
	self.fire_timer = 0
	self.angle_timer = 0
	self.speed_timer = 0

	self.firing = False

	self.speed, self.speed_max, self.speed_factor, self.angle_max, self.angle, self.angle_factor, score_a = self.move_ai_data
	self.deathBlow, self.fire_max, self.firing_max, self.switch_back_point, self.fire_data, score_b, self.explode_data = self.fire_ai_data
	self.firing_interval = self.fire_data[5]
	self.firing_base_degree = self.fire_data[6]
	self.firing_degree_passed = self.firing_base_degree

	self.score = score_a + score_b

    def update(self):

	if self.firing == True:
	    self.firing_degree_passed += self.firing_interval
	    self.firing_timer += 1
	    if self.firing_timer - self.firing_timer_old == self.switch_back_point:
		self.firing_degree_passed = self.firing_base_degree
		self.firing_timer_old = self.firing_timer
	    if self.firing_timer == self.firing_max:
		self.firing = False
		self.firing_timer = 0
		self.firing_timer_old = 0
	    self.xMove = 0
	    self.yMove = 0
	else:

	    self.angle_timer += 1
	    self.fire_timer += 1
	    self.speed_timer += 1
	    self.angle += self.angle_factor
	    if self.speed_timer == self.speed_max:
		self.speed_factor = -self.speed_factor
		self.speed_timer = 0
	    if self.angle_timer == self.angle_max:
		self.angle_factor = -self.angle_factor
		self.angle_timer = 0
	    if self.fire_timer >= self.fire_max:
		self.firing = True
		self.fire_timer = 0
		self.fire_max += random.randint(-2,2)
		if self.fire_max < 10:
		    self.fire_max = 10

	    rotation = self.angle * (pi / 180)
	    self.xMove = cos(rotation) * self.speed
	    self.yMove = sin(rotation) * self.speed
	    self.rect.move_ip(self.xMove,self.yMove)
	    x,y,width,height = self.rect
	    if y > 1004 or y < -504 or x > 1004 or x < -504:
		self.kill()
