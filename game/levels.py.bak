import pygame
from pygame.locals import *

from helpers import *

class Level:
    def __init__(self):
        self.loaded = True

class StageOne(Level):
    def __init__(self):
        Level.__init__(self)
        self.bgImg = load_image_trans("hitbox.png")
        self.monsterKinds = [
            ["tanuki.png",[3,100,.01,90,0,5,5],[True,12,15,3,[12,"monsterbulletred.png",3,[0,0],1.006,30,60,-1,0,0,0],7,[12,"tanukiexplode.png",5,[-25,25],.97,40,30]],250,False],
            ["kitsune.png",[3,50,.02,270,7,5,7],[True,15,10,5,[10,"monsterbullet.png",3,[0,0],1.01,30,30,-1,0,0,0],5,[10,"monsterbulletblue.png",5,[0,0],1.01,40,0]],300,False],
            ["tengu.png",[4,100,.01,360,0,6,12],[False,10,20,5,[20,"tengubullet.png",3,[0,0],1.006,30,30,-1,0,0,0],18,[0,"hitbox.png",0,[0,0],0,0,0]],1500,True]]
        # img,move_ai[speed,speed_max,speed_factor,angle_max,angle_factor,angle,score],fire_ai[death_blow,fire_max,firing_max,switch_back_point,fire_data[dam,img,speed,angle_factor,speed_factor,interval,firing_degree,dir_change_point,dir_change_factor,dir_change_time,spin],score,explode[dam,img,speed,angle_factor[a,b],speed_factor,interval,spin]],health,end_level

        self.monsterSpawns = []
        for time in range(1, 900000, 100):
            monster_type = random.randint(0, 2)
            x_coord = random.randint(0, 500)
            x_coord_2 = 500-x_coord
            self.monsterSpawns.append([time, monster_type, (x_coord, 0)])
            self.monsterSpawns.append([time, monster_type, (x_coord_2, 0)])
        '''
        self.monsterSpawns = [
            [1,0,(250,0)],
            [100,0,(125,0)],
            [100,0,(375,0)],
            [200,1,(125,0)],
            [200,1,(375,0)],
            [300,0,(125,0)],
            [300,1,(250,0)],
            [300,0,(375,0)],
            [400,0,(125,0)],
            [400,0,(375,0)],
            [500,1,(375,0)],
            [600,1,(125,0)],
            [600,0,(250,0)],
            [600,0,(375,0)],
            [700,1,(125,0)],
            [700,1,(375,0)],
            [700,2,(250,0)]] # [time,type,(x,y)]
        '''

class StageTwo(Level):
    def __init__(self):
	self.bgImg = load_image_trans("hitbox.png")
	self.monsterKinds = [
	    ["tanuki.png",[4,100,.01,90,0,5,5],[True,12,15,3,[12,"monsterbulletred.png",3,[0,0],1.006,30,60,-1,0,0,0],7,[12,"tanukiexplode.png",5,[-25,25],.97,40,30]],250,False],
	    ["kitsune.png",[4,50,.02,270,7,5,7],[True,15,10,5,[10,"monsterbullet.png",3,[0,0],1.01,30,30,-1,0,0,0],5,[10,"monsterbulletblue.png",5,[0,0],1.01,40,0]],300,False],
	    ["kappa.png",[6,100,.01,180,0,12,25],[False,5,5,1,[20,"kappabullet.png",2,[0,0],1.02,0,90,40,6,60,0],0,[0,"hitbox.png",0,[0,0],0,0,0]],2250,True]]
	# img,move_ai[speed,speed_max,speed_factor,angle_max,angle_factor,angle,score],fire_ai[death_blow,fire_max,firing_max,switch_back_point,fire_data[dam,img,speed,angle_factor,speed_factor,interval,firing_degree,dir_change_point,dir_change_factor,dir_change_time],score],health,end_level
	self.monsterSpawns = [
	    [1,0,(125,0)],
	    [1,0,(375,0)],
	    [100,1,(125,0)],
	    [100,0,(250,0)],
	    [100,1,(375,0)],
	    [200,0,(125,0)],
	    [200,0,(375,0)],
	    [350,1,(250,0)],
	    [400,1,(125,0)],
	    [400,1,(375,0)],
	    [500,0,(125,0)],
	    [500,1,(250,0)],
	    [500,0,(375,0)],
	    [600,0,(250,0)],
	    [700,2,(125,0)],
	    [700,1,(375,0)],
	    [700,1,(250,0)]] # [time,type,(x,y)]

class StageThree(Level):
    def __init__(self):
	self.bgImg = load_image_trans("hitbox.png")
	self.monsterKinds = [
	    ["tanuki.png",[4,100,.008,90,0,5,5],[True,12,15,3,[12,"monsterbulletred.png",3,[0,0],1.008,30,60,-1,0,0,0],7,[12,"tanukiexplode.png",5,[-25,25],.97,40,30]],250,False],
	    ["kitsune.png",[4,50,.02,270,7,5,7],[True,15,10,5,[10,"monsterbullet.png",3,[0,0],1.02,30,30,-1,0,0,0],5,[10,"monsterbulletblue.png",5,[0,0],1.01,40,0]],300,False],
	    ["bakeneko.png",[8,50,.1,360,0,5,15],[True,5,10,1,[15,"bakenekobullet.png",3,[12,0],1.05,0,90,30,-12,999999999,0],0,[14,"bakenekoexplode.png",3,[0,0],1.005,40,30]],400,False],
	    ["onryou.png",[15,100,.1,360,0,12,50],[False,1,36,36,[25,"onryoubullet.png",3,[0,0],1.02,20,90,20,36,10,0],0,[0,"hitbox.png",0,[0,0],0,0,0]],3000,True]]
	# img,move_ai[speed,speed_max,speed_factor,angle_max,angle_factor,angle,score],fire_ai[death_blow,fire_max,firing_max,switch_back_point,fire_data[dam,img,speed,angle_factor,speed_factor,interval,firing_degree,dir_change_point,dir_change_factor,dir_change_time],score],health,end_level
	self.monsterSpawns = [
	    [1,1,(125,0)],
	    [1,1,(250,0)],
	    [1,0,(375,0)],
	    [100,1,(250,0)],
	    [120,1,(250,0)],
	    [140,1,(250,0)],
	    [160,1,(250,0)],
	    [180,1,(250,0)],
	    [200,1,(250,0)],
	    [300,0,(250,0)],
	    [310,0,(250,0)],
	    [320,0,(250,0)],
	    [330,0,(250,0)],
	    [340,0,(250,0)],
	    [350,0,(350,0)],
	    [400,1,(125,0)],
	    [400,1,(375,0)],
	    [500,0,(125,0)],
	    [500,1,(250,0)],
	    [500,0,(375,0)],
	    [550,0,(250,0)],
	    [600,1,(250,0)],
	    [700,2,(125,0)],
	    [700,2,(375,0)],
	    [700,3,(250,100)]] # [time,type,(x,y)]
