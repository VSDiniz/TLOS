# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:44:15 2016

@author: vini_
"""

# Escolha de Movimentos
        if self.change_x == 0 and self.change_y == 0 :
            self.rect.x += self.change_x
            pos = 120
            if self.direction == "R":
                frame = (pos // 30) % len(self.Para_Frames_R)
                self.image = self.Para_Frames_R[frame]
            else:
                frame = (pos // 30) % len(self.Para_Frames_L)
                self.image = self.Para_Frames_R[frame]
                
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
            # Move Up/Down
        elif self.change_x == 0 and self.change_y != 0:
            self.rect.y += self.change_y
            pos = self.rect.y
            if self.direction == "R":
                frame = (pos // 30) % len(self.Salto_Para_Frames_R)
                self.image = self.Salto_Para_Frames_R[frame]
            else:
                frame = (pos // 30) % len(self.Salto_Para_Frames_L)
                self.image = self.Salto_Para_Frames_L[frame]