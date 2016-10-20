# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:59:32 2016

@author: vini_
"""

import pygame

pygame.init()

# Player
player_latk1 = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword1.wav")
player_latk2 = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword2.wav")
player_hatk = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Spin.wav")
player_defend = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Clang_Bombable.wav")
player_jump = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Jump1.wav")
player_roll = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Attack1.wav")
player_dmg1 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt1.wav")
player_dmg2 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt2.wav")
player_dmg3 = pygame.mixer.Sound("sounds\TLOZ\OOT_AdultLink\OOT_AdultLink_Hurt3.wav")
player_estus1 = pygame.mixer.Sound("sounds\TLOZ\OOT_Navi\OOT_Navi_Out.wav")
player_estus2 = pygame.mixer.Sound("sounds\TLOZ\OOT_Navi\OOT_Navi_In.wav")
dead = pygame.mixer.Sound("sounds\DS\You Died.wav")

# Enemy
enemy_latk = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_MegatonHammer_Swing.wav")
enemy_hatk = pygame.mixer.Sound("sounds\TLOZ\OOT_Enemies\OOT_IronKnuckle_Attack_Swipe.wav")
enemy_defend = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_MegatonHammer_Hit.wav")
enemy_dmg = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Clang1.wav")
enemy_dead = pygame.mixer.Sound("sounds\TLOZ\OOT_Enemies\OOT_ReDead_Die.wav")

# Boss
boss_latk = pygame.mixer.Sound("sounds\TLOZ\OOT_Bosses\OOT_Ganondorf_Pound.wav")
boss_hatk = pygame.mixer.Sound("sounds\TLOZ\OOT_Bosses\OOT_Ganondorf_Burst_C.wav")
boss_defend = pygame.mixer.Sound("sounds\TLOZ\OOT_Bosses\OOT_Ganondorf_Deflect.wav")
boss_dmg = pygame.mixer.Sound("sounds\TLOZ\OOT_Bosses\OOT_Ganondorf_Hurt.wav")
boss_laugh = pygame.mixer.Sound("sounds\TLOZ\OOT_Voices\OOT_Ganondorf_Heheh.wav")
boss_win = pygame.mixer.Sound("sounds\TLOZ\OOT_Voices\OOT_Ganondorf_Laugh.wav")
boss_lose = pygame.mixer.Sound("sounds\DS\Defeated_Boss.wav")

# Menus
menu_open = pygame.mixer.Sound("sounds\TLOZ\OOT_Menus\OOT_PauseMenu_Open.wav")
menu_close = pygame.mixer.Sound("sounds\TLOZ\OOT_Menus\OOT_PauseMenu_Close.wav")
menu_cursor = pygame.mixer.Sound("sounds\TLOZ\OOT_Menus\OOT_PauseMenu_Cursor.wav")

# Others
bonfire_active = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Away.wav")
bonfire_lit = pygame.mixer.Sound("sounds\TLOZ\OOT_WeaponsItems\OOT_Sword_Draw.wav")
parry = pygame.mixer.Sound("sounds\DS\Parry.wav")
riposte = pygame.mixer.Sound("sounds\DS\Riposte.wav")