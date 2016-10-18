# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:56:15 2016

@author: vini_
"""

import pygame, constants, levels, sounds, spritesheet_functions

class Bonfire(pygame.sprite.Sprite):
    
    def __init__(self, player, screen):
        super().__init__()
        
        self.lit = False
        self.active = False
        
        self.lit_frames = []
        self.notlit_frames = []
        self.player = player
        self.screen = screen
        self.a = 0
        
        sprite_sheet = spritesheet_functions.SpriteSheet("images/link_3.png")
        
        "Acesa"
        list1=[[412, 1090, 27, 35],
               [412, 1130, 27, 35]]
        self.lit_frames = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACKBLUE)

        "Apagada"
        list1=[[367, 1090, 27, 35],
               [367, 1130, 27, 35]]
        self.notlit_frames = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACKBLUE)
        
        self.image = self.notlit_frames[0]
        self.rect = self.image.get_rect()
        
    def ani_bonfire(self):
        if self.lit:
            if self.active:
                self.image = self.lit_frames[0]
            else:
                self.image = self.lit_frames[1]
        else:
            self.image = self.notlit_frames[1]
            
    def lit_bonfire(self, player, screen, joy_count, b_triang, pressed):
        if pygame.sprite.collide_rect(self, player):
            if not self.lit:
                if joy_count > 1:
                    levels.msg_player("PRESS TRIANGLE TO LIT", screen)
                    if b_triang and player.on_ground:
                        self.lit = True
                        self.active = True
                        if self.a == 0:
                            sounds.bonfire_lit.play()
                            self.a = 1
                    else:
                        self.a = 0
                else:
                    levels.msg_player("PRESS U TO LIT", screen)
                    if pressed[pygame.K_u] and player.on_ground:
                        self.lit = True
                        self.active = True
                        if self.a == 0:
                            sounds.bonfire_lit.play()
                            self.a = 1
                    else:
                        self.a = 0
            else:
                    if joy_count > 1:
                        levels.msg_player("PRESS TRIANGLE TO REST", screen)
                        if b_triang and player.on_ground:
                            self.active = True
                            player.reborn()
                            if self.a == 0:
                                sounds.bonfire_active.play()
                                self.a = 1
                            for enemy in player.enemies:
                                enemy.reborn()
                        else:
                            self.a = 0
                    else:
                        levels.msg_player("PRESS U TO REST", self.screen)
                        if pressed[pygame.K_u] and player.on_ground:
                            self.active = True
                            player.reborn()
                            if self.a == 0:
                                sounds.bonfire_active.play()
                                self.a = 1
                            for enemy in player.enemies:
                                enemy.reborn()
                        else:
                            self.a = 0
            
    def update(self):
        self.ani_bonfire()
                        
                        
                        
                        
                        