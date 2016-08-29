# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 08:37:58 2016

@author: vini_
"""

import pygame

def timerFunc():
    print ("Timer CallBack")

pygame.init()
pygame.time.set_timer(pygame.USEREVENT+1, 1000)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT+1:
            timerFunc() #calling the function wheever we get timer event.
        if event.type == pygame.QUIT:
            break