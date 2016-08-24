# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:25:12 2016

@author: vini_
"""

import pygame, constants
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Enemy(pygame.sprite.Sprite):
 
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
 
        sprite_sheet = SpriteSheet("images/ganon1.png")
        
        # Carrega todas as sprites paradas viradas para a direita
        image_wait = sprite_sheet.get_image(11, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_r.append(image_wait)
        image_wait = sprite_sheet.get_image(65, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_r.append(image_wait)
        image_wait = sprite_sheet.get_image(121, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_r.append(image_wait)
        image_wait = sprite_sheet.get_image(178, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_r.append(image_wait)
        
        # Carrega todas as sprites paradas viradas para a direita e as vira para a esquerda
        image_wait = sprite_sheet.get_image(11, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.flip(image_wait, True, False)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_l.append(image_wait)
        image_wait = sprite_sheet.get_image(65, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.flip(image_wait, True, False)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_l.append(image_wait)
        image_wait = sprite_sheet.get_image(121, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.flip(image_wait, True, False)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_l.append(image_wait)
        image_wait = sprite_sheet.get_image(178, 890, 48, 62, constants.DARKBLUE)
        image_wait = pygame.transform.flip(image_wait, True, False)
        image_wait = pygame.transform.scale2x(image_wait)
        self.waiting_frames_l.append(image_wait)
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        image = sprite_sheet.get_image(10, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(71, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(128, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(181, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(238, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(300, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(356, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(410, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
 
        # Carrega todas as imagens correndo viradas para a direita e as vira para a esquerda
        image = sprite_sheet.get_image(410, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(356, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(300, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(238, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(181, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(128, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(71, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(10, 976, 52, 57, constants.DARKBLUE)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        
        # Carrega todas as imagens pulando viradas para a direita numa lista
        image_jump = sprite_sheet.get_image(15, 1064, 41, 52, constants.DARKBLUE)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_r.append(image_jump)
        image_jump = sprite_sheet.get_image(64, 1047, 41, 70, constants.DARKBLUE)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_r.append(image_jump)
        image_jump = sprite_sheet.get_image(108, 1047, 41, 70, constants.DARKBLUE)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_r.append(image_jump)
        
        # Carrega todas as imagens pulando viradas para a direita e as vira para a esquerda
        image_jump = sprite_sheet.get_image(15, 1064, 41, 52, constants.DARKBLUE)
        image_jump = pygame.transform.flip(image_jump, True, False)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_l.append(image_jump)
        image_jump = sprite_sheet.get_image(64, 1047, 41, 70, constants.DARKBLUE)
        image_jump = pygame.transform.flip(image_jump, True, False)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_l.append(image_jump)
        image_jump = sprite_sheet.get_image(108, 1047, 41, 70, constants.DARKBLUE)
        image_jump = pygame.transform.flip(image_jump, True, False)
        image_jump = pygame.transform.scale2x(image_jump)
        self.jumping_frames_l.append(image_jump)
 
        # Define a sprite que o player começa
        self.image_wait = self.waiting_frames_r[0]
        self.image = self.walking_frames_r[0]
        self.image_jump = self.jumping_frames_r[0]
 
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
        self.rect_jump = self.image_jump.get_rect()
        self.rect_wait = self.image_wait.get_rect()
  
    def update(self):
        # Move o player
        # Gravidade
        self.calc_grav()
        
        # Reproduz a animação de espera
        if self.change_x == 0 and self.change_y == 0:
            self.rect.x += self.change_x
            pos = 120
            if self.direction == "R":
                frame = (pos // 30) % len(self.waiting_frames_r)
                self.image = self.waiting_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.waiting_frames_l)
                self.image = self.waiting_frames_l[frame]
 
        elif self.change_x != 0 and self.change_y == 0:
            # Move para esquerda/direita e reproduz a animação de corrida
            self.rect.x += self.change_x
            pos = self.rect.x + self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
                
        elif self.change_x == 0 and self.change_y != 0:
            # Reproduz animação de pulo
            self.rect.y += self.change_y
            pos = self.rect.y
            
            if self.direction == "R":
                frame = (pos // 30) % len(self.jumping_frames_r)
                self.image = self.jumping_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.jumping_frames_l)
                self.image = self.jumping_frames_l[frame]
        elif self.change_x != 0 and self.change_y != 0:
             self.rect.y += self.change_y
             self.rect.x += self.change_x
             pos = self.rect.x + self.level.world_shift
             
             if self.direction == "R":
                frame = (pos // 30) % len(self.jumping_frames_r)
                self.image = self.jumping_frames_r[frame]
             else:
                frame = (pos // 30) % len(self.jumping_frames_l)
                self.image = self.jumping_frames_l[frame]
 
        # Verifica se existe colisão
        """block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Se o player está indo para a direita, define o lado direito do player
            # para o lado esquerdo do objeto que o acertou
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Se o player estiver indo para a esquerda, faz o oposto
                self.rect.left = block.rect.right"""
 
        # Move para cima/baixo
        self.rect.y += self.change_y
 
        """# Verifica se existe colisão
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
                self.rect.x += block.change_x"""
 
    def calc_grav(self):
        # Calcula o efeito da gravidade
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # Verifica se o player está no chão
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
 
        # Move o player 2 pixels para baixo para verificar se existe uma plataforma
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # Se for possível pular, define a velocidade da subida
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
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