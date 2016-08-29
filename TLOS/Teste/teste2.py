# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:56:03 2016

@author: vini_
"""

import pygame, sys #, glob
from Player import player
import Sprites
 
pygame.init()    
 
window = pygame.display.set_mode((800,600))
 
pygame.display.set_caption("The Legend of Souls")
 
black = (0,0,0)
white = (255,255,255)
red = (255,25,25)

'''class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=36
        self.height=48
        self.velocity=0
        self.falling=True
        self.onGround=False
        self.image=pygame.image.load("images/link.png")
        self.numImages=5
        self.cImage=0
        
    def update(self,gravity,pos):
        self.velocity+=gravity
        self.y-=self.velocity
        if pos !=0:
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.img=pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed=self.ani_1speed
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
        window.blit(self.image,(self.x,self.y))'''
        
player = player()
link = Sprites.SpriteSheet("link.png")
pos=0
gravity=-0.


#player=player(0,0)
 
clock = pygame.time.Clock()
        
while True:
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
 
            sys.exit()
 
        elif (event.type==pygame.KEYDOWN):
            
            if event.key==pygame.K_LALT or pygame.K_RALT:
                
                if event.key==pygame.K_F4:
                                        
                    sys.exit()
            
            if (event.key==pygame.K_a):
 
                moveX = -4
 
            if (event.key==pygame.K_d):
 
                moveX = 4
                pos=1
 
            if (event.key==pygame.K_w):
 
                moveY = -4
 
            if (event.key==pygame.K_s):
 
                moveY = 4
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_a):
 
                moveX=0
 
            if (event.key==pygame.K_d):
 
                moveX=0
                pos=0
                
            if (event.key==pygame.K_w):
 
                moveY=0
 
            if (event.key==pygame.K_s):
 
                moveY=0
 
    window.fill(white)
    window.blit(link,(0,0))
   # collisions=detectCollisions(player.x,player.y,player.width,player.height,Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height)
 
    player.render(window)    
    
    #player.render(collisions)
 
#    Sprite2.render(False)
 
    pygame.display.flip()
 
    clock.tick(50)
 
pygame.quit()