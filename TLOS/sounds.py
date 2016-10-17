# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:59:32 2016

@author: vini_
"""

import pygame

pygame.init()

level0 = pygame.mixer.Sound("sounds/TLOZ/Gerudo Valley Theme.wav")
level1 = pygame.mixer.Sound("sounds/DS/Bloodborne Soundtrack OST - Cleric Beast.wav")

# Player
player_latk1 = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword1.wav")
player_latk2 = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword2.wav")
player_hatk = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Spin.wav")
player_defend = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Clang_Bombable.wav")
player_roll = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Attack1.wav")
player_dmg1 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt1.wav")
player_dmg2 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt2.wav")
player_dmg3 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt3.wav")
player_estus1 = pygame.mixer.Sound("sounds\TLOZ\OOT_Navi\OOT_Navi_Out.wav")
player_estus2 = pygame.mixer.Sound("sounds\TLOZ\OOT_Navi\OOT_Navi_In.wav")
dead = pygame.mixer.Sound("sounds\DS\You Died.wav")

# Enemy
enemy_dmg = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Clang1.wav")

# Boss
#boss_latk = pygame.mixer.Sound("sounds\TLOZ\OOT_.wav")
#boss_hatk = pygame.mixer.Sound("sounds\TLOZ\OOT_.wav")
#boss_dmg = pygame.mixer.Sound("sounds\TLOZ\OOT_.wav")
#boss_win = pygame.mixer.Sound("sounds\TLOZ\OOT_.wav")

# Others
bonfire_active = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Away.wav")
bonfire_lit = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Draw.wav")
parry = pygame.mixer.Sound("sounds\DS\Parry.wav")
riposte = pygame.mixer.Sound("sounds\DS\Riposte.wav")