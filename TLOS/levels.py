# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:53:45 2016

@author: vini_
"""

import pygame, sys, constants, platforms, pytmx
from pytmx.util_pygame import load_pygame

class Level():
    # Classe genérica para definir um level
 
    def __init__(self, player, enemy):
        # Lista de sprites usadas em todos os levels
        self.platform_list = None
        self.enemy_list = None
 
        # Imagem de background
        self.background = None
 
        # Quanto o world se deslocou esquerda/direita
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.enemy = enemy
 
    # Atualiza tudo num level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        # Desenha tudo num level 
        # Desenha o background
        screen.fill(constants.GRAY)
        # Faz o world se deslocar mais lentamente que o player
        screen.blit(self.background,(self.world_shift // 3,0)) 
 
        # Desenha todas as listas de sprites
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
         
    def shift_world(self, shift_x):
        # Desloca o world quando o player se move
        # Mantém controle de quanto o world se desloca
        self.world_shift += shift_x
 
        # Passa por toda a lista de sprites e altera
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
# Cria as plataformas para o level
 
class Level_00(Level):
 
    def __init__(self, player):
 
        Level.__init__(self, player)
 
        self.background = pygame.image.load("images/background.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        
 
class Level_01(Level):
 
    def __init__(self, player, enemy):
 
        Level.__init__(self, player, enemy)
 
        self.background = pygame.image.load("images/map4.png").convert() #101,5,48,150
        self.background = pygame.transform.scale(self.background,(2000,835))
        self.background.set_colorkey(constants.BGREEN)
        self.level_limit = -2500
 
        # Array com o tipo de plataforma e coordenadas (x,y) para localização
        level = [ [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-48, constants.SCREEN_HEIGHT-12],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*2), constants.SCREEN_HEIGHT-12],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*3), constants.SCREEN_HEIGHT-12],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*4), constants.SCREEN_HEIGHT-12],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*5), constants.SCREEN_HEIGHT-12],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-48, constants.SCREEN_HEIGHT-24],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*2), constants.SCREEN_HEIGHT-24],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*3), constants.SCREEN_HEIGHT-24],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*4), constants.SCREEN_HEIGHT-24],
                  [platforms.STONE_PLATFORM_MIDDLE, constants.SCREEN_WIDTH-(48*5), constants.SCREEN_HEIGHT-24]
                  ]
 
        # Passa pelo array e adiciona plataformas
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            block.enemy = self.enemy
            self.platform_list.add(block)
 
        # Adiciona uma plataforma móvel
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.enemy = self.enemy
        block.level = self
        self.platform_list.add(block)
 
 
class Level_02(Level):
 
    def __init__(self, player, enemy):
 
        Level.__init__(self, player, enemy)
 
        self.background = pygame.image.load("images/background.png").convert()
        self.background = pygame.transform.scale2x(self.background)
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
 
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
 
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
def start_screen():
    
    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        
    game_title = constants.soulsFont.render("THE LEGEND OF SOULS", True, constants.WHITE, None)
    press_start = constants.bitsFont.render("Press ENTER", True, constants.WHITE, None)
    not_start = constants.not_startBF.render("I said ENTER", True, constants.WHITE, None)

    instart = True

    while instart:
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
        game_title_rect = game_title.get_rect()
        game_title_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 450)
        screen1.blit(game_title, game_title_rect)
        press_start_rect = press_start.get_rect()
        press_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 100)
        screen1.blit(press_start, press_start_rect)
        pygame.display.update()
        
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit() # Fecha a janela se o usuário clicar em fechar
            if event.type == pygame.KEYDOWN:
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                    sys.exit() # Fecha a janela se o usuário pressionar ALT+F4
                    
                elif pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]:
                    instart = False # Sai da tela de início
                else:
                    not_start_rect = not_start.get_rect() # Zoa o usuário
                    not_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 75)
                    screen1.blit(not_start, not_start_rect)
                    pygame.display.update()
                    pygame.event.wait()