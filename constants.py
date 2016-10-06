# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:53:08 2016

@author: vini_
"""

#Constantes globais

import pygame

pygame.init()

# Constantes

# Dimensões de janela
SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 600
LEVEL_BOTTOM  = SCREEN_HEIGHT + 1000

# Player
slow_regen = 0.04
fast_regen = 0.12
estus_maxregen = 35
player_roll_frames = 0
psp_x = 6000#1075
psp_y = SCREEN_HEIGHT - 45

# Boss
boss_roll_frames = 0
bsp_x = 6050
bsp_y = SCREEN_HEIGHT - 45

# Gerais
c = k = 0
 
# Cores
BGREEN = (21, 35, 12)
BLACK    = (0, 0, 0) 
BLUE     = (0, 0, 255)
DARKBLUE = (47, 54, 153)
FAINTBLUE = (0, 64, 128)
GRAY = (81, 74, 67)
GREEN = (55, 117, 44)
ORANGE = (186, 53, 7)
RED = (165, 23, 9)
YELLOW = (254, 255, 104)
WHITE    = (255, 255, 255)

# Fontes
bitsFont_M = pygame.font.Font("fonts\8-BIT_WONDER.TTF",20)
bitsFont_P = pygame.font.Font("fonts\8-BIT_WONDER.TTF",10)
soulsFont_G = pygame.font.Font("fonts\OptimusPrinceps.ttf",120)
soulsFont_M = pygame.font.Font("fonts\OptimusPrinceps.ttf",72)
soulsFont_P = pygame.font.Font("fonts\OptimusPrinceps.ttf",12)
scrollFont_M = pygame.font.Font("fonts\TravelingTypewriter.ttf",60)
scrollFont_P = pygame.font.Font("fonts\TravelingTypewriter.ttf",25)
 
# Taxa de quadros da tela
FPS = 60