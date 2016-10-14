# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 21:11:55 2016

@author: vini_
"""

import pygame
from spritesheet_functions import SpriteSheet

STONE_PLATFORM_LEFT   = (174, 196, 48, 12)
STONE_PLATFORM_MIDDLE = (174, 196, 48, 12)
STONE_PLATFORM_RIGHT  = (174, 196, 48, 12)
STONE_WALL = (101, 5, 48, 150)

class Background(pygame.sprite.Sprite):
    # Plataforma onde o player pode pular
 
    def __init__(self, sprite_sheet_data):
        """ Construtor do background
            O usuário passa um array de 4 números como indicado no topo do código """
        super().__init__()
 
        sprite_sheet = SpriteSheet("images/castle.png")
        # Pega a imagem para esta plataforma
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
 
        self.rect = self.image.get_rect()