import pygame
import random
from math import *
from pygame.locals import *

import ai

class Sprite(pygame.sprite.Sprite):

    def __init__(self, centerPoint, image):
	pygame.sprite.Sprite.__init__(self)
	self.image = image
	self.rect = image.get_rect()
	self.rect.center = centerPoint

class Object(Sprite):
    def __init__(self, centerPoint, image):
	Sprite.__init__(self, centerPoint, image)

    def update(self, xMove=0, yMove=0):

	self.rect.move_ip(xMove,yMove)

class Bullet(Sprite):
    def __init__(self, centerPoint, image, angle, data):
	Sprite.__init__(self, centerPoint, image)
	self.dam, self.speed, angleFactor, self.speedFactor, self.charge, self.homing, self.spin = data
	self.stored_rotation = 0
	if angleFactor != 0:
	    factorA,factorB = angleFactor
	    factor = random.randint(factorA,factorB)
	else:
	    factor = 0
	float(factor)
	self.angleFactor = factor
	self.angle = angle
	rotation = self.angle * (pi / 180)
	self.xMove = cos(rotation) * self.speed
	self.yMove = sin(rotation) * self.speed
	self.image_base = self.image

    def update(self, target):

	if self.homing == 0:
	    self.angle += self.angleFactor
	else:
	    if target != None:
		m = target
		x,y,w,h = self.rect
		x += w / 2
		y += h / 2
		mx,my,mw,mh = m.rect
		mx += mw / 2
		my += mh / 2
		if x < mx and self.angle < -70:
		    self.angle += self.homing
		elif x > mx and self.angle > -110:
		    self.angle -= self.homing

	if self.spin != 0:
	    self.stored_rotation += self.spin
	    self.image = pygame.transform.rotate(self.image_base, self.stored_rotation)
	else:
	    imgRotation = ((self.angle * -1) - 90)
	    self.image = pygame.transform.rotate(self.image_base, imgRotation)

	self.speed += self.speedFactor
	x,y,w,h = self.rect
	if y > 1004 or y < -504 or x > 1004 or x < -504:
	    self.kill()
	if self.speed <= 0:
	    self.kill()
	rotation = self.angle * (pi / 180)
	self.xMove = cos(rotation) * self.speed
	self.yMove = sin(rotation) * self.speed
	self.rect.move_ip(self.xMove,self.yMove)


class monsterBullet(Sprite):
    def __init__(self, centerPoint, image, angle, data):
	Sprite.__init__(self, centerPoint, image)
	self.image_base = image
	self.dam, self.speed, self.angleFactor, self.speedFactor, self.dirChangePoint, self.dirChangeFactor, self.dirChangeTime, self.spin = data
	self.stored_spin = 0
	self.dir_change_point_timer = 0
	self.dir_change_timer = 0
	self.dir_change = False
	self.angle = angle
	rotation = self.angle * (pi / 180)
	self.xMove = cos(rotation) * self.speed
	self.yMove = sin(rotation) * self.speed

    def update(self):

	self.image = self.image_base
	if self.dir_change == True:
	    self.dir_change_timer += 1
	    angleFactor = self.angleFactor + self.dirChangeFactor
	    if self.dir_change_timer == self.dirChangeTime:
		self.dir_change = False
		self.dir_change_timer = 0
	else:
	    angleFactor = self.angleFactor
	    self.dir_change_point_timer += 1
	    if self.dir_change_point_timer == self.dirChangePoint:
		self.dir_change = True
		self.dir_change_point_timer = 0

	if angleFactor != 0 and self.spin == 0:
	    imgRotation = ((self.angle * -1) + 90)
	    self.image = pygame.transform.rotate(self.image_base, imgRotation)
	elif self.spin != 0:
	    imgRotation = ((self.stored_spin) + 90)
	    self.image = pygame.transform.rotate(self.image_base, imgRotation)
	    self.stored_spin += self.spin
	    self.spin = self.spin * self.speedFactor

	self.angle = self.angle + angleFactor
	self.speed = self.speed * self.speedFactor
	x,y,w,h = self.rect
	if y > 1004 or y < -504 or x > 1004 or x < -504:
	    self.kill()
	if self.speed < 1:
	    self.kill()
	elif self.speed >= h:
	    self.speed = h
	rotation = self.angle * (pi / 180)
	self.xMove = cos(rotation) * self.speed
	self.yMove = sin(rotation) * self.speed
	self.rect.move_ip(self.xMove,self.yMove)


