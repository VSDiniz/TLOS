# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:59:46 2016

@author: vini_
"""
import pygame

def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Escolha de Movimentos
        if self.change_x == 0 and self.change_y == 0 :
            self.rect.x += self.change_x
            pos = self.rect.x
            if self.direction == "R":
                frame = (pos // 30) % len(self.Para_Frames_R)
                self.image = self.Para_Frames_R[frame]
            else:
                frame = (pos // 30) % len(self.Para_Frames_L)
                self.image = self.Para_Frames_L[frame]
                
        elif self.change_x != 0 and self.change_y == 0:
            # Move left/right
            self.rect.x += self.change_x
            pos = self.rect.x + self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.Move_Frames_R)
                self.image = self.Move_Frames_R[frame]
            else:
                frame = (pos // 30) % len(self.Move_Frames_L)
                self.image = self.Move_Frames_L[frame]
            
        
            # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # Move Up/Down
        if self.change_x == 0 and self.change_y != 0:
            self.rect.y += self.change_y
            pos = self.rect.y
            if self.direction == "R":                
                if -9.9 >= self.change_y >= -10 :
                   self.image = self.Salto_Para_Frames_R[0]
                elif (0 > self.change_y >= -9.9):
                    self.image = self.Salto_Para_Frames_R[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Para_Frames_R[2]
                elif 2 < self.change_y <= 10:
                   self.image = self.Salto_Para_Frames_R[3]             
            else:                
                if -9.9 >= self.change_y >= -10 :
                   self.image = self.Salto_Para_Frames_L[0]
                elif (0 > self.change_y >= -9.9):
                    self.image = self.Salto_Para_Frames_L[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Para_Frames_L[2]
                elif 2 < self.change_y <= 10:
                   self.image = self.Salto_Para_Frames_L[3]

        elif self.change_x != 0 and self.change_y != 0:
            self.rect.y += self.change_y
            self.rect.x += self.change_x
            pos = self.rect.x + self.level.world_shift
            if self.direction == "R":
                if -9.9 >= self.change_y >= -10 :
                   self.image = self.Salto_Move_Frames_R[0]
                elif (0 > self.change_y >= -9.9):
                    self.image = self.Salto_Move_Frames_R[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Move_Frames_R[2]
                elif 2 < self.change_y <= 10:
                   self.image = self.Salto_Move_Frames_R[3]
            else:
                if -9.9 >= self.change_y >= -10 :
                   self.image = self.Salto_Move_Frames_L[0]
                elif (0 > self.change_y >= -9.9):
                    self.image = self.Salto_Move_Frames_L[1]
                elif (0 <= self.change_y <= 2):
                    self.image = self.Salto_Move_Frames_L[2]
                elif 2 < self.change_y <= 10:
                   self.image = self.Salto_Move_Frames_L[3]
        
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x