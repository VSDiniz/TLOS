# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:55:17 2016

@author: vini_
"""

import pygame, constants, spritesheet_functions

class Enemy1(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
        
        # Define variáveis de características do inimigo
        self.maxhealth = 250
        self.health = 250
        self.stamina = 50
        self.dmg_r = 0
        self.dmg_d = 0
        
        # Define variáveis de estado do inimigo
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
        self.world_shift = 0
        self.start_clocker = False
        
        # Define o vetor velocidade do inimigo
        self.change_x = 0
        self.change_y = 0
        
        # Armazena todas as imagens da animação de descanço esquerda/direita do inimigo
        self.waiting_frames_l = []
        self.waiting_frames_r = []
        
        # Armazena todas as imagens da animação de andar para esquerda/direita do inimigo
        self.walking_frames_l = []
        self.walking_frames_r = []
        
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
 
        # Direção que o inimigo está virado
        self.direction = "L"
 
        # Lista de sprites que o inimigo pode esbarrar
        self.level = None
 
        self.delay = self.i = self.c = self.s = 0
        self.a = self.b = self.d = self.e = 0
        sprite_sheet = spritesheet_functions.SpriteSheet("images/enemy1.png")
        
        
        # Carrega todas as sprites paradas viradas para a direita/esquerda
        "Esperar"
        list1 = [[0, 0, 100, 84]]
                 
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)               
        
        # Carrega todas as sprites correndo viradas para a direita numa lista
        "Correr"
        list1 = [[100, 0, 100, 84],
                 [200, 0, 100, 84]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
 
#==============================================================================
#         
#==============================================================================
        # Carrega todas as imagens de defesa viradas para a direita numa lista
        "Defender"
        list1 = [[300, 0, 100, 84]]
        
        self.defense_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.defense_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)         
        
        # Carrega todas as imagens de quebra de guarda viradas para a direita numa lista
        "Quebra de guarda"
        list1 = [[400, 0, 100, 84]]
        
        self.guardbreak_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # vira as imagens para a esquerda
        self.guardbreak_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de parry viradas para a direita numa lista
        "Parry"
        list1 = [[500, 0, 100, 84],
                 [400, 0, 100, 84]]
                 
        self.parry_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.parry_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de riposte viradas para a direita numa lista
        "Riposte"
        list1 = [[0, 90, 100, 84],
                 [100, 90, 100, 84],
                 [200, 90, 100, 84],
                 [300, 90, 100, 84],
                 [400, 90, 100, 84]]
        
        self.riposte_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.riposte_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de ataque leve viradas para a direita numa lista
        "Ataque leve"
        list1 = [[400, 0, 100, 84],
                 [600, 0, 100, 84],
                 [700, 0, 100, 84]]
                 
        self.lightatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.lightatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens de ataque pesado viradas para a direita numa lista
        "Ataque pesado"
        list1 = [[0, 90, 100, 84],
                 [100, 90, 100, 84],
                 [200, 90, 100, 84],
                 [300, 90, 100, 84],
                 [400, 90, 100, 84]]
                 
        self.heavyatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.heavyatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens tomando dano viradas para a direita numa lista
        "Tomar dano"
        list1 = [[500, 90, 100, 84]]
        
        self.takedmg_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.takedmg_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
        # Carrega todas as imagens morrendo viradas para a direita numa lista
        "Morrer"
        list1 = [[600, 90, 100, 84]]
                 
        self.dead_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira todas as imagens para a esquerda
        self.dead_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)

        # Define a sprite que o inimigo começa
        self.image = self.waiting_frames_l[0]
 
        # Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
  
    def update(self):
        # Move o inimigo
        # Gravidade
        self.calc_grav()
        
        # Reproduz a animação de espera           
        if self.possible("wait"):
            if self.c > 120:
                self.c = 0
                self.guard = True
            else:
                self.c += 1
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

        # Morte do inimigo        
        if not self.live:
            self.change_y = 10
            if self.direction == "R":
                self.image = self.dead_frames_r[0]
            else:
                self.image = self.dead_frames_l[0]
 
        # Verifica se existe colisão                
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
 
        # Verifica se existe colisão
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
                
        if self.live:
            self.take_dmg()
            self.calc_damage()
            if not self.jumping:
                if self.guard:
                    if self.stamina > 0:
                        self.parry()
                        self.riposte()
                        self.roll()
                        self.light_atk()
                        self.heavy_atk()
                else:
                    self.guard_break()
            
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
 
        # Verifica se o inimigo está no chão
        if self.rect.y >= constants.LEVEL_BOTTOM - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.live = False
            self.health = 0
            self.jumping = False
 
    # Movimentos do inimigo:
    def go_left(self):
        # Quando o inimigo vai para a esquerda
        self.change_x = -4
        self.direction = "L"
 
    def go_right(self):
        # Quando o inimigo vai para a direita
        self.change_x = 4
        self.direction = "R"
 
    def stop(self):
        # Quando o inimigo não se move
        self.change_x = 0
        
    
#==============================================================================
#  Mecânicas do inimigo
#==============================================================================

    # Coloca o inimigo em posição de defesa
    def defend(self):
        self.defending = True
        self.jumping = False
        if self.direction == "R":
            self.image = self.defense_frames_r[0]
        else:
            self.image = self.defense_frames_l[0]
    
    # Quebra a guarda do inimigo
    def guard_break(self):
        if not self.guard:
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
                if constants.i == (7 or 8):
                    self.dealdmg = True
                else:
                    self.dealdmg = False
            else: 
                constants.d1 += 1
    
    # Ataque forte
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
                if constants.i == (8 or 9 or 10):
                    self.dealdmg = True
                else:
                    self.dealdmg = False
            else: 
                constants.d1 += 1
            
    # Calcula o dano recebido pelo inimigo
    def calc_damage(self):
        # Verifica se o inimigo está defendendo
        if self.guard and self.takedmg:
            if self.defending:
                pass
                                        
            else:
                if self.direction == "R":
                    self.image = self.takedmg_frames_r[0]
                else:
                    self.image = self.takedmg_frames_l[0]
                if self.health - self.dmg_r > 0:
                    self.health -= self.dmg_r # Reduz vida
                else:
                    self.health = 0                    
        if self.health <= 0:
            self.live = False
                
    def take_dmg(self):
        self.clocker_rt = 1
        if not self.defending and self.takedmg:
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
                
    # Calcula a stamina gasta pelo inimigo
    def calc_stamina(self, stm_cost):
        if self.stamina > 0:        
            self.stamina -= stm_cost
        else:
            self.stamina = 0
            
    # Regenera stamina usada
    def stamina_regen(self):
        # Calcula a regeneração de stamina do inimigo
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
        self.live = True
        self.guard = True
        self.defending = False
        self.health = self.maxhealth
        self.rect.y = 50
        
    def clocker(self):
        if self.start_clocker:
            if constants.k > constants.FPS:
                constants.k = 0
                self.start_clocker = False
            else:
                constants.k += self.clocker_rt
                                
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
        pygame.draw.rect(screen, constants.WHITE, (self.rect.top-11, self.rect.left-1, (self.maxhealth)+2, 7))
        pygame.draw.rect(screen, constants.GRAY, (self.rect.top-10, self.rect.left, self.maxhealth, 5))
        if self.health >= self.maxhealth:
            self.health = self.maxhealth
        if self.health > 0:
            pygame.draw.rect(screen, constants.ORANGE, self.rect.top-10, self.rect.left, self.health, 5)
            
    # Inteligência artificial do inimigo
    def AI(self, player, clock):
        # Vira o inimigo na direção do player
        if self.possible("wait"):
            if player.rect.centerx > self.rect.centerx:
                self.direction = "R"
            else:
                self.direction = "L"
            # Persegue o player
            if player.rect.centerx + 50 < self.rect.left:
                self.go_left()
            elif player.rect.centerx - 50 > self.rect.right:
                self.go_right()
        if player.rect.left > self.rect.right +200 or player.rect.right < self.rect.left -200:
              self.stop()
        elif (player.rect.centerx > self.rect.centerx -80 and player.rect.centerx < self.rect.centerx +80) \
          or (player.rect.centerx < self.rect.centerx +80 and player.rect.centerx > self.rect.centerx -80):
            self.stop()
#            self.a = random.choice([0, 1, 2, 3, 4, 5])
            if clock.get_fps() >= 60:
                if self.a == 0 and self.possible("latk"):
                    self.latk = True
                elif self.a == 1 and self.possible("hatk"):
                    self.hatk = True
                elif self.a == 2 and self.possible("roll"):
                    self.rolling = True
                    self.active_roll()
            elif self.a == 3 or 4 or 5:
                pass
#                self.b = random.choice([0, 1])
#                self.d = random.uniform(0, 1)
#                self.e = random.uniform(0, 1)
                if player.dealdmg:
                    if self.direction != player.direction:
                        if self.b == 0:
                            if self.d > 0.4:
                                 if self.possible("defend"):
                                   self.defend()
                            if not self.defending:
                                self.dmg_r = player.dmg_d
                                self.takedmg = True
                        else:
                            if self.e > 0.1:
                                 if self.possible("parry"):
                                     self.parrying = True
                    else:
                        if self.possible("latk"):
                            self.latk = True
                else:
                    self.defending = False
                    self.parrying = False
                    self.dmg_r = 0