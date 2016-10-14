# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:37:33 2016

@author: vini_
"""

import pygame
# modulo pra pegar cada sprite
class SpriteSheet(object):
    def _init_(self, Nome_foto):
        #Inicializa a SpriteSheet
        self.SpriteSheet = pygame.image.load(Nome_foto).convert()
        
        
    def PegaSprite(self, x, y, L, C, colorkey=None):
        #Cria o Retangunlo aonde ficara cada imagem 
        image = pygame.Surface([L,C]).convert()
        #Coloca a Sprite no Retangulo 
        image.blit(self.SpriteSheet,(0,0),(x,y,L,C))
        #Transforma o Fundo da imagem Transparente
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
            
        return image
        

                
                
        
    