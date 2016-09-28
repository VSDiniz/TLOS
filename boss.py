# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:25:12 2016

@author: vini_
"""

import pygame, constants, spritesheet_functions
#from platforms import MovingPlatform

class Boss(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
        
        # Define variáveis de características do boss
        self.maxhealth = 1000
        self.health = 1000
        self.stamina = 50
        
        # Define variáveis de estado do boss
        self.live = True
        self.on_ground = True
        self.defending = False
        self.takedmg = False
        self.jumping = False
        self.guard = True
        self.latk = False
        self.hatk = False
        self.rolling = False
        self.parrying = False
        self.riposting = False
        
        # Define outras variáveis
        self.world_shift = 0
        self.start_clocker = False
        
        # Define o vetor velocidade do boss
        self.change_x = 0
        self.change_y = 0
        
        # Armazena todas as imagens da animação de descanço esquerda/direita do boss
        self.waiting_frames_l = []
        self.waiting_frames_r = []
        
        # Armazena todas as imagens da animação de andar para esquerda/direita do boss
        self.walking_frames_l = []
        self.walking_frames_r = []
        
        # Armazena todas as imagens da animação de pular para a esquerda/direita do boss
        self.jumping_frames_l = []
        self.jumping_frames_r = []
        
        # Armazena todas as imagens da animação de defesa para a esquerda/direita
        self.defense_frames_l = []
        self.defense_frames_r = []
        
        # Armazena todas as imagens da animação de quebra de guarda para a esquerda/direita
        self.guardbreak_frames_l = []
        self.guardbreak_frames_r = []
        
        # Armazena todas as imagens da animação de parry para a esquerda/direita
        self.parry_frames_l = []
        self.parry_frames_r = []        
        
        # Armazena todas as imagens da animação de riposte para a esquerda/direita
        self.riposte_frames_l = []
        self.riposte_frames_r = []
        
        # Armazena todas as imagens da animação de rolar para a esquerda/direita
        self.roll_frames_l = []
        self.roll_frames_r = []
        
        # Armazena todas as imagens da animação de ataque leve para a esquerda/direita
        self.lightatk_frames_l = []
        self.lightatk_frames_r = []
        
        # Armazena todas as imagens da animação de ataque pesado para a esquerda/direita
        self.heavyatk_frames_l = []
        self.heavyatk_frames_r = []
        
        # Armazena todas as imagens da animação de tomar dano para a esquerda/direita
        self.takedmg_frames_l = []
        self.takedmg_frames_r = []

        # Armazena todas as imagens da animação de morte para a esquerda/direita
        self.dead_frames_l = []
        self.dead_frames_r = []
 
        # Direção que o boss está virado
        self.direction = "L"
 
        # Lista de sprites que o player pode esbarrar
        self.level = None
 
        self.delay = self.i = self.s = 0        
        sprite_sheet = spritesheet_functions.SpriteSheet("images/ganon7.png")
        
        
        # Carrega todas as sprites paradas viradas para a direita/esquerda
        "Esperar"
#        list1 = [[11, 894, 48, 62],
#                 [65, 894, 48, 62],
#                 [121, 894, 48, 62],
#                 [178, 894, 48, 62],
#                 [121, 894, 48, 62],
#                 [65, 894, 48, 62]]
        list1 = [[0, 0, 113, 73],
                 [120, 0, 113, 73],
                 [240, 0, 113, 73],
                 [360, 0, 113, 73],
                 [240, 0, 113, 73],
                 [120, 0, 113, 73]]
                 
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)               
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        "Correr"
#        list1 = [[10, 976, 52, 62],
#                 [71, 976, 52, 62],
#                 [128, 976, 52, 62],
#                 [181, 976, 52, 62],
#                 [238, 976, 52, 62],
#                 [300, 976, 52, 62],
#                 [356, 976, 52, 62],
#                 [410, 976, 52, 62]]
        list1 = [[120, 80, 113, 73],
                 [240, 80, 113, 73],
                 [360, 80, 113, 73],
                 [480, 80, 113, 73],
                 [600, 80, 113, 73],
                 [0, 160, 113, 73],
                 [120, 160, 113, 73],
                 [240, 160, 113, 73]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
 
        # Carrega todas as imagens correndo viradas para a direita e as vira para a esquerda
#        list1 = [[410, 976, 52, 62],
#                 [356, 976, 52, 62],
#                 [300, 976, 52, 62],
#                 [238, 976, 52, 62],
#                 [181, 976, 52, 62],
#                 [128, 976, 52, 62],
#                 [71, 976, 52, 62],
#                 [10, 976, 52, 62]]
        list1 = [[240, 160, 113, 73],
                 [120, 160, 113, 73],
                 [0, 160, 113, 73],
                 [600, 80, 113, 73],
                 [480, 80, 113, 73],
                 [360, 80, 113, 73],
                 [240, 80, 113, 73],
                 [120, 80, 113, 73]]
                 
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens pulando viradas para a direita numa lista
        "Pular"
#        list1 = [[15, 1068, 41, 52],
#                 [64, 1051, 41, 70],
#                 [108, 1051, 41, 70]]
        list1 = [[480, 0, 113, 73],
                 [600, 0, 113, 73],
                 [0, 80, 113, 73]]
                 
        self.jumping_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.jumping_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
#==============================================================================
#         
#==============================================================================
        # Carrega todas as imagens de defesa viradas para a direita numa lista
        "Defender"
#        list1 = [[537, 1625, 43, 60]]
        list1 = [[0, 320, 113, 73]]
        
        self.defense_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.defense_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)         
        
        # Carrega todas as imagens de quebra de guarda viradas para a direita numa lista
        "Quebra de guarda"
        list1 = [[16, 2113, 45, 62]]
#        list1 = [[120, 320, 113, 73]]
        
        self.guardbreak_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # vira as imagens para a esquerda
        self.guardbreak_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de parry viradas para a direita numa lista
        "Parry"
        list1 = [[418, 1618, 49, 67],
                 [479, 1615, 40, 70]]
#        list1 = [[240, 320, 113, 73],
#                 [360, 320, 113, 73],]
                 
        self.parry_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.parry_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de riposte viradas para a direita numa lista
        "Riposte"
        list1 = [[63, 1792, 45, 59],
                 [108, 1793, 58, 58],
                 [169, 1778, 58, 73]]
#        list1 = [[480, 320, 113, 73],
#                 [600, 320, 113, 73],
#                 [0, 400, 113, 73]]
        
        self.riposte_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.riposte_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de rolar viradas para a direita numa lista        
        "Rolar"
#        list1 = [[237, 1298, 62, 68]]
        list1 = [[600, 240, 113, 73]]
        
        self.roll_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.roll_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de ataque leve viradas para a direita numa lista
        "Ataque leve"
#        list1 = [[12, 1149, 45, 58],
#                 [70, 1149, 53, 58],
#                 [140, 1150, 62, 58],
#                 [217, 1149, 66, 58],
#                 [217, 1149, 66, 58],
#                 [367, 1150, 50, 58],
#                 [423, 1150, 79, 58],
#                 [12, 1149, 45, 58],
#                 [70, 1149, 53, 58]]
        list1 = [[360, 160, 113, 73],
                 [480, 160, 113, 73],
                 [600, 160, 113, 73],
                 [0, 240, 113, 73],
                 [0, 240, 113, 73],
                 [240, 240, 113, 73],
                 [360, 240, 113, 73],
                 [360, 160, 113, 73],
                 [480, 160, 113, 73]]
                 
        self.lightatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.lightatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de ataque pesado viradas para a direita numa lista
        "Ataque pesado"
#        list1 = [[12, 1149, 45, 58],
#                 [70, 1149, 53, 58],
#                 [140, 1150, 62, 58],
#                 [620, 1150, 89, 58],
#                 [217, 1149, 66, 58],
#                 [367, 1150, 50, 58],
#                 [499, 1027, 105, 111],
#                 [12, 1149, 45, 58],
#                 [70, 1149, 53, 58]]
        list1 = [[360, 160, 113, 73],
                 [480, 160, 113, 73],
                 [600, 160, 113, 73],
                 [0, 240, 113, 73],
                 [120, 240, 113, 73],
                 [120, 240, 113, 73],
                 [240, 240, 113, 73],
                 [480, 240, 113, 73],
                 [480, 240, 113, 73],
                 [480, 240, 113, 73],
                 [360, 160, 113, 73],
                 [480, 160, 113, 73],
                 [480, 160, 113, 73]]
                 
        self.heavyatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.heavyatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens tomando dano viradas para a direita numa lista
        "Tomar dano"
        list1 = [[121, 2116, 47, 59]]
#        list1 = [[120, 400, 113, 73]]
        
        self.takedmg_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.takedmg_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens morrendo viradas para a direita numa lista
        "Morrer"
        list1 = [[217, 529,  62, 36],
                 [284, 524, 50, 50],
                 [338, 570, 64, 16]]
#        list1 = [[240, 400, 113, 73],
#                 [360, 400, 113, 73],
#                 [480, 400, 113, 73]]
                 
        self.dead_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.dead_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)

        # Define a sprite que o boss começa
        self.image = self.waiting_frames_r[0]
 
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
  
    def update(self):
        # Move o boss
        # Gravidade
        self.calc_grav()
        
        # Reproduz a animação de espera           
        if self.possible("wait"):
            if self.change_x == 0 and self.change_y == 0:
                
                if self.delay > constants.FPS/len(self.waiting_frames_r):
                    self.delay = 0
                    if self.direction == "R":
                        self.image = self.waiting_frames_r[self.i]
                    else:
                        self.image = self.waiting_frames_l[self.i]
                    if self.i >= len(self.waiting_frames_r) - 1:
                        self.i = 0
                    else:
                        self.i += 1            
                else:
                   self.delay += 1

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

        # Morte do boss        
        if not self.live:
            self.change_y = 10
            if self.direction == "R":
                self.image = self.dead_frames_r[0]
            else:
                self.image = self.dead_frames_l[0]
 
        # Verifica se existe colisão
#        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#        for block in block_hit_list:
#            # Se o player está indo para a direita, define o lado direito do boss
#            # para o lado esquerdo do objeto que o acertou
#            if self.change_x > 0:
#                self.rect.right = block.rect.left
#            elif self.change_x < 0:
#                # Se o player estiver indo para a esquerda, faz o oposto
#                self.rect.left = block.rect.right
                
        block_hit_list =  self.level.platform_list
        for block in block_hit_list:
            if pygame.sprite.collide_rect(self, block):                
                if not self.jumping:
                    if self.rect.bottom < block.rect.bottom and self.rect.bottom > block.rect.top:
                        if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                            self.rect.right = block.rect.left
                        if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                            self.rect.left = block.rect.right
                    if self.rect.top > block.rect.top and self.rect.top < block.rect.bottom:
                        if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                            self.rect.right = block.rect.left
                        if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                            self.rect.left = block.rect.right
                    if self.rect.top <= block.rect.top and self.rect.bottom >= block.rect.bottom:
                        if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                            self.rect.right = block.rect.left
                        if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                            self.rect.left = block.rect.right
                if self.rect.top >= block.rect.top and self.rect.bottom <= block.rect.bottom:
                    if self.rect.left < block.rect.left and self.rect.right > block.rect.left:
                        self.rect.right = block.rect.left
                    if self.rect.right > block.rect.right and self.rect.left < block.rect.right:
                        self.rect.left = block.rect.right
 
#        # Move para cima/baixo
#        if self.change_x == 0 and self.change_y != 0:
#            self.rect.y += self.change_y
#            pos = self.rect.y
#            
#            if self.direction == "R":
#                if (-10 <= self.change_y <= -9.9):
#                    self.image = self.jumping_frames_r[0]
#                elif (-9.9 < self.change_y <= 2):
#                    self.image = self.jumping_frames_r[1]
#                elif (2 < self.change_y <= 10):
#                   self.image = self.jumping_frames_r[2]
#                
#            else:
#                if (-10 <= self.change_y <= -9.9):
#                    self.image = self.jumping_frames_l[0]
#                elif (-9.9 < self.change_y <= 2):
#                    self.image = self.jumping_frames_l[1]
#                elif (2 < self.change_y <= 10):
#                   self.image = self.jumping_frames_l[2]
#                
#                
#        elif self.change_x != 0 and self.change_y != 0:
#             self.rect.y += self.change_y
#             self.rect.x += self.change_x
#             pos = self.rect.x + self.level.world_shift
#             
#             if self.direction == "R":
#                if (-10 <= self.change_y <= -9.9):
#                    self.image = self.jumping_frames_r[0]
#                elif (-9.9 < self.change_y <= 2):
#                    self.image = self.jumping_frames_r[1]
#                elif (2 < self.change_y <= 10):
#                   self.image = self.jumping_frames_r[2]
#                
#             else:
#                if (-10 <= self.change_y <= -9.9):
#                    self.image = self.jumping_frames_l[0]
#                elif (-9.9 < self.change_y <= 2):
#                    self.image = self.jumping_frames_l[1]
#                elif (2 < self.change_y <= 10):
#                   self.image = self.jumping_frames_l[2]
                   
        # Move para cima/baixo
        if self.change_y != 0:
            self.rect.y += self.change_y
            self.rect.x += self.change_x
                 
            if self.direction == "R" and self.jumping == True:
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_r[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_r[1]
                elif (2 < self.change_y <= 10):
                    self.image = self.jumping_frames_r[2]
                    
            elif self.direction == "L" and self.jumping == True :
                if (-10 <= self.change_y <= -9.9):
                    self.image = self.jumping_frames_l[0]
                elif (-9.9 < self.change_y <= 2):
                    self.image = self.jumping_frames_l[1]
                elif (2 < self.change_y <= 10):
                    self.image = self.jumping_frames_l[2]
 
        # Verifica se existe colisão
#        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#        for block in block_hit_list:
# 
#            # Redefine a posição do player baseada no topo/fundo do objeto
#            if self.change_y > 0:
#                self.rect.bottom = block.rect.top
#            elif self.change_y < 0:
#                self.rect.top = block.rect.bottom
# 
#            # Para o movimento vertical do boss
#            self.change_y = 0
# 
#            if isinstance(block, MovingPlatform):
#                self.rect.x += block.change_x
        self.on_ground = False
        block_hit_list = self.level.platform_list
        pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if pygame.sprite.collide_rect(self,block):
                if self.rect.right > block.rect.left and self.rect.left < block.rect.right:
                    if self.rect.bottom > block.rect.top and (self.rect.bottom - 10) < block.rect.top:
                        if self.change_y > 0 and not self.on_ground:
                            self.rect.bottom = block.rect.top
                            self.on_ground = True
                            self.jumping = False
                            self.change_y = 0
                    if self.rect.top < block.rect.bottom and (self.rect.top + 10) > block.rect.bottom:
                        if self.change_y < 0 and not self.on_ground:
                            self.rect.top = block.rect.bottom
                
        self.clocker()
        if self.live:
            self.take_dmg()
            if self.guard and not self.jumping:
                if self.stamina > 0:
                    self.parry()
                    self.riposte()
                    self.roll()
                    self.light_atk()
                    self.heavy_atk()
            
    def calc_grav(self):
        # Calcula o efeito da gravidade
        if self.change_y == 0:
            if self.on_ground:
                self.change_y = 0
            else:
                self.change_y = 1
        else:
            self.jumping = True
            self.change_y += .35
 
        # Verifica se o boss está no chão
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height - 47 + (1000) and self.change_y >= 0:
            self.change_y = 0
            #self.rect.y = constants.SCREEN_HEIGHT - self.rect.height-45 +(1000)
            self.live = False
            self.health = 0
            self.jumping = False
 
    def jump(self):
 
        # Move o boss 2 pixels para baixo para verificar se existe uma plataforma
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # Se for possível pular, define a velocidade da subida
        if len(platform_hit_list) > 0:
            self.change_y = -10
            self.jumping = True
            self.on_ground = False
 
    # Movimentos do boss:
    def go_left(self):
        # Quando o boss vai para a esquerda
        self.change_x = -6
        self.direction = "L"
 
    def go_right(self):
        # Quando o boss vai para a direita
        self.change_x = 6
        self.direction = "R"
 
    def stop(self):
        # Quando o boss não se move
        self.change_x = 0
        
    
#==============================================================================
#  Mecânicas do boss
#==============================================================================

    # Coloca o boss em posição de defesa
    def defend(self):
        self.defending = True
        self.jumping = False
        if self.direction == "R":
            self.image = self.defense_frames_r[0]
            self.jumping = False
        else:
            self.image = self.defense_frames_l[0]
            self.jumping = False
    
    # Quebra a guarda do boss
    def guard_break(self):
        self.guard = False
        if self.direction == "R":
            self.image = self.guardbreak_frames_r[0]
        else:
            self.image = self.guardbreak_frames_l[0]

    # Desvia um ataque e quebra guarda do player
    def parry(self):
        if self.parrying:
            self.change_x = 0
            if constants.d1 > constants.FPS/len(self.parry_frames_r):
                constants.d1 = 0
                if self.direction == "R":
                    self.image = self.parry_frames_r[constants.i]
                else:
                    self.image = self.parry_frames_l[constants.i]
                if constants.i >= len(self.parry_frames_r) - 1:
                    constants.i = 0
                    self.parrying = False
                else: 
                    constants.i += 1
            else: 
                constants.d1 += 1
    
    # Ataque crítico
    def riposte(self):
        if self.riposting:
            self.change_x = 0
            if constants.d1 > constants.FPS/len(self.riposte_frames_r):
                constants.d1 = 0
                if self.direction == "R":
                    self.image = self.riposte_frames_r[constants.i]
                else:
                    self.image = self.riposte_frames_l[constants.i]
                if constants.i >= len(self.riposte_frames_r) - 1:
                    constants.i = 0
                    self.riposting = False
                else: 
                    constants.i += 1
            else: 
                constants.d1 += 1

    # Faz o boss desviar
    def roll(self):
        rolling_speed = 8
        roll_dt = 4
        if self.rolling and constants.boss_roll_frames > 0:
            if self.direction == "R":
                self.rect.x += rolling_speed
                constants.boss_roll_frames -= roll_dt
                self.image = self.roll_frames_r[0]
                
            else:
                self.rect.x -= rolling_speed
                constants.boss_roll_frames -= roll_dt
                self.image = self.roll_frames_l[0]
        self.rolling = False
        
    def active_roll(self):
        constants.boss_roll_frames += 85
    
    # Ataque leve
    def light_atk(self):
        if self.latk:
            self.change_x = 0
            if constants.d1 > constants.FPS/len(self.lightatk_frames_r):
                constants.d1 = 0
                if self.direction == "R":
                    self.image = self.lightatk_frames_r[constants.i]
                else:
                    self.image = self.lightatk_frames_l[constants.i]
                if constants.i >= len(self.lightatk_frames_r) - 1:
                    constants.i = 0
                    self.latk = False
                else: 
                    constants.i += 1
            else: 
                constants.d1 += 1
    
    # Ataque pesado
    def heavy_atk(self):
        if self.hatk:
            self.change_x = 0
            if constants.d1 > constants.FPS/len(self.heavyatk_frames_r):
                constants.d1 = 0
                if self.direction == "R":
                    self.image = self.heavyatk_frames_r[constants.i]
                else:
                    self.image = self.heavyatk_frames_l[constants.i]
                if constants.i >= len(self.heavyatk_frames_r) - 1:
                    constants.i = 0
                    self.hatk = False
                else: 
                    constants.i += 1
            else: 
                constants.d1 += 1
            
    # Calcula o dano recebido pelo boss
    def calc_damage(self, damage):
        # Verifica se o boss está defendendo
        if self.guard:
            if self.defending:
                self.calc_stamina(damage/2) # Reduz stamina
                if self.stamina <= 0:
                    self.stamina = 0
                    self.guard_break() # Quebra guarda
                                        
            else:
                if self.direction == "R":
                    self.image = self.takedmg_frames_r[0]
                else:
                    self.image = self.takedmg_frames_l[0]
                if self.health - damage > 0:
                    self.health -= damage # Reduz vida
                else:
                    self.health = 0
#        else:
#            self.health -= damage*2                    
                    
        if self.health <= 0:
            self.live = False
                
    def take_dmg(self):
        self.clocker_rt = 1
        if not self.defending and self.takedmg:
#            self.rect.x -= 0.001
            if constants.delay > constants.FPS/len(self.takedmg_frames_r):
                constants.delay = 0
                if self.direction == "R":
                    self.image = self.takedmg_frames_r[0]
                else:
                    self.image = self.takedmg_frames_l[0]
                if constants.i >= len(self.takedmg_frames_r) - 1:
                    constants.i = 0
                    self.takedmg = False
                    self.guard = True
                else:
                    constants.i += 1
            else:
                constants.delay += 1
                
    # Calcula a stamina gasta pelo boss
    def calc_stamina(self, stm_cost):
        if self.stamina > 0:        
            self.stamina -= stm_cost
        else:
            self.stamina = 0
            
    # Regenera stamina usada
    def stamina_regen(self):
        # Calcula a regeneração de stamina do boss
        self.clocker_rt = 1
        if not self.start_clocker:
            if not self.defending:
                if self.stamina < self.maxstamina:
                    self.stamina += 1
                else:
                    self.stamina = self.maxstamina
            else:
                if self.stamina < self.maxstamina:
                    self.stamina += 0.1
                else:
                    self.stamina = self.maxstamina
            
    # Faz o boss voltar a vida
    def reborn(self):
        self.live = True
        self.guard = True
        self.defending = False
        self.health = self.maxhealth
        self.rect.y = 50
        self.rect.x = 200
        
    def clocker(self):
        if self.start_clocker:
            if constants.k > constants.FPS:
                constants.k = 0
                self.start_clocker = False
            else:
                constants.k += self.clocker_rt
                
    def shift_world(self, shift_x):
        # Desloca o world quando o player se move
        # Mantém controle de quanto o world se desloca
        self.world_shift += shift_x
 
        # Passa por toda a lista de sprites e altera
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
                
    def possible(self, event):
        if event == "wait":
            if self.live and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "move":
            if self.live and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "jump":
            if self.live and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting and (not self.jumping or self.on_ground):
                return True
        elif event == "defend":
            if self.live and not self.jumping and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "latk":
            if self.live and not self.jumping and not self.defending and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "hatk":
            if self.live and not self.jumping and not self.defending and not self.latk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "parry":
            if self.live and not self.jumping and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.riposting:
                return True
        elif event == "riposte":
            if self.live and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying:
                return True
        elif event == "roll":
            if self.live and not self.jumping and not self.latk and not self.hatk and not self.takedmg and not self.parrying and not self.riposting:
                return True
        else:
            return False
        
    def boss_hud(self, screen):
        boss_name = constants.soulsFont_P.render("Ganondorf, the Great King of Evil", True, constants.WHITE, None)
        boss_name_rect = boss_name.get_rect()
        boss_name_rect.x = 50
        boss_name_rect.y = 565
        screen.blit(boss_name, boss_name_rect)

        pygame.draw.rect(screen, constants.WHITE, (49, 579, (0.8*self.maxhealth)+2, 12))
        pygame.draw.rect(screen, constants.GRAY, (50, 580, 0.8*self.maxhealth, 10))
        if self.health > 0:
            pygame.draw.rect(screen, constants.ORANGE, (850-(0.8*self.health), 580, 0.8*self.health, 10))
        
# Mostra tela de vitória        
def dead_screen(screen, boss):
    s = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
    s.fill((255, 255, 255, 60))
    screen.blit(s, (0, 0))
    you_win_txt = constants.soulsFont_M.render("VICTORY ACHIEVED", True, constants.YELLOW, None)
    you_win_rect = you_win_txt.get_rect()
    you_win_rect.centerx = constants.SCREEN_WIDTH/2
    you_win_rect.centery = constants.SCREEN_HEIGHT/2
    screen.blit(you_win_txt, you_win_rect)
    
    for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit() # Fecha a janela se o usuário clicar em fechar
                quit()
            if event.type == pygame.KEYDOWN:
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                    pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                    quit()
                if event.key == pygame.K_BACKSPACE:
                    boss.reborn()