import pygame
from pygame.locals import *
import os, sys, profile, pstats
import random
import pickle
from math import *
import pygame.surfarray as surfarray

from helpers import *
import sprites
import levels

class Main:

    def __init__(self):
	print ("Initializing Pygame...")
	pygame.init()
	width,height = 512, 512
	self.screen = pygame.display.set_mode((width
					       , height))
	self.screen.fill((0,0,0))

	self.playerInit()
	self.menuInit()
	self.variableInit()
	self.levelInit()
	self.groupInit()
	self.menu(self.characterMenu)
        #enter game right away
        pygame.event.clear()
        self.initGame(self.playerList[2][1])

    def menuInit(self):
        #start the game with the player we want
        #self.initGame(self.ormrinn)
	print ("Initializing menus...")

	self.characterMenu = [["Choose your character:",(95,140,225)]]

    #selects character
	indexNum = 2
	indexMax = len(self.playerList) - 1
	x,y = 100,200
	while indexNum <= indexMax:
	    text = self.playerList[indexNum][0]
	    player = self.playerList[indexNum][1]
	    list = [text,(95,140,225),(x,y),self.initGame,player]
	    self.characterMenu.append(list)
	    indexNum += 1
	    y += 32
	self.difficultyMenu = [
	    ["Set Difficulty Level:",(95,140,225)],
	    ["Easy",(95,140,225),(100,200),self.setDifficulty,.8],
	    ["Normal",(95,140,225),(100,234),self.setDifficulty,1],
	    ["Hard",(95,140,225),(100,268),self.setDifficulty,1.2]]
	self.startMenu = [
	    ["",(0,0,0)],
	    ["New Game",(95,140,225),(100,200),self.menu,self.characterMenu],
	    ["Set Difficulty",(95,140,225),(100,234),self.menu,self.difficultyMenu],
	    ["Quit",(95,140,225),(100,268),sys.exit,None]]
	self.endLevelMenu = [
	    ["Stage clear! Continue?",(95,140,225)],
	    ["Continue",(95,140,225),(100,200),self.startGame,None],
	    ["Quit",(95,140,225),(100,234),sys.exit,None]]

    def variableInit(self):
	print("Initializing variables...")

	self.playing = False
	self.inMenu = False
	self.paused = False
	self.delaying_respawn = False
	self.moveable = False
	self.delay_fire = False

	self.respawn_timer = 0
	self.respawn_now = 50
	self.ms_per_round = 30
	self.rounds_passed = 0
	self.last_bg_draw = 0

	self.current_selection = 1
	self.num_choices = 0
	self.current_menu = self.characterMenu

	self.xMove = 0
	self.yMove = 0
	self.lives = 99999999
        self.death = False
	self.score = 0
        self.score_prev = 0

	self.difficulty = 1

	try:
	    loadDataFile = open("pickles.py", "r", 0)
	    loadDataDict = pickle.load(loadDataFile)
	    self.difficulty = loadDataDict["difficulty"]
	    loadDataFile.close()
	except IOError:
	    loadDataFile = open("pickles.py", "w", 0)
	    loadDataDict = {'difficulty':self.difficulty}
	    pickle.dump(loadDataDict,loadDataFile)
	self.monster_total_counter = 0
	self.monster_list = []
	self.character = [(250,450),"triangleman.png",10,4,6,1,4,5,["bullet.png",True,(65,115),30,10,(0,0),.1,False,0,0],1,["bullet.png",10,2160,[-1,-1],5,5,[-10,10],1,0,0],50,.1,["shield.png",30,100],2]
	self.spawnPlayer()


    def levelInit(self):
	print("Initializing levels...")

	self.ending_level = False
	self.ending_level_counter = 0
	self.levels = [levels.StageOne(),levels.StageTwo(),levels.StageThree()]
	self.level = 0
	self.current_level = self.levels[self.level]
	self.bg_move = 0
	self.bg_dist = 1
	self.bg_img = self.current_level.bgImg

    def playerInit(self):
	print("Initializing player...")

	self.ltReed = [(250,450),"reed.png",6,3,5,1,1,3,["reedbullet.png",True,(65,115),90,9,(0,0),.1,False,False,0],1,["reedchargebullet.png",5,1080,[-100,30],1.2,5,[0,0],1,0,0],50,.1,["shield.png",20,120],2]

	self.lerea = [(250,450),"lerea.png",6,4,6,1,2,3,["lereabullet.png",True,(65,115),20,6,(0,0),.2,False,False,20],2,["lereachargebullet.png",15,60,[-120,-180],30,2,[0,0],.2,0,0],50,.2,["shield.png",120,100],1]

	self.karex = [(250,450),"karex.png",5,4,6,1,2,3,["karexbullet.png",False,(0,0),40,3,(0,0),.2,False,4,0],2,["karexbullet.png",10,1080,[-100,30],2,2,[0,0],.2,4,0],50,.2,["shield.png",150,100],6]

	self.dragonfly = [(250,450),"dragonfly.png",7,2,4,1,3,4,["dragonflybullet.png",True,(55,125),20,11,(-5,5),.2,False,0,0],1,["dragonflybullet.png",10,2160,[-1,-1],1.5,5,[-10,10],1,0,0],60,.2,["shield.png",25,80],1]

	self.ormrinn = [(250,450),"ormrinn.png",6,4,6,1,2,3,["ormrinnbullet.png",False,(0,0),40,10,(0,0),.5,False,0,0],2,["ormrinnbullet.png",10,2160,[-1,-1],2,5,[10,10],1,0,0],40,.1,["shield.png",100,50],2]

	self.triangleMan = [(250,450),"triangleman.png",10,4,6,1,4,5,["bullet.png",True,(65,115),30,10,(0,0),.1,False,0,0],1,["bullet.png",10,2160,[-1,-1],5,5,[-10,10],1,0,0],50,.1,["shield.png",30,100],2]

	self.playerList = [["Lt. Reed",self.ltReed],["Dragonfly",self.dragonfly],["Ormrinn",self.ormrinn],["Karex",self.karex],["Lerea",self.lerea]]

    def groupInit(self):
	print("Initializing groups...")

	self.wall_vertical_group = pygame.sprite.Group()
	self.wall_horizontal_group = pygame.sprite.Group()

	self.player_bullet_group = pygame.sprite.Group()
	self.monster_bullet_group = pygame.sprite.Group()

	self.monster_group = pygame.sprite.Group()
	self.shield_group = pygame.sprite.Group()

    def menu(self, choices):

	self.screen.fill((0,0,0))
	self.inMenu = True
	self.num_choices = len(choices) - 1
	itr = 1
	self.current_menu = choices
	if pygame.font:
	    font = pygame.font.Font(None, 34)
	    text = font.render(choices[0][0]
			       , 1, (choices[0][1]))
	    textpos = 80,150
	    self.screen.blit(text, textpos)
	while itr <= self.num_choices:
	    if pygame.font:
		font = pygame.font.Font(None, 28)
		if choices[self.current_selection] == choices[itr]:
		    text = font.render(choices[itr][0]
				       , 1, (choices[itr][1]))
		else:
		    text = font.render(choices[itr][0]
				       , 1, (55, 85, 110))
		textpos = choices[itr][2]
		self.screen.blit(text, textpos)
		itr += 1

    def setDifficulty(self, value):

	self.difficulty = value
	loadDataFile = open("pickles.py", "w", 0)
	loadDataDict = {'difficulty':self.difficulty}
	pickle.dump(loadDataDict,loadDataFile)
	self.menu(self.characterMenu)

    def initGame(self, character):

	self.character = character
	self.spawnPlayer()
	self.startGame()

    def startGame(self):

	self.current_level = self.levels[self.level]
	self.bg_img = self.current_level.bgImg
	img = load_image_trans("wall.png",-1)
	ctrpt = 1,500
	self.wall_b = sprites.Object(ctrpt,img)
	ctrpt = 1,0
	self.wall_t = sprites.Object(ctrpt,img)
	img2 = pygame.transform.rotate(img, 90)
	ctrpt = 1,250
	self.wall_l = sprites.Object(ctrpt,img2)
	ctrpt = 500,250
	self.wall_r = sprites.Object(ctrpt,img2)
	self.wall_vertical_group.add(self.wall_l)
	self.wall_vertical_group.add(self.wall_r)
	self.wall_horizontal_group.add(self.wall_b)
	self.wall_horizontal_group.add(self.wall_t)
        ctrpt = 250,500
        self.wall_b_2 = sprites.Object(ctrpt, img)
        self.wall_horizontal_group.add(self.wall_b_2)

	img = load_image_trans("sidebar.png")
	ctrpt = 500,250
	sidebar = sprites.Object(ctrpt,img)
	self.sidebar = pygame.sprite.RenderPlain((sidebar))

	self.playing = True
	self.moveable = True

    def sidebarDraw(self):

	self.sidebar.draw(self.screen)
    '''
	if pygame.font:
	    font = pygame.font.Font(None, 28)
	    level = self.level + 1
	    text = font.render("Level: %s" % level
			       , 1, (55, 85, 110))
	    textpos = 510,10
	    self.screen.blit(text, textpos)
	    text = font.render("Score: %s" % self.score
			       , 1, (55, 85, 110))
	    textpos = 510,42
	    self.screen.blit(text, textpos)

	    font = pygame.font.Font(None, 28)
	    text = font.render("Lives: %s" % self.lives
			       , 1, (55, 85, 110))
	    textpos = 510,74
	    self.screen.blit(text, textpos)

	    font = pygame.font.Font(None, 28)
	    text = font.render("Charge: %s" % self.hitbox.charge
			       , 1, (55, 85, 110))
	    textpos = 510,106
	    self.screen.blit(text, textpos)

	    charge_bar = load_image_trans('chargebar.png', -1)
	    charge_bar_bg = load_image_trans('chargebarbg.png', -1)
	    self.screen.blit(charge_bar_bg, (510, 138))
	    if self.hitbox.charge > 0:
		self.screen.blit(pygame.transform.scale(charge_bar,(int(175*(float(self.hitbox.charge)/self.hitbox.charge_max)),20)), (512,140))

	    font = pygame.font.Font(None, 28)
	    text = font.render("Stamina: %s" % self.hitbox.stamina
			       , 1, (55, 85, 110))
	    textpos = 510,170
	    self.screen.blit(text, textpos)

	    stamina_bar = load_image_trans('chargebar.png', -1)
	    stamina_bar_bg = load_image_trans('chargebarbg.png', -1)
	    self.screen.blit(stamina_bar_bg, (510, 202))
	    if self.hitbox.stamina > 0:
		self.screen.blit(pygame.transform.scale(stamina_bar,(int(175*(float(self.hitbox.stamina)/self.hitbox.stamina_max)),20)), (512,204))

	    font = pygame.font.Font(None, 28)
	    text = font.render("Shield: %s" % self.hitbox.shield
			       , 1, (55, 85, 110))
	    textpos = 510,236
	    self.screen.blit(text, textpos)

	    shield_bar = load_image_trans('chargebar.png', -1)
	    shield_bar_bg = load_image_trans('chargebarbg.png', -1)
	    self.screen.blit(stamina_bar_bg, (510, 268))
	    if self.hitbox.shield > 0:
		self.screen.blit(pygame.transform.scale(shield_bar,(int(175*(float(self.hitbox.shield)/self.hitbox.shield_max)),20)), (512,270))

	    font = pygame.font.Font(None, 28)
	    text = font.render("Difficulty: %s" % self.difficulty
			       , 1, (55, 85, 110))
	    textpos = 510,304
	    self.screen.blit(text, textpos)
        '''

    def inGameDraw(self):

	if self.inMenu == False:
	    pygame.display.flip()
	    self.screen.fill((0,0,0))
	    self.bg_img = self.current_level.bgImg
	    self.bg_move += self.bg_dist
	    if self.last_bg_draw + 500 == self.rounds_passed:
		self.last_bg_draw = self.rounds_passed
		self.bg_move -= 500
	    coord = self.bg_move - 500
	    #self.screen.blit(self.bg_img, (0,coord))
	    self.shield_group.draw(self.screen)
	    self.player_bullet_group.draw(self.screen)
	    self.player_group.draw(self.screen)
	    self.hitbox_group.draw(self.screen)
	    self.wall_vertical_group.draw(self.screen)
	    self.wall_horizontal_group.draw(self.screen)
	    self.monster_group.draw(self.screen)
	    self.monster_bullet_group.draw(self.screen)
	    #self.sidebarDraw()

    def spawnPlayer(self):

	centerPoint,image,size,xmove,ymove,health,stamina_gain,stamina_loss,bullet_data,charge_speed,charge_bullet_data,shield_cost,shield_gain,shield_data,delay_bullets = self.character
	data = xmove,ymove,health,stamina_gain,stamina_loss,bullet_data,charge_speed,charge_bullet_data,shield_cost,shield_gain,shield_data,delay_bullets
	img = load_image_trans("hitbox.png",-1)
	img = pygame.transform.scale(img,(size,size))
	self.hitbox = sprites.Hitbox(centerPoint,img,data)
	image = load_image_trans(image,-1)
	self.playerImg = sprites.Object(centerPoint,image)
	self.hitbox_group = pygame.sprite.RenderPlain((self.hitbox))
	self.player_group = pygame.sprite.RenderPlain((self.playerImg))
	self.delaying_respawn = False
	self.respawn_counter = 0
	self.moveable = True
	self.hitbox.xMove,self.hitbox.yMove = self.xMove,self.yMove
        self.hitbox.firing = True
        self.prev_key = 3
        self.reward_given = 0
        self.alive = True

    def spawnMonster(self):

	for l in self.current_level.monsterSpawns:
	    if l[0] == self.rounds_passed:
		img = load_image_trans(self.current_level.monsterKinds[l[1]][0],-1)
		move_ai_data = self.current_level.monsterKinds[l[1]][1]
		fire_ai_data = self.current_level.monsterKinds[l[1]][2]
		data = [move_ai_data,fire_ai_data,self.current_level.monsterKinds[l[1]][-2],self.current_level.monsterKinds[l[1]][-1]]
		monster = sprites.Monster(l[2],img,data)
		monster.health = monster.health * self.difficulty
		monster.fire_max = monster.fire_max / self.difficulty
		self.monster_group.add(monster)
		self.monster_total_counter += 1
		self.monster_list.append(monster)

    def fire(self):

	if self.hitbox.stamina == 0:
	    self.hitbox.firing = True
	    self.hitbox.stamina_out = False
	else:
	    self.hitbox.stamina -= 0
	    if self.hitbox.stamina < 100:
		self.stamina = 100
	    x,y,width,height = self.hitbox.rect
	    x += (width / 2)
	    ctrpt = x,y
	    img = load_image_trans(self.hitbox.bullet_data[0],-1)
	    spray_angle_a,spray_angle_b = self.hitbox.bullet_data[2]
	    if self.hitbox.bullet_data[1] == True:
		flight_angle = random.randint(spray_angle_a,spray_angle_b)
		flight_angle = -flight_angle
	    else:
		flight_angle = -90
	    rotation = -flight_angle - 90
	    img = pygame.transform.rotate(img,rotation)
	    bullet = sprites.Bullet(ctrpt,img,flight_angle,self.hitbox.bullet_data[3:])
	    self.player_bullet_group.add(bullet)

    def shield(self):

	if self.hitbox.shield >= self.hitbox.shield_cost:
	    self.hitbox.shield -= self.hitbox.shield_cost
	    x,y,width,height = self.hitbox.rect
	    x += (width / 2)
	    y -= (height / 2)
	    ctrpt = x,y
	    img = load_image_trans(self.hitbox.shield_data[0])
	    data = [self.hitbox.shield_data[1],self.hitbox.shield_data[2]]
	    shield = sprites.Shield(ctrpt,img,data)
	    self.shield_group.add(shield)

    def playerPatternFire(self):
	imgID,interval,degreeNum,switchBackPoints,damFactor,speed,angleFactor,speedFactor,homing,spin = self.hitbox.charge_bullet_data
	self.hitbox.charge = 0
	x,y,width,height = self.hitbox.rect
	x += (width / 2)
	y -= (height / 2)
	ctrpt = x,y
	img = load_image_trans(imgID,-1)
	dam = (self.hitbox.dam * damFactor * self.hitbox.stamina) / 100
	degrees = 0
	passedDegrees = switchBackPoints[0]
	oldDegrees = 0
	rotation = -90 - switchBackPoints[0]
	while degrees <= degreeNum:
	    if (oldDegrees + 360) == degrees:
		speed += speedFactor
		oldDegrees = degrees

	    if (degrees - oldDegrees) == switchBackPoints[1]:
		passedDegrees = switchBackPoints[0]
		rotation = -switchBackPoints[0] - 90
		oldDegrees = degrees
		speed += speedFactor
	    image = pygame.transform.rotate(img,rotation)
	    data = [dam,speed,angleFactor,speedFactor,True,homing,spin]
	    bullet = sprites.Bullet(ctrpt,image,passedDegrees,data)
	    self.player_bullet_group.add(bullet)
	    degrees += interval
	    passedDegrees += interval
	    rotation -= interval

    def monsterPatternFire(self, monst):

	monst.firing = False
	dam,img,degreeNum,speed,angleFactor,speedFactor,interval,switchBackPoints = monst.fire_data
	img = load_image_trans(img,-1)
	x,y,width,height = monst.rect
	x += (width / 2)
	y += (height / 2)
	ctrpt = x,y
	degrees = 0
	oldDegrees = 0
	passedDegrees = switchBackPoints[0]
	rotation = -90 + switchBackPoints[0]
	while degrees < degreeNum:
	    if (degrees - oldDegrees) >= switchBackPoints[1]:
		passedDegrees = switchBackPoints[0]
		rotation = -90 + switchBackPoints[0]
		speed += 2
		oldDegrees = degrees
	    data = [dam,speed,angleFactor,speedFactor,False]
	    bullet = sprites.Bullet(ctrpt,img,passedDegrees,data)
	    self.monster_bullet_group.add(bullet)
	    degrees += interval
	    passedDegrees += interval
	    rotation -= interval

    def monsterFire(self, monst):

	dam,img,speed,angleFactor,speedFactor,interval,degree_base,dir_change_point,dir_change_factor,dir_change_time,spin = monst.fire_data
	if angleFactor[1] != 0:
	    angleFactor = (random.randint(angleFactor[0],angleFactor[1]) / 10)
	else:
	    angleFactor = angleFactor[0]
	degree = monst.firing_degree_passed
	img = load_image_trans(img,-1)
	rotation = (degree * -1)
	img = pygame.transform.rotate(img, rotation)
	x,y,width,height = monst.rect
	x += (width / 2)
	y += (height / 2)
	ctrpt = x,y
	data = [dam,speed,angleFactor,speedFactor,dir_change_point,dir_change_factor,dir_change_time,spin]
	bullet = sprites.monsterBullet(ctrpt,img,degree,data)
	self.monster_bullet_group.add(bullet)

    def explode(self, monst):

	dam,img,speed,factor,speedFactor,interval,spin = monst.explode_data
	x,y,width,height = monst.rect
	x += (width / 2)
	y += (height / 2)
	ctrpt = x,y
	dam = monst.fire_data[0]
	degrees = 0
	img = load_image_trans(img,-1)
	while degrees <= 360:
	    if factor[1] != 0:
		factor_a, factor_b = factor[0],factor[1]
		angleFactor = (random.randint(factor_a,factor_b) / 10)
	    else:
		angleFactor = factor[0]
	    data = [dam,speed,angleFactor,speedFactor,-1,0,0,spin]
	    bullet = sprites.monsterBullet(ctrpt,img,degrees,data)
	    self.monster_bullet_group.add(bullet)
	    degrees += interval

    def getTarget(self):

	storedCoord = 9999999
	storedMonst = None
	if self.monster_list != []:
	    for m in self.monster_group:
		mx,my,mw,mh = m.rect
		px,py,pw,ph = self.hitbox.rect
		coord = (mx - px) + (my - py)
		if coord < storedCoord:
		    storedCoord = coord
		    storedMonst = m
	return storedMonst

    def inGameUpdate(self):

        self.reward_given = 0
	self.rounds_passed += 1
	self.spawnMonster()
	if self.respawn_counter >= self.respawn_now and self.lives > 0 and self.delaying_respawn == True:
            #
            #Still have the issue of drifting on respawn, causing the player to have high movespeed and

            #causing player to clip out of bounds
            map(lambda b: b.kill(), self.monster_bullet_group)
            map(lambda b: b.kill(), self.player_bullet_group)
            map(lambda m: m.kill(), self.monster_group)
            pygame.event.clear()
            self.levelInit()
            self.initGame(self.playerList[2][1])

            self.alive = True
            self.death = False
            self.rounds_passed = 0
	    #for b in self.monster_bullet_group:
		#b.kill()

	if self.ending_level == True:
	    if self.ending_level_counter == 100:
		self.level += 1
		self.moveable = False
		self.menu(self.endLevelMenu)
		self.ending_level = False
		self.ending_level_counter = 0
		for b in self.monster_bullet_group:
		    b.kill()
		for b in self.player_bullet_group:
		    b.kill()
		for s in self.shield_group:
		    s.kill()
		for m in self.monster_group:
		    m.kill()
		self.rounds_passed = 0
		self.last_bg_draw = 0
	    else:
		self.ending_level_counter = 1
	if self.lives < 1:
	    #print(self.score)
	    self.__init__()

	if self.delaying_respawn == True:
	    self.moveable = False
	    self.respawn_counter += self.ms_per_round
	    self.hitbox.charge = 0
	else:
	    self.respawn_counter = 0

	if self.hitbox.firing == True:
	    if self.rounds_passed % self.hitbox.delay_bullets == 0:
		self.fire()
	    else:
		self.hitbox.stamina -= self.hitbox.stamina_loss

	if self.hitbox.stamina < 100:
	    self.hitbox.stamina = 100

	for m in self.monster_group:
	    if m.firing == True:
		self.monsterFire(m)
	    if m.dying == True:
		self.score += m.score
		if m.deathBlow == True:
		    self.explode(m)
		if m.end_level == True:
		    self.ending_level = True
		m.kill()
		self.monster_total_counter -= 1
		self.monster_list.remove(m)
	    if m.giving_charge_points == True:
		self.hitbox.charge += 1
		m.giving_charge_points = False
                self.reward_given += 5
		if self.hitbox.charge > self.hitbox.charge_max:
		    self.hitbox.charge = self.hitbox.charge_max

	if self.hitbox.health < 0:
            self.death = True
            self.alive = False
            self.hitbox.MoveKeyUp(276-self.prev_key)
	    self.hitbox.health = 0
	    self.lives -= 1
	    self.hitbox.firing = False
	    self.delaying_respawn = True
	    self.hitbox.charge = 0
	    self.moveable = False
	    self.playerImg.kill()
	    self.hitbox.rect.move_ip(100000,100000)
	    self.hitbox.kill()



	self.xMove,self.yMove = self.hitbox.xMove,self.hitbox.yMove
	self.hitbox.moveable = self.moveable
	self.hitbox.update(self.wall_vertical_group,self.wall_horizontal_group,self.monster_bullet_group)
	self.playerImg.update(self.hitbox.xPub,self.hitbox.yPub)
	target = self.getTarget()
	self.player_bullet_group.update(target)
	self.monster_group.update(self.player_bullet_group)
	self.monster_bullet_group.update()
	self.shield_group.update(self.monster_bullet_group, self.player_bullet_group)

	self.inGameDraw()

    def MainLoop(self, action):
        pygame.time.wait(self.ms_per_round)
        performed_action = 0
        previous_action = 0
        if action == 0:
            performed_action = K_LEFT
        elif action == 1:
            performed_action = K_RIGHT
        else:
            performed_action = K_x

        if self.prev_key == 0:
            previous_action = K_LEFT
        elif self.prev_key == 1:
            previous_action = K_RIGHT
        else:
            previous_action = K_x
        if self.alive:
            pygame.event.post(pygame.event.Event(KEYDOWN, key=K_x))
            if self.prev_key != action:
                pygame.event.post(pygame.event.Event(KEYUP, key=previous_action))
                pygame.event.post(pygame.event.Event(KEYDOWN, key=performed_action))

        self.prev_key = action


        pygame.event.pump()

        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        	    sys.exit()
        	elif event.type == KEYDOWN:
        	    if ((event.key == K_RIGHT)
        		or (event.key == K_LEFT)
        		or (event.key == K_UP)
        		or (event.key == K_DOWN)):
        		self.hitbox.MoveKeyDown(event.key)
        	    if event.key == K_x:
        		if self.hitbox.stamina_out == False:
        		    self.hitbox.firing = True
        	    if event.key == K_z:
        		if self.hitbox.charge == self.hitbox.charge_max:
        		    self.playerPatternFire()
        	    if event.key == K_c:
        		self.shield()
        	    if event.key == K_p:
        		if self.paused == True:
        		    self.paused = False
        		    self.playing = True
        		    self.moveable = True
        		else:
        		    self.paused = True
        		    self.playing = False
        		    self.moveable = False
        	    if self.inMenu == True:
        		if event.key == K_UP:
        		    self.current_selection -= 1
        		    if self.current_selection < 1:
        			self.current_selection = 1
        		    self.menu(self.current_menu)
        		elif event.key == K_DOWN:
        		    self.current_selection += 1
        		    if self.current_selection > self.num_choices:
        			self.current_selection = self.num_choices
        		    self.menu(self.current_menu)
        		elif event.key == K_x:
        		    self.inMenu = False
        		    self.screen.fill((0,0,0))
        		    if self.current_menu[self.current_selection][4] != None:
        			self.current_menu[self.current_selection][3](self.current_menu[self.current_selection][4])
        			self.current_selection = 1
        		    else:
        			self.current_menu[self.current_selection][3]()
        			self.current_selection = 1
        	elif event.type == KEYUP:
        	    if ((event.key == K_RIGHT)
        		or (event.key == K_LEFT)
        		or (event.key == K_UP)
        		or (event.key == K_DOWN)):
        		self.hitbox.MoveKeyUp(event.key)
        	    if event.key == K_x:
        		self.hitbox.firing = False

        if self.inMenu == True:
        	self.moveable = False
        	self.playing = False
        pygame.display.flip()
        if self.playing == True:
        	self.inMenu = False
        	self.inGameUpdate()
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        reward = (self.score - self.score_prev)*2 + self.reward_given*2 - 1
        if self.death:
            reward = -500
        self.score_prev = self.score
        #print(self.alive)
        return reward, image_data, self.death

if __name__ == "__main__":
    MainWindow = Main()
    MainWindow.MainLoop()
