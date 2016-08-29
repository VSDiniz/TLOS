# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:53:08 2016

@author: vini_
"""

#Constantes globais

import pygame

pygame.init()

# Constantes
slow_regen = 0.05
fast_regen = 0.25
estus_maxregen = 35
i = 0
 
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
WHITE    = (255, 255, 255) 

# Fontes
bitsFont = pygame.font.Font("fonts\8-BIT_WONDER.TTF",20)
not_startBF = pygame.font.Font("fonts\8-BIT_WONDER.TTF",10)
soulsFont = pygame.font.Font("fonts\OptimusPrinceps.ttf",72)
boss_SF = pygame.font.Font("fonts\OptimusPrinceps.ttf",12)
estus_BF = pygame.font.Font("fonts\8-BIT_WONDER.TTF",10)
 
# Dimensões de janela
SCREEN_WIDTH  = 900
SCREEN_HEIGHT = 550

# Taxa de quadros da tela
FPS = 60