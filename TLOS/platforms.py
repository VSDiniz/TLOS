# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:54:18 2016

@author: vini_
"""

import pygame, constants
from spritesheet_functions import SpriteSheet
 
""" As constantes definem o tipo de plataforma:
        Nome do arquivo
        Coordenada X do sprite
        Coordenada Y do sprite
        Largura da sprite
        Altura da sprite """
 
#plat1 = (0, 0, 608, 64)
#plat2 = (0, 0, 640, 64)
#plat3 = (0, 0, 768, 64)
#plat4 = (0, 0, 576, 64)
#plat5 = (0, 0, 480, 64)
#plat6 = (0, 0, 250, 16)
#plat7 = (0, 0, 2200, 64)
#floatplat = (0, 0, 124, 16)
#block1 = (0, 0, 32, 32)
#block2 = (0, 0, 64, 32)
#block3 = (0, 0, 96, 32)
#stone_wall = (0, 0, 64, 1600)
plat1 = (0, 0, 736, 64)
plat2 = (0, 0, 2200, 64)
plat3 = (0, 0, 256, 64)
block1 = (0, 0, 32, 32)
block2 = (0, 0, 64, 32)
block3 = (0, 0, 96, 32)
floatplat3 = (0, 0, 92, 16)
floatplat4 = (0, 0, 128, 16)
stone_wall = (0, 0, 64, 1600)
 
class Platform(pygame.sprite.Sprite):
    # Plataforma onde o player pode pular
 
    def __init__(self, sprite_sheet_data):
        """ Construtor da Plataforma
            O usuário passa um array de 4 números como indicado no topo do código """
        super().__init__()
 
        sprite_sheet = SpriteSheet("images/whiteplatform.png")

        # Pega a imagem para esta plataforma
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        
        # Deixa as plataformas transparentes                                            
        self.image.set_colorkey(constants.WHITE)
 
        self.rect = self.image.get_rect()
        
 
class MovingPlatform(Platform):
    # Plataforma móvel

    def __init__(self, sprite_sheet_data):
 
        super().__init__(sprite_sheet_data)
 
        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.player = None
 
    def update(self):
        """ Move a plataforma.
            Se o player estiver no caminho, vai empurrá-lo para fora do caminho.
            Não foi programado o que acontece se a plataforma empurra o player
            para outro objeto """ 
 
        # Move direita/esquerda
        self.rect.x += self.change_x
 
        # Verifica se colide com o player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            """ Colisão com o player. Empurra o player e assume
                que não colide com mais nada """
 
            """ Se o player está indo para a direita, define o lado direito do player
                para o lado esquerdo do objeto que o acertou """
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Se o player estiver indo para a esquerda, faz o oposto
                self.player.rect.left = self.rect.right
 
        # Move para cima/baixo
        self.rect.y += self.change_y
 
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
 
            # Redefine a posição do player baseada no topo/fundo do objeto
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Checa as fronteiras e verifica se é necessário reverter as direções
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1