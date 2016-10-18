# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:11:21 2016

@author: vini_
"""

import pygame, random, constants, sounds, spritesheet_functions

class Enemy2(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
        
        # Define variáveis de características do enemy
        self.maxhealth = 110
        self.health = 110
        self.maxstamina = 50
        self.stamina = 50
        self.dmg_r = 0
        self.dmg_d = 0
        self.rolling_speed = 8
        self.roll_dt = 4
        
        # Define variáveis de estado do enemy
        self.live = True
        self.on_ground = True
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
        self.players = []
        self.current_position = 0
        self.world_shift = 0
        self.clocker_rt = 0
        self.DEATH = 1
        self.DMG_TAKEN = 0
        self.a = self.b = self.c = self.d = self.e = self.f = self.g = self.h = self.i = \
        self.j = self.k = self.l = self.m = self.n = self.o = self.p = self.q = 0
        
        # Define o vetor velocidade do enemy
        self.change_x = 0
        self.change_y = 0
        
        # Armazena todas as imagens da animação de descanço esquerda/direita do enemy
        self.waiting_frames_l = []
        self.waiting_frames_r = []
        
        # Armazena todas as imagens da animação de andar para esquerda/direita do enemy
        self.walking_frames_l = []
        self.walking_frames_r = []
        
        # Armazena todas as imagens da animação de pular para a esquerda/direita do enemy
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
 
        # Direção que o enemy está virado
        self.direction = "L"
 
        # Lista de sprites que o enemy pode esbarrar
        self.level = None

        sprite_sheet = spritesheet_functions.SpriteSheet("images/enemy_1.png")
        
        
        # Carrega todas as sprites paradas viradas para a direita/esquerda
        "Esperar"
        list1 = [[0, 180, 100, 84]]
                 
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)               
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        "Correr"
        list1 = [[100, 180, 100, 84],
                 [700, 270, 100, 84],
                 [200, 180, 100, 84],
                 [700, 270, 100, 84]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens pulando viradas para a direita numa lista
        "Pular"
        list1 = [[400, 180, 100, 84]]
                 
        self.jumping_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.jumping_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
 
        # Carrega todas as imagens de defesa viradas para a direita numa lista
        "Defender"
        list1 = [[300, 180, 100, 84]]
        
        self.defense_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.defense_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)         
        
        # Carrega todas as imagens de quebra de guarda viradas para a direita numa lista
        "Quebra de guarda"
        list1 = [[400, 180, 100, 84]]
        
        self.guardbreak_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # vira as imagens para a esquerda
        self.guardbreak_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de parry viradas para a direita numa lista
        "Parry"
        list1 = [[500, 180, 100, 84],
                 [400, 180, 100, 84]]
                 
        self.parry_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.parry_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de riposte viradas para a direita numa lista
        "Riposte"
        list1 = [[0, 270, 100, 84],
                 [100, 270, 100, 84],
                 [200, 270, 100, 84],
                 [300, 270, 100, 84],
                 [400, 270, 100, 84]]
        
        self.riposte_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.riposte_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de rolar viradas para a direita numa lista
        "Rolar"
        list1 = [[500, 270, 100, 84]]
        
        self.roll_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.roll_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de ataque leve viradas para a direita numa lista
        "Ataque leve"
        list1 = [[400, 180, 100, 84],
                 [400, 180, 100, 84],
                 [600, 180, 100, 84],
                 [600, 180, 100, 84],
                 [700, 180, 100, 84],
                 [700, 180, 100, 84]]
                 
        self.lightatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.lightatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens de ataque pesado viradas para a direita numa lista
        "Ataque pesado"
        list1 = [[0, 270, 100, 84],
                 [100, 270, 100, 84],
                 [100, 270, 100, 84],
                 [200, 270, 100, 84],
                 [200, 270, 100, 84],
                 [300, 270, 100, 84],
                 [400, 270, 100, 84]]
                 
        self.heavyatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira as imagens para a esquerda
        self.heavyatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens tomando dano viradas para a direita numa lista
        "Tomar dano"
        list1 = [[500, 270, 100, 84]]
        
        self.takedmg_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.takedmg_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)
        
        # Carrega todas as imagens morrendo viradas para a direita numa lista
        "Morrer"
        list1 = [[600, 270, 100, 84]]
                 
        self.dead_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.DARKBLUE)
        # Vira todas as imagens para a esquerda
        self.dead_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.DARKBLUE)

        # Define a sprite que o inimigo começa
        self.image = self.waiting_frames_l[0]
 
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
  
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
            self.image = self.jumping_frames_r[0]
        elif self.direction == "L" and self.jumping == True :
            self.image = self.jumping_frames_l[0]
    
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
            if self.i == 4:
                if self.q == 0:
                    sounds.enemy_latk.play()
                    self.q = 1
            else:
                self.q = 0
            if self.i == 5:
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
            if self.k == 4:
                if self.q == 0:
                    sounds.enemy_hatk.play()
                    self.q = 1
            else:
                self.q = 0
            if self.k == 4:
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
        self.dealdmg = False
        self.latk = False
        self.hatk = False
        if self.direction == "R":
            self.image = self.dead_frames_r[0]
        else:
            self.image = self.dead_frames_l[0]

#==============================================================================
#   
#==============================================================================
    def update(self):
        # Move o enemy
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
        self.right = self.rect.right - 15
        self.left = self.rect.left + 15
        for block in block_hit_list:
            if pygame.sprite.collide_rect(self, block):
                if not self.jumping:
                    if self.rect.bottom < block.rect.bottom and self.rect.bottom > block.rect.top:
                        if self.left < block.rect.left and self.right > block.rect.left:
                            self.rect.right = block.rect.left + 55
                        if self.right > block.rect.right and self.left < block.rect.right:
                            self.rect.left = block.rect.right - 55
                    if self.rect.top > block.rect.top and self.rect.top < block.rect.bottom:
                        if self.left < block.rect.left and self.right > block.rect.left:
                            self.rect.right = block.rect.left + 55
                        if self.right > block.rect.right and self.left < block.rect.right:
                            self.rect.left = block.rect.right - 55
                    if self.rect.top <= block.rect.top and self.rect.bottom >= block.rect.bottom:
                        if self.left < block.rect.left and self.right > block.rect.left:
                            self.rect.right = block.rect.left + 55
                        if self.right > block.rect.right and self.left < block.rect.right:
                            self.rect.left = block.rect.right - 55
                if self.rect.top >= block.rect.top and self.rect.bottom <= block.rect.bottom:
                    if self.left < block.rect.left and self.right > block.rect.left:
                        self.rect.right = block.rect.left + 55
                    if self.right > block.rect.right and self.left < block.rect.right:
                        self.rect.left = block.rect.right - 55
 
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
                if self.right > block.rect.left and self.left < block.rect.right:
                    if self.rect.bottom > block.rect.top and (self.rect.bottom - 20) < block.rect.top:
                        if self.change_y > 0 and not self.on_ground:
                            self.rect.bottom = block.rect.top
                            self.on_ground = True
                            self.jumping = False
                            self.change_y = 0
                    if self.rect.top < block.rect.bottom and (self.rect.top + 10) > block.rect.bottom:
                        if self.change_y < 0 and not self.on_ground:
                            self.rect.top = block.rect.bottom
                
        # Habilita os movimentos do enemy
        self.clocker()
        if self.live:
            self.defend()
            self.detect_atk()
            if self.guard:
                self.parry()
                self.riposte()
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
 
        # Verifica se o enemy está no chão
        if self.rect.y >= constants.LEVEL_BOTTOM - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.live = False
            self.health = 0
            self.jumping = False
 
#==============================================================================
#     Movimentos do inimigo:
#==============================================================================
    def jump(self):
        # Move o enemy 2 pixels para baixo para verificar se existe uma plataforma
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # Se for possível pular, define a velocidade da subida
        if len(platform_hit_list) > 0:
            self.change_y = - 10
            self.jumping = True
            self.on_ground = False
            
    # Move o enemy para a esquerda
    def go_left(self):
        self.change_x = -8
        self.direction = "L"
 
    # Move o enemy para a direita
    def go_right(self):
        self.change_x = 8
        self.direction = "R"
        
    # Impede o movimento do enemy
    def stop(self):
        self.change_x = 0
        
    
#==============================================================================
#  Mecânicas do inimigo
#==============================================================================

    # Coloca o inimigo em posição de defesa
    def defend(self):
        if self.defending:
            self.ani_defend()
    
    # Quebra a guarda do inimigo
    def guard_break(self):
        if not self.guard:
            self.ani_guardbreak()

    # Desvia um ataque e quebra guarda do player
    def parry(self):
        if self.parrying:
            self.start_clocker = True
            self.change_x = 0
            self.ani_parry()
    
    # Ataque crítico
    def riposte(self):
        if self.riposting:
            self.start_clocker = True
            self.change_x = 0
            self.ani_riposte()
            
    # Faz o enemy desviar
    def roll(self):
        if self.rolling and constants.boss_roll_frames > 0:
            self.start_clocker = True
            self.ani_roll()
        self.rolling = False
        
    # Calcula quantos frames serão usados para rolar
    def active_roll(self):
        constants.boss_roll_frames += 85

    # Ataque leve
    def light_atk(self):
        if self.latk:
            self.change_x = 0
            self.dmg_d = 0.5 # Dano real = dmg_d * 12
            self.start_clocker = True
            self.ani_latk()
    
    # Ataque forte
    def heavy_atk(self):
        if self.hatk:
            self.change_x = 0
            self.dmg_d = 1 # Dano real = dmg_d * 10
            self.start_clocker = True
            self.ani_hatk()
                
    # Percebe se o enemy está tomando um ataque
    def detect_atk(self):
        self.clocker_rt = 1
        for player in self.players:
            if (self.rect.centerx > player.rect.centerx -80 and self.rect.centerx < player.rect.centerx and player.direction == 'L') \
            or (self.rect.centerx < player.rect.centerx +80 and self.rect.centerx > player.rect.centerx and player.direction == 'R'):
                if player.dealdmg and pygame.sprite.collide_rect(self, player):
                    self.dmg_r = player.dmg_d
                    self.takedmg = True
                    self.calc_damage()
                else:
                    self.dmg_r = 0
                    self.takedmg = False
                if not player.dealdmg:
                    self.q = 0
            
    # Calcula o dano recebido pelo inimigo
    def calc_damage(self):
        # Verifica se o boss está defendendo
        if self.guard and self.takedmg:
            if self.defending:
                self.calc_stamina(self.dmg_r/2) # Reduz stamina
            else:
                self.ani_damage()
                if self.q == 0:
                    sounds.enemy_dmg.play()
                    self.q = 1
                if self.health - self.dmg_r > 0:
                    self.health -= self.dmg_r # Reduz vida
                    self.DMG_TAKEN += self.dmg_r
                else:
                    self.health = 0
                
    # Calcula a stamina gasta pelo inimigo
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
            
    # Faz o inimigo voltar a vida
    def reborn(self):
        self.rect.y = constants.eb1_y - 250
        if self.p == 1:
            self.rect.x -= self.current_position - constants.eb1_x
        elif self.p == 2:
            self.rect.x -= self.current_position - constants.eb2_x
        elif self.p == 3:
            self.rect.x -= self.current_position - constants.eb3_x
        self.live = True
        self.guard = True
        self.jumping = True
        self.defending = False
        self.health = self.maxhealth
        self.stamina = self.maxstamina
        self.DEATH = 1
        self.image = self.waiting_frames_l[0]
        self.direction = "L"
        
    # Estabelece um delay
    def clocker(self):
        if self.start_clocker:
            if constants.k > constants.FPS:
                constants.k = 0
                self.start_clocker = False
            else:
                constants.k += self.clocker_rt
                
    def randomize(self):
        self.l = random.choice(["latk", "hatk", "roll", "wait"])
        self.m = random.choice(["def", "wait"])
        self.n = random.uniform(0, 1)
        self.o = random.uniform(0, 1)
                                
    # Verifica a possibilidade de um evento acontecer
    def possible(self, event):
        if event == "wait":
            if self.live and not self.jumping and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "move":
            if self.live and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting:
                return True
        elif event == "jump":
            if self.live and not self.defending and not self.latk and not self.hatk and not self.rolling and not self.takedmg and not self.parrying and not self.riposting and not self.jumping:
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
        
    def enemy_hud(self, screen):
        if self.health >= self.maxhealth:
            self.health = self.maxhealth
        if 0 < self.health < self.maxhealth:
            if self.direction == "L":
                pygame.draw.rect(screen, constants.WHITE, (self.rect.left+74, self.rect.top+9, (self.maxhealth)+2, 9))
                pygame.draw.rect(screen, constants.GRAY, (self.rect.left+75, self.rect.top+10, self.maxhealth, 7))
                pygame.draw.rect(screen, constants.ORANGE, (self.rect.left+75, self.rect.top+10, self.health, 7))
            else:
                pygame.draw.rect(screen, constants.WHITE, (self.rect.left+14, self.rect.top+9, (self.maxhealth)+2, 9))
                pygame.draw.rect(screen, constants.GRAY, (self.rect.left+15, self.rect.top+10, self.maxhealth, 7))
                pygame.draw.rect(screen, constants.ORANGE, (self.rect.left+15, self.rect.top+10, self.health, 7))
            
    # Inteligência artificial do enemy
    def AI(self, player, clock):
        if self.direction == "R":
            self.right = self.rect.centerx
            self.left = self.rect.centerx - 30
            self.center = self.rect.centerx - 15
        else:
            self.right = self.rect.centerx + 30
            self.left = self.rect.centerx
            self.center = self.rect.centerx + 15
        # Vira o boss na direção do player
        if self.possible("wait"):
            if player.rect.centerx > self.center:
                self.direction = "R"
            else:
                self.direction = "L"
#            block_hit_list =  self.level.platform_list
#            for block in block_hit_list:
#                if player.rect.bottom == self.rect.bottom:
#                    if block.rect.left <= self.rect.left and block.rect.right >= self.rect.right:
                        # Persegue o player
            if player.rect.centerx + 15 < self.left:
                self.go_left()
            elif player.rect.centerx - 15 > self.right:
                self.go_right()
            if player.rect.left > self.right +400 or player.rect.right < self.left -400:
                  self.stop()
            elif (player.rect.centerx > self.center -55 and player.rect.centerx < self.center) \
              or (player.rect.centerx < self.center +55 and player.rect.centerx > self.center):
                self.stop()
#                                self.l = random.choice(["latk", "hatk", "roll", "wait"])
                if self.l == "latk" and self.possible("latk"):
                    self.latk = True
                elif self.l == "hatk" and self.possible("hatk"):
                    self.hatk = True
                elif self.l == "roll" and self.possible("roll"):
                    self.rolling = True
                    self.active_roll()
                elif self.l == "wait":
                    pass
#                                    self.m = random.choice(["def", "wait"])
#                                    self.n = random.uniform(0, 1)
#                                    self.o = random.uniform(0, 1)
                if player.dealdmg:
                    if self.direction != player.direction:
                        if self.m == "def":
                            if self.n > 0.4:
                                if self.possible("defend"):
                                    self.defending = True
                        if not self.defending:
                            self.dmg_r = player.dmg_d
                            self.takedmg = True
                        else:
                            if self.o > 0.1:
                                if self.possible("parry"):
                                    self.parrying = True
                                    if self.possible("latk"):
                                        self.latk = True
                else:
                    self.defending = False
                    self.parrying = False
                    self.dmg_r = 0
                self.rolling = False
        else:
            self.stop()