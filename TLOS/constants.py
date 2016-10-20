# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:53:08 2016

@author: vini_
"""

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
psp_x = 620#620,9100
psp_y = 230#230
psp_x2 = 7800
psp_y2 = 555

# Boss
boss_roll_frames = 0
bsp_x = 10600
bsp_y = SCREEN_HEIGHT - 45

# Inimigos
er1_x = 1400
er2_x = 2450
er3_x = 3500
er4_x = 4550
er5_x = 6700
eb1_x = 5900
eb2_x = 7000
eb3_x = 8300
er1_y = er2_y = er3_y = er4_y = er5_y = eb1_y = eb2_y = eb3_y = SCREEN_HEIGHT - 45

# Bonfires
pb1_x = 661
pb1_y = 158
pb2_x = 8120
pb2_y = 1502

# Gerais
a = b = c = d = k = e = f = 0
 
# Cores
BGREEN = (21, 35, 12)
BLACK    = (0, 0, 0) 
BLUE     = (0, 0, 255)
BLACKBLUE = (51, 51, 153)
DARKBLUE = (47, 54, 153)
FAINTBLUE = (0, 64, 128)
SKYBLUE = (43, 66, 93)
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
soulsFont_MP = pygame.font.Font("fonts\OptimusPrinceps.ttf",30)
soulsFont_P = pygame.font.Font("fonts\OptimusPrinceps.ttf",12)
scrollFont_M = pygame.font.Font("fonts\TravelingTypewriter.ttf",60)
scrollFont_P = pygame.font.Font("fonts\TravelingTypewriter.ttf",25)
 
# Taxa de quadros da tela
FPS = 60