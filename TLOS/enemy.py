# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:25:12 2016

@author: vini_
"""

import pygame, constants, spritesheet_functions
from platforms import MovingPlatform

class Boss(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
 
        # Define o vetor velocidade do player
        self.change_x = 0
        self.change_y = 0
        
        # Armazena todas as imagens da animação de descanço esquerda/direita do player
        self.waiting_frames_l = []
        self.waiting_frames_r = []
        
        # Armazena todas as imagens da animação de andar para esquerda/direita do player
        self.walking_frames_l = []
        self.walking_frames_r = []
        
        # Armazena todas as imagens da animação de pular para a esquerda/direita do player
        self.jumping_frames_l = []
        self.jumping_frames_r = []
 
        # Direção que o player está virado
        self.direction = "L"
 
        # Lista de sprites que o player pode esbarrar
        self.level = None
 
        sprite_sheet = spritesheet_functions.SpriteSheet("images/ganon1.png")
        
        # Carrega todas as sprites paradas viradas para a direita
        list1 = [[11, 890, 48, 62],
                 [65, 890, 48, 62],
                 [121, 890, 48, 62],
                 [178, 890, 48, 62]]        
        
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as sprites paradas viradas para a direita e as vira para a esquerda
        list1 = [[178, 890, 48, 62],
                 [121, 890, 48, 62],
                 [65, 890, 48, 62],
                 [11, 890, 48, 62]]        
        
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)        
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        list1 = [[10, 976, 52, 57],
                 [71, 976, 52, 57],
                 [128, 976, 52, 57],
                 [181, 976, 52, 57],
                 [238, 976, 52, 57],
                 [300, 976, 52, 57],
                 [356, 976, 52, 57],
                 [410, 976, 52, 57]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
 
        # Carrega todas as imagens correndo viradas para a direita e as vira para a esquerda
        list1 = [[410, 976, 52, 57],
                 [356, 976, 52, 57],
                 [300, 976, 52, 57],
                 [238, 976, 52, 57],
                 [181, 976, 52, 57],
                 [128, 976, 52, 57],
                 [71, 976, 52, 57],
                 [10, 976, 52, 57]]
                 
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens pulando viradas para a direita numa lista
        list1 = [[15, 1064, 41, 52],
                 [64, 1047, 41, 70],
                 [108, 1047, 41, 70]]
                 
        self.jumping_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens pulando viradas para a direita e as vira para a esquerda
        list1 = [[15, 1064, 41, 52],
                 [64, 1047, 41, 70],
                 [108, 1047, 41, 70]]
                 
        self.jumping_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)        
 
        # Define a sprite que o player começa
        self.image = self.waiting_frames_r[0]
 
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
  
    def update(self):
        # Move o player
        # Gravidade
        self.calc_grav()
        
        # Reproduz a animação de espera
        if self.change_x == 0 and self.change_y == 0:
            self.rect.x += self.change_x
            pos = self.rect.x
            if self.direction == "R":
                frame = (pos // 30) % len(self.waiting_frames_r)
                self.image = self.waiting_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.waiting_frames_l)
                self.image = self.waiting_frames_l[frame]
        
        # Move para esquerda/direita e reproduz a animação de corrida 
        elif self.change_x != 0 and self.change_y == 0:
            self.rect.x += self.change_x
            pos = self.rect.x + self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
 
        # Verifica se existe colisão
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Se o player está indo para a direita, define o lado direito do player
            # para o lado esquerdo do objeto que o acertou
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Se o player estiver indo para a esquerda, faz o oposto
                self.rect.left = block.rect.right
 
        # Move para cima/baixo
        if self.change_x == 0 and self.change_y != 0:
            self.rect.y += self.change_y
            pos = self.rect.y
            
            if self.direction == "R":
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_r[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_r[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_r[2]
                
            else:
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_l[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_l[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_l[2]
                
                
        elif self.change_x != 0 and self.change_y != 0:
             self.rect.y += self.change_y
             self.rect.x += self.change_x
             pos = self.rect.x + self.level.world_shift
             
             if self.direction == "R":
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_r[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_r[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_r[2]
                
             else:
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_l[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_l[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_l[2]
 
        # Verifica se existe colisão
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Redefine a posição do player baseada no topo/fundo do objeto
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Para o movimento vertical do player
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
 
    def calc_grav(self):
        # Calcula o efeito da gravidade
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # Verifica se o player está no chão
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height-52 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height-52
 
    def jump(self):
 
        # Move o player 2 pixels para baixo para verificar se existe uma plataforma
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # Se for possível pular, define a velocidade da subida
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT-52:
            self.change_y = -10
 
    # Movimentos do player:
    def go_left(self):
        # Quando o player vai para a esquerda
        self.change_x = -6
        self.direction = "L"
 
    def go_right(self):
        # Quando o player vai para a direita
        self.change_x = 6
        self.direction = "R"
 
    def stop(self):
        # Quando o player não se move
        self.change_x = 0
        
def boss_hud(screen):
    enemy_health = 800
    boss_name = constants.boss_SF.render("Ganondorf, the Gerudo King", True, constants.WHITE, None)
    boss_name_rect = boss_name.get_rect()
    boss_name_rect.x = 50
    boss_name_rect.y = 515
    screen.blit(boss_name, boss_name_rect)

    pygame.draw.rect(screen, constants.ORANGE, (50, 530, enemy_health, 10))