# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:02:21 2016

@author: vini_
"""

# Este módulo é usado para pegar sprites individuais das sprite sheets
import pygame

def createSprite(sprite_sheet, list1, doFlip=0, scale=0, colorkey=None):
    list2 = []
    for item in list1:
        item.append(colorkey)
        image =  sprite_sheet.get_image(item[0],item[1],item[2],item[3],item[4])
        if doFlip:
            image = pygame.transform.flip(image,True,False)
        if scale:
            image = pygame.transform.scale2x(image) 
        list2.append(image)
    return list2

class SpriteSheet(object):
    # Classe usada para pegar imagens de uma sprite sheet
 
    def __init__(self, file_name):
        # Construtor. Recebe o nome do arquivo do sprite sheet
 
        # Carrega o sprite sheet
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
    def get_image(self, x, y, width, height, colorkey = None):
        # Pega uma única imagem de uma sprite sheet
        # Recebe a coordenada (x,y) do sprite, canto superior esquerdo
        # e a largura e altura da sprite
 
        # Cria um blank de imagem novo
        image = pygame.Surface([width, height]).convert()
 
        # Copia a sprite da sprite sheet numa imagem menor
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assume "colorkey" como uma cor transparente
        image.set_colorkey(colorkey)
 
        # Retorna a imagem
        return image