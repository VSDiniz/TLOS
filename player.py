# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:49:19 2016

@author: vini_
"""

import pygame, constants, spritesheet_functions, sounds, os
 
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
        
        # Define variáveis de características do player
        self.maxhealth = 100
        self.health = 100
        self.maxstamina = 50
        self.stamina = 50
        self.dmg_r = 0
        self.dmg_d = 0
        self.estus_rn = 5
        self.estus_used = 0
        self.estus_regen = 0
        self.rolling_speed = 10
        self.roll_dt = 5
        self.look_dist = 600
        
        # Define variáveis de estado do player
        self.live = True
        self.on_ground = True
        self.recovering = False
        self.defending = False
        self.takedmg = False
        self.dealdmg = False
        self.jumping = False
        self.guard = True
        self.latk = False
        self.hatk = False
        self.rolling = False
        self.parrying = False
        self.riposting = False
        
        # Define outras variáveis
        self.start_clocker = False
        self.enemies = []
        self.a = self.b = self.c = self.d = self.e = self.f = self.g = self.h = self.i = \
        self.j = self.k = self.l = self.m = 0
 
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

        # Armazena todas as imagens da animação de recuperar vida para a esquerda/direita
        self.estus_frames_l = []
        self.estus_frames_r = []

        # Armazena todas as imagens da animação de tomar dano para a esquerda/direita
        self.takedmg_frames_l = []
        self.takedmg_frames_r = []

        # Armazena todas as imagens da animação de morte para a esquerda/direita
        self.dead_frames_l = []
        self.dead_frames_r = []
 
        # Direção que o player está virado
        self.direction = "R"
 
        # Lista de sprites que o player pode esbarrar
        self.level = None
        
        sprite_sheet = spritesheet_functions.SpriteSheet("images/link_2.png")
        
        # Carrega todas as sprites paradas viradas para a direita numa lista
        "Esperar"
        list1 = [[0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [0, 0, 80, 60],
                 [80, 0, 80, 60],
                 [160, 0, 80, 60],
                 [80, 0, 80, 60]]
        
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        "Correr"
        list1 = [[320, 300, 80, 60],
                 [240, 300, 80, 60],
                 [160, 300, 80, 60],
                 [80, 300, 80, 60],
                 [0, 300, 80, 60],
                 [320, 240, 80, 60],
                 [240, 240, 80, 60],
                 [160, 240, 80, 60],
                 [80, 240, 80, 60],
                 [0, 240, 80, 60]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
 
        # Carrega todas as imagens correndo viradas para a direita e as vira para a esquerda
        list1 = [[0, 240, 80, 60],
                 [80, 240, 80, 60],
                 [160, 240, 80, 60],
                 [240, 240, 80, 60],
                 [320, 240, 80, 60],
                 [0, 300, 80, 60],
                 [80, 300, 80, 60],
                 [160, 300, 80, 60],
                 [240, 300, 80, 60],
                 [320, 300, 80, 60]]
                 
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens pulando viradas para a direita numa lista
        "Pular"
        list1 = [[0, 60, 80, 60],
                 [80, 60, 80, 60],
                 [160, 60, 80, 60]]
                 
        self.jumping_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.jumping_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)

        # Carrega todas as imagens de defesa viradas para a direita numa lista
        "Defender"
        list1 = [[320, 120, 80, 60]]
        
        self.defense_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.defense_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de quebra de guarda viradas para a direita numa lista
        "Quebra de guarda"
        list1 = [[0, 360, 80, 60]]
        
        self.guardbreak_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # vira as imagens para a esquerda
        self.guardbreak_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de parry viradas para a direita numa lista
        "Parry"
        list1 = [[320, 0, 80, 60],
                 [320, 180, 80, 60],
                 [320, 180, 80, 60],
                 [320, 180, 80, 60],
                 [320, 180, 80, 60],
                 [320, 180, 80, 60],
                 [320, 180, 80, 60]]
                 
        self.parry_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.parry_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de riposte viradas para a direita numa lista
        "Riposte"
        list1 = [[320, 0, 80, 60],
                 [80, 180, 80, 60],
                 [0, 180, 80, 60],
                 [0, 180, 80, 60]]
        
        self.riposte_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.riposte_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de rolar viradas para a direita numa lista
        "Rolar"
        list1 = [[80, 360, 80, 60]]
        
        self.roll_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.roll_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de ataque leve viradas para a direita numa lista
        "Ataque leve"
        list1 = [[240, 0, 80, 60],
                 [240, 180, 80, 60],
                 [240, 180, 80, 60],
                 [240, 180, 80, 60]]
                 
        self.lightatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.lightatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de ataque pesado viradas para a direita numa lista
        "Ataque pesado"
        list1 = [[240, 0, 80, 60],
                 [240, 0, 80, 60],
                 [80, 180, 80, 60],
                 [80, 180, 80, 60],
                 [80, 180, 80, 60],
                 [0, 180, 80, 60],
                 [0, 180, 80, 60]]
        
        self.heavyatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.heavyatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens do uso de estus viradas para a direita numa lista
        "Usar estus"
        list1 = [[160, 360, 80, 60],
                 [320, 360, 80, 60],
                 [240, 360, 80, 60],
                 [320, 360, 80, 60],
                 [240, 360, 80, 60],
                 [320, 360, 80, 60]]
        
        self.estus_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.estus_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens tomando dano viradas para a direita numa lista
        "Tomar dano"
        list1 = [[240, 60, 80, 60]]
        
        self.takedmg_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.takedmg_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens morrendo viradas para a direita numa lista
        "Morrer"
        list1 = [[320, 60,  80, 60]]
        
        self.dead_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.dead_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)


        # Define a sprite que o player começa
        self.image = self.waiting_frames_r[0]
        
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
        
#==============================================================================
#         Animações do player
#==============================================================================
    
    # Reproduz a animação de espera
    def ani_wait(self):
        if self.a > 120:
            self.a = 0
            self.guard = True
        else:
            self.a += 1
        if self.change_x == 0 and self.change_y == 0:
            
            if self.b > constants.FPS/len(self.waiting_frames_r):
                self.b = 0
                if self.direction == "R":
                    self.image = self.waiting_frames_r[self.c]
                else:
                    self.image = self.waiting_frames_l[self.c]
                if self.c >= len(self.waiting_frames_r) - 1:
                    self.c = 0
                else:
                    self.c += 1
            else:
               self.b += 1
    
    # Move para esquerda/direita e reproduz a animação de corrida
    def ani_walk(self):
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
    
    # Reproduz a animação de pulo
    def ani_jump(self):
        if self.direction == "R" and self.jumping == True:
            if (-12 <= self.change_y <= 0):
                self.image = self.jumping_frames_r[0]
            elif (0 < self.change_y <= 2):
                self.image = self.jumping_frames_r[1]
            elif (2 < self.change_y <= 12):
                self.image = self.jumping_frames_r[2]
                
        elif self.direction == "L" and self.jumping == True :
            if (-12 <= self.change_y <= 0):
                self.image = self.jumping_frames_l[0]
            elif (0 < self.change_y <= 2):
                self.image = self.jumping_frames_l[1]
            elif (2 < self.change_y <= 12):
                self.image = self.jumping_frames_l[2]
    
    # Reproduz animação de defesa
    def ani_defend(self):
        if self.direction == "R":
            self.image = self.defense_frames_r[0]
        else:
            self.image = self.defense_frames_l[0]
    
    # Reproduz animação de quebra de guarda
    def ani_guardbreak(self):
        if self.direction == "R":
            self.image = self.guardbreak_frames_r[0]
        else:
            self.image = self.guardbreak_frames_l[0]
    
    # Reproduz animação de parry
    def ani_parry(self):
        if self.d > constants.FPS/len(self.parry_frames_r):
            self.d = 0
            if self.direction == "R":
                self.image = self.parry_frames_r[self.e]
            else:
                self.image = self.parry_frames_l[self.e]
            if self.e >= len(self.parry_frames_r) - 1:
                self.e = 0
                self.parrying = False
            else: 
                self.e += 1
        else: 
            self.d += 1
    
    # Reproduz a animação de riposte
    def ani_riposte(self):
        if self.f > constants.FPS/len(self.riposte_frames_r):
            self.f = 0
            if self.direction == "R":
                self.image = self.riposte_frames_r[self.g]
            else:
                self.image = self.riposte_frames_l[self.g]
            if self.g >= len(self.riposte_frames_r) - 1:
                self.g = 0
                self.riposting = False
            else: 
                self.g += 1
        else: 
            self.f += 1
    
    # Reproduz animação de roll
    def ani_roll(self):
        if self.direction == "R":
            self.rect.x += self.rolling_speed
            constants.player_roll_frames -= self.roll_dt
            self.image = self.roll_frames_r[0]
            
        else:
            self.rect.x -= self.rolling_speed
            constants.player_roll_frames -= self.roll_dt
            self.image = self.roll_frames_l[0]
    
    # Reproduz animação de ataque leve
    def ani_latk(self):
        if self.h > constants.FPS/len(self.lightatk_frames_r):
            self.h = 0
            if self.direction == "R":
                self.image = self.lightatk_frames_r[self.i]
            else:
                self.image = self.lightatk_frames_l[self.i]
            if self.i >= len(self.lightatk_frames_r) - 1:
                self.i = 0
                self.latk = False
            else:
                self.i += 1
            if self.i == (2 or 3 or 4):
                self.dealdmg = True
            else:
                self.dealdmg = False
        else:
            self.h += 1
    
    # Reproduz animação de ataque pesado
    def ani_hatk(self):
        if self.j > constants.FPS/len(self.heavyatk_frames_r):
            self.j = 0
            if self.direction == "R":
                self.image = self.heavyatk_frames_r[self.k]
            else:
                self.image = self.heavyatk_frames_l[self.k]
            if self.k >= len(self.heavyatk_frames_r) - 1:
                self.k = 0
                self.hatk = False
            else:
                self.k += 1
            if self.k == (3 or 4 or 5):
                self.dealdmg = True
            else:
                self.dealdmg = False
        else:
            self.j += 1
            
    # Reproduz animação de tomar dano
    def ani_damage(self):
        if self.direction == "R":
            self.image = self.takedmg_frames_r[0]
        else:
            self.image = self.takedmg_frames_l[0]
    
    # Reproduz a animação de morte
    def ani_death(self):
        self.change_y = 9
        if self.direction == "R":
            self.image = self.dead_frames_r[0]
        else:
            self.image = self.dead_frames_l[0]

    # Reproduz animação de uso de estus
    def ani_estus(self):
        if self.l > constants.FPS/len(self.estus_frames_r):
            self.l = 0
            if self.direction == "R":
                self.image = self.estus_frames_r[self.m]
            else:
                self.image = self.estus_frames_l[self.m]
            if self.m >= len(self.estus_frames_l) - 1:
                self.m = 0
                self.recovering = False
            else:
                self.m += 1
        else:
            self.l += 1
#==============================================================================
#  
#==============================================================================
    def update(self):
        # Move o player
        # Gravidade
        self.calc_grav()
        if self.health <= 0:
            self.live = False
        if self.possible("wait"):
            self.ani_wait()
        if self.possible("move"):
            if self.change_x != 0 and self.change_y == 0:
                self.rect.x += self.change_x
                self.ani_walk()
        if not self.live:
            self.ani_death()
                
        # Verifica se existe colisão ao andar
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

        # Move para cima/baixo
        if self.change_y != 0:
            self.rect.y += self.change_y
            self.rect.x += self.change_x
            self.ani_jump()

        # Verifica se existe colisão ao pular
        self.on_ground = False
        block_hit_list = self.level.platform_list
        pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if pygame.sprite.collide_rect(self,block):
            # Redefine a posição do player baseada no topo/fundo do objeto
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
        
        # Habilita os movimentos do player
        self.clocker()
        if self.live:
            self.defend()
            self.detect_atk()
            if not self.jumping:
                if self.guard:
                    self.estus()
                    if self.stamina > 0:
                        self.parry()
                        self.riposte()
                        self.roll()
                        self.light_atk()
                        self.heavy_atk()
                else:
                    self.guard_break()
                
    # Calcula o efeito da gravidade
    def calc_grav(self):
        if self.change_y == 0:
            if self.on_ground:
                self.change_y = 0
            else:
                self.change_y = 1
        else:
            self.jumping = True
            self.change_y += .35
 
        # Verifica se o player está no chão
        if self.rect.y >= constants.LEVEL_BOTTOM - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.live = False
            self.health = 0
            self.jumping = False

#==============================================================================
#   Movimentos do player:
#==============================================================================
    def jump(self):
        # Move o player 2 pixels para baixo para verificar se existe uma plataforma
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # Se for possível pular, define a velocidade da subida
        if len(platform_hit_list) > 0:
            self.change_y = - 10
            self.jumping = True
            self.on_ground = False
    
    # Move o player para a esquerda
    def go_left(self):
            self.change_x = - 6
            self.direction = "L"
    
    # Move o player para a direita
    def go_right(self):
            self.change_x = 6
            self.direction = "R"
            
    # Impede o movimento do player
    def stop(self):
        self.change_x = 0
    
#==============================================================================
#  Mecânicas do player
#==============================================================================

    # Coloca o player em posição de defesa
    def defend(self):
        if self.defending:
            self.ani_defend()
    
    # Quebra a guarda do player
    def guard_break(self):
        if not self.guard:
            self.ani_guardbreak()

    # Desvia um ataque e quebra guarda do enemy
    def parry(self):
        if self.parrying:
            self.start_clocker = True
            self.change_x = 0
            self.ani_parry()
    
    # Ataque crítico
    def riposte(self):
        if self.riposting:
            self.change_x = 0
            self.start_clocker = True
            self.ani_riposte()
            
    # Faz o player desviar
    def roll(self):
        if self.rolling and constants.player_roll_frames > 0:
            self.start_clocker = True
            self.ani_roll()
        self.rolling = False
        
    # Calcula quantos frames serão usados para rolar
    def active_roll(self):
        constants.player_roll_frames += 85
        self.calc_stamina(15)#10
    
    # Ataque leve
    def light_atk(self):
        if self.latk:
            self.dmg_d = 1 # Dano real = dmg_d * 17
            self.start_clocker = True
            self.change_x = 0
            self.ani_latk()
    
    # Ataque forte
    def heavy_atk(self):
        if self.hatk:
            self.dmg_d = 4 # Dano real = dmg_d * 10
            self.start_clocker = True
            self.change_x = 0
            self.ani_hatk()
            
    # Animação para recuperar a vida do player
    def estus(self):
        if self.recovering:
            self.change_x = 0
            self.ani_estus()

    # Usa item para recuperar a vida do player
    def use_estus(self):
        if self.estus_rn > 0:
            self.estus_rn -= 1
            self.estus_used += 1
            self.estus_regen += constants.estus_maxregen
            
    # Regenera a vida do player
    def life_regen(self, estus_regen):
        if self.health < self.maxhealth:
            if self.estus_used == 1:
                self.health += 1
                self.estus_regen -= 1
            elif self.estus_used > 1:
                self.health += 3
                self.estus_regen -= 3  
        if self.estus_used == 0 or self.estus_regen < 0:
            self.estus_used = 0
            self.estus_regen = 0
            pygame.time.set_timer(estus_regen, 0)
            self.recovering = False
        elif self.health >= self.maxhealth:
            self.health = self.maxhealth
            self.estus_used = 0
            self.estus_regen = 0
            pygame.time.set_timer(estus_regen, 0)
            
    # Percebe se o player está tomando um ataque
    def detect_atk(self):
        self.clocker_rt = 1
        for enemy in self.enemies:
            if (self.rect.centerx > enemy.rect.centerx -80 and self.rect.centerx < enemy.rect.centerx and enemy.direction == 'L') \
            or (self.rect.centerx < enemy.rect.centerx +80 and self.rect.centerx > enemy.rect.centerx and enemy.direction == 'R'):
                if enemy.dealdmg and pygame.sprite.collide_rect(self, enemy):
                    self.dmg_r = enemy.dmg_d
                    self.takedmg = True
                    self.calc_damage()
                    if enemy.direction == 'R':
                        self.rect.x += 10
                    else:
                        self.rect.x -= 10
                    self.dmg_r = 0
#                    self.takedmg = False

    # Calcula o dano recebido pelo player
    def calc_damage(self):
        # Verifica se o player está defendendo
        if self.guard and self.takedmg:
            if self.defending:
                self.calc_stamina(self.dmg_r) # Reduz stamina
                if self.stamina <= 0:
                    self.stamina = 0
                    self.guard = False # Quebra guarda
                                        
            else:
                self.ani_damage()
                if self.health - self.dmg_r > 0:
                    pass
#                    self.health -= self.dmg_r # Reduz vida
                else:
                    self.health = 0
        else:
            self.health -= self.dmg_r*2
                
    # Calcula a stamina gasta pelo player
    def calc_stamina(self, stm_cost):
        if self.stamina > 0:
            self.stamina -= stm_cost
        else:
            self.stamina = 0
            
    # Regenera stamina usada
    def stamina_regen(self):
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
                
    # Faz o player voltar a vida
    def reborn(self):
        self.live = True
        self.guard = True
        self.defending = False
        self.health = self.maxhealth
        self.estus_rn = 5
        self.rect.y = -150
        os.system('cls') # Limpa o console
        
    # Estabelece um delay
    def clocker(self):
        if self.start_clocker:
            if constants.c > constants.FPS:
                constants.c = 0
                self.start_clocker = False
            else:
                constants.c += self.clocker_rt
        
    # Verifica a possibilidade de um evento acontecer
    def possible(self, event):
        if event == "wait":
            if self.live and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "move":
            if self.live and self.guard and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "jump":
            if self.live and self.guard and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting and self.stamina > 0.6*self.maxstamina:
                return True
        elif event == "defend":
            if self.live and self.guard and not self.jumping and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "latk":
            if self.live and self.guard and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "hatk":
            if self.live and self.guard and not self.jumping and not self.defending and not self.latk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "parry":
            if self.live and self.guard and not self.jumping and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.riposting:
                return True
        elif event == "riposte":
            if self.live and self.guard and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.recovering and not self.takedmg and not self.parrying:
                return True
        elif event == "roll":
            if self.live and self.guard and not self.jumping and not self.latk and not self.hatk and not self.recovering and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "estus":
            if self.live and self.guard and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting and self.estus_rn > 0:
                return True
        else:
            return False

    # Mostra na tela as informações do player
    def player_hud(self, screen):
        estus_n = constants.bitsFont_P.render(str(self.estus_rn), True, constants.WHITE, None)
        estus_n_rect = estus_n.get_rect()
        estus_n_rect.x = 37
        estus_n_rect.y = 30
        image = spritesheet_functions.SpriteSheet("images/link_2.png")
        
        if self.estus_rn > 0:
            image = image.get_image(219, 1074, 12, 15, constants.BLACK)
        else:
            image = image.get_image(169, 1074, 12, 15, constants.BLACK)
                
        image = pygame.transform.scale(image, (25, 31))
        screen.blit(image,[10, 10])
        screen.blit(estus_n, estus_n_rect)

        pygame.draw.rect(screen, constants.WHITE, (49, 14, (3*self.maxhealth)+2, 12))
        pygame.draw.rect(screen, constants.GRAY, (50, 15, 3*self.maxhealth, 10))
        pygame.draw.rect(screen, constants.WHITE, (49, 29, (3*self.maxstamina)+2, 12))
        pygame.draw.rect(screen, constants.GRAY, (50, 30, 3*self.maxstamina, 10))
        pygame.draw.rect(screen, constants.WHITE, (50 + 1.8*self.maxstamina, 30, 1, 10))
        if self.health > 0:
            pygame.draw.rect(screen, constants.RED, (50, 15, 3*self.health, 10))
        if self.stamina > 0:
            pygame.draw.rect(screen, constants.GREEN, (50, 30, 3*self.stamina, 10))

# Mostra tela de morte
def dead_screen(screen, player):
    sounds.dead.play()
    black_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
    black_surf.fill((0, 0, 0, 180))
    screen.blit(black_surf, (0, 0))
    you_died_txt = constants.soulsFont_G.render("YOU   DIED", True, constants.RED, None)
    you_died_rect = you_died_txt.get_rect()
    you_died_rect.centerx = constants.SCREEN_WIDTH/2
    you_died_rect.centery = constants.SCREEN_HEIGHT/2
    screen.blit(you_died_txt, you_died_rect)
    player.change_x, player.change_y = 0, 0
    player.health, player.stamina = 0, 0
    
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
                    player.reborn()
                if event.key == pygame.K_e:
                    pass
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_q:
                    pass