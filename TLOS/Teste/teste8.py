# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 09:02:34 2016

@author: vini_
"""

import pygame
pygame.init()
dsp=pygame.display.set_mode((500,500))
pygame.display.update()
ins=1
while ins==1:
    for x in pygame.event.get():
        print(x)
        if x.type == pygame.QUIT:
            ins=0
pygame.QUIT()
quit()