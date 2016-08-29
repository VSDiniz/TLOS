# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:08:06 2016

@author: vini_
"""
from Sprites import SpriteSheet
import pygame

class player(pygame.sprite.Sprite):
    
    p_l = []
    p_r = []
    
    d="r"
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        sprite = SpriteSheet("link.png")
        
        image = sprite.PegaSprite(0,0,32,60,0)
        self.p_r.append(image)
        
        self.images = self.p_r[0]
        self.rect = self.images.get_rect()
        
    def render(self,tela):
        tela.blit(self.p_r,(0,0))
        