class Monster(ai.BasicAI):
    def __init__(self, centerPoint, image, data):
	ai.BasicAI.__init__(self, centerPoint, image, data)
	self.dying = False
	self.giving_charge_points = False

    def update(self, bullets):
	ai.BasicAI.update(self)
	self.rect.move_ip(self.xMove,self.yMove)
	for b in pygame.sprite.spritecollide(self, bullets, False):
	    self.health = self.health - b.dam
	    if b.charge == False:
		self.giving_charge_points = True
	    b.kill()
	    if self.health < 1:
		self.dying = True

class Shield(Sprite):

    def __init__(self, centerPoint, image, data):
	Sprite.__init__(self, centerPoint, image)
	self.health, self.life_timer_max = data
	self.life_timer = 0

    def update(self, bullet_group_a, bullet_group_b):

	self.life_timer += 1
	if self.life_timer == self.life_timer_max:
	    self.kill()

	for b in pygame.sprite.spritecollide(self, bullet_group_a, False):
	    self.health -= b.dam
	    b.kill()
	for b in pygame.sprite.spritecollide(self, bullet_group_b, False):
	    self.health -= b.dam
	    b.kill()

	if self.health < 1:
	    self.kill()

class Hitbox(Sprite):

    def __init__(self, centerPoint, image, data):
	Sprite.__init__(self, centerPoint, image)
	self.xMove, self.yMove = 0,0
	self.xPub, self.yPub = self.xMove, self.yMove
	self.x_dist, self.y_dist, self.health, self.stamina_gain, self.stamina_loss, self.bullet_data, self.charge_speed, self.charge_bullet_data, self.shield_cost, self.shield_gain, self.shield_data, self.delay_bullets = data
	self.facing = 2
	self.dam = self.bullet_data[3]
	self.stamina_max = 100
	self.shield_max = 100
	self.charge_max = 100
	self.charge = 0
	self.stamina = self.stamina_max
	self.shield = self.shield_max
	self.firing = False
	self.stamina_out = False
	self.moveable = False

    def update(self, vert_walls, hori_walls, bullets):

	if self.moveable == True:
	    self.xPub,self.yPub = self.xMove,self.yMove
	    self.rect.move_ip(self.xMove,self.yMove)

	if pygame.sprite.spritecollideany(self, vert_walls):
	     self.rect.move_ip(-self.xMove,0)
	     self.xPub = 0
	if pygame.sprite.spritecollideany(self, hori_walls):
	    self.rect.move_ip(0,-self.yMove)
	    self.yPub = 0

	if self.xMove == 0 and self.yMove == 0:
	    self.facing = 2

	if self.stamina == 0:
	    self.firing = False

	for b in pygame.sprite.spritecollide(self, bullets, False):
	    self.health = self.health - b.dam
	    b.kill()
	if self.health < 1:
	    self.kill()

	if self.stamina < self.stamina_max:
	    self.stamina += self.stamina_gain
	if self.stamina > self.stamina_max:
	    self.stamina = self.stamina_max
	if self.shield < self.shield_max:
	    self.shield += self.shield_gain

	if self.stamina_out == True and self.stamina == 100:
	    self.stamina_out = False

    def MoveKeyDown(self, key):
	if (key == K_RIGHT):
	    self.xMove += self.x_dist
	    self.facing = 3
	elif (key == K_LEFT):
	    self.xMove += -self.x_dist
	    self.facing = 1
	elif (key == K_UP):
	    self.yMove += -self.y_dist
	    self.facing = 2
	elif (key == K_DOWN):
	    self.yMove += self.y_dist
	    self.facing = 2

    def MoveKeyUp(self, key): # FIX ME! As is, this can cause player drift on respawn, but if those boolean checks are uncommented, it causes stick when changing from right<->left or up<->down

	if (key == K_RIGHT):
	    #if self.xMove < 0 or self.xMove > 0:
		self.xMove += -self.x_dist
	elif (key == K_LEFT):
	    #if self.xMove < 0 or self.xMove > 0:
		self.xMove += self.x_dist
	elif (key == K_UP):
	    #if self.yMove < 0 or self.yMove > 0:
		self.yMove += self.y_dist
	elif (key == K_DOWN):
	    #if self.yMove < 0 or self.yMove > 0:
		self.yMove += -self.y_dist
