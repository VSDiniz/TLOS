# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:03:06 2016

@author: vini_
"""

import pygame, constants, spritesheet_functions
from platforms import MovingPlatform
 
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
 
        super().__init__()
        
        self.maxhealth = 100
        self.health = 100
        self.maxstamina = 50
        self.stamina = 50
        self.estus_rn = 5
        self.defending= False
 
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
        
        # Armazena todas as imagens da animação de ataque leve para a esquerda/direita
        self.lightatk_frames_l = []
        self.lightatk_frames_r = []
        

 
        # Direção que o player está virado
        self.direction = "R"
 
        # Lista de sprites que o player pode esbarrar
        self.level = None        
        
        self.delay = self.i = self.s = 0 
        sprite_sheet = spritesheet_functions.SpriteSheet("images/link.png")
        
# Carrega todas as sprites paradas viradas para a direita numa lista
        list1 = [[54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [54, 61, 42, 42],
                 [104, 61, 42, 42],
                 [154, 61, 42, 42],
                 [104, 61, 42, 42]]        
        
        self.waiting_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.waiting_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
# Carrega todas as sprites correndo viradas para a direita numa lista
        list1 = [[204, 411, 42, 41],
                 [154, 411, 42, 41],
                 [104, 411, 42, 41],
                 [54, 411, 42, 41],
                 [4, 411, 42, 41],
                 [204, 461, 42, 41],
                 [154, 461, 42, 41],
                 [104, 461, 42, 41],
                 [54, 461, 42, 41],
                 [4, 461, 42, 41]]
                 
        self.walking_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
 
        # Carrega todas as imagens correndo viradas para a direita e as vira para a esquerda
        list1 = [[4, 411, 42, 41],
                 [54, 411, 42, 41],
                 [104, 411, 42, 41],
                 [154, 411, 42, 41],
                 [204, 411, 42, 41],
                 [4, 461, 42, 41],
                 [54, 461, 42, 41],
                 [104, 461, 42, 41],
                 [154, 461, 42, 41],
                 [204, 461, 42, 41]]
                 
        self.walking_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)        
        
# Carrega todas as imagens pulando viradas para a direita numa lista
        list1 = [[304, 0, 42, 54],
                 [354, 0, 42, 54],
                 [404, 0, 42, 54]]
                 
        self.jumping_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.jumping_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)

# Carrega todas as imagens de defesa viradas para a direita numa lista
        list1 = [[259, 311, 32, 42]]
        
        self.defense_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.defense_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)         
        
# Carrega todas as imagens de quebra de guarda viradas para a direita numa lista
        list1 = [[255, 562, 39, 44]]
        
        self.guardbreak_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # vira as imagens para a esquerda
        self.guardbreak_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
# Carrega todas as imagens de parry viradas para a direita numa lista
        list1 = [[258, 363, 63, 38],
                 [106, 757, 37, 49]]
                 
        self.parry_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.parry_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)
        
# Carrega todas as imagens de ataque leve viradas para a direita numa lista
        list1 = [[204, 59, 41, 45],
                 [328, 313, 63, 38]]
                 
        self.lightatk_frames_r = spritesheet_functions.createSprite(sprite_sheet,list1, 0, 1, constants.BLACK)
        # Vira as imagens para a esquerda
        self.lightatk_frames_l = spritesheet_functions.createSprite(sprite_sheet,list1, 1, 1, constants.BLACK)    



# Define a sprite que o player começa
        self.image = self.waiting_frames_r[0]
 
# Define uma referência para o retângulo da sprite
        self.rect = self.image.get_rect()
 
    def update(self):
        # Move o player
        # Gravidade
        self.calc_grav()
        
        # Reproduz a animação de espera           
        if self.defending == False:
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
                if (-10 <= self.change_y <= 0):
                    self.image = self.jumping_frames_r[0]
                elif (0 < self.change_y <= 2):
                    self.image = self.jumping_frames_r[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_r[2]
                
            else:
                if (-10 <= self.change_y <= 0):
                    self.image = self.jumping_frames_l[0]
                elif (0 < self.change_y <= 2):
                    self.image = self.jumping_frames_l[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_l[2]
                
                
        elif self.change_x != 0 and self.change_y != 0:
             self.rect.y += self.change_y
             self.rect.x += self.change_x
             pos = self.rect.x + self.level.world_shift
             
             if self.direction == "R":
                if (-10 <= self.change_y <= 0):
                    self.image = self.jumping_frames_r[0]
                elif (0 < self.change_y <= 2):
                    self.image = self.jumping_frames_r[1]
                elif (2 < self.change_y <= 10):
                   self.image = self.jumping_frames_r[2]
                
             else:
                if (-10 <= self.change_y <= 0):
                    self.image = self.jumping_frames_l[0]
                elif (0 < self.change_y <= 2):
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
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height-50 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height-50
 
    def jump(self):
        
        if self.defending == False: 
            # Move o player 2 pixels para baixo para verificar se existe uma plataforma
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2
     
            # Se for possível pular, define a velocidade da subida
            if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT-50:
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
    
# Mecânicas do player
    
    # Coloca o player em posição de defesa
    def defend(self):
        if self.defending == True:
            if self.direction == "R":
                self.image = self.defense_frames_r[0]
            else:
                self.image = self.defense_frames_l[0]
    
    # Quebra a guarda do player
    def guard_break(self):
        pass

    # Desvia um ataque crítico
    def parry(self):
        pass   
    
    # Ataque crítico
    def riposte(self):
        pass
    
    # Faz o player desviar
    def roll(self):
        pass    
    
    # Ataque leve
    def light_atk(self):
        pass    
    
    # Ataque forte
    def heavy_atk(self):
        pass      
    
    # Quando o player recupera vida
    def use_estus(self):
        if self.health < self.maxhealth - 35 and self.estus_rn > 0:
            self.health += 35
            self.estus_rn -= 1
        elif self.health > self.maxhealth - 35 and self.estus_rn > 0:
            self.health = self.maxhealth
            self.estus_rn -= 1
        else:
            pass
        
    # Quando o player recebe dano
    def calc_damage(self, damage, defending):
        # Verifica se o player está defendendo
        if defending:
            if self.stamina - (damage/2) > 0:
                self.stamina -= damage/2 # Reduz stamina
            else:
                self.stamina = 0
                self.guard_break()
                
        else:
            if self.health - damage > 0:
                self.health -= damage # Reduz vida
            else:
                self.health = 0
            
    # Quando o player gasta stamina
    def calc_stamina(self, stm_cost):
        if self.stamina > 0:        
            self.stamina -= stm_cost
        else:
            self.stamina = 0
            
    # Regenera stamina usada
    def stamina_regen(self):
        if self.defending:        
            if self.stamina < self.maxstamina:
                self.stamina += constants.slow_regen
        else:
            if self.stamina < self.maxstamina:
                self.stamina += constants.fast_regen

# Mostra na tela as informações do player
def player_hud(screen, player_health, player_stamina, estus_rn):
    player_maxhealth = 100
    player_maxstamina = 50
    estus_n = constants.estus_BF.render(str(estus_rn), True, constants.WHITE, None)
    estus_n_rect = estus_n.get_rect()
    estus_n_rect.x = 37
    estus_n_rect.y = 30
    image = spritesheet_functions.SpriteSheet("images/link.png")
    
    if estus_rn > 0:
        image = image.get_image(219, 1074, 12, 15, constants.BLACK)
    else:
        image = image.get_image(169, 1074, 12, 15, constants.BLACK)
        
    image = pygame.transform.scale(image, (25, 31))
    screen.blit(image,[10, 10])
    screen.blit(estus_n, estus_n_rect)

    pygame.draw.rect(screen, constants.WHITE, (49, 14, (3*player_maxhealth)+2, 12))
    pygame.draw.rect(screen, constants.GRAY, (50, 15, 3*player_maxhealth, 10))
    if player_health > 0:
        pygame.draw.rect(screen, constants.RED, (50, 15, 3*player_health, 10))
    pygame.draw.rect(screen, constants.WHITE, (49, 29, (3*player_maxstamina)+2, 12))
    pygame.draw.rect(screen, constants.GRAY, (50, 30, 3*player_maxstamina, 10))
    if player_stamina > 0:
        pygame.draw.rect(screen, constants.GREEN, (50, 30, 3*player_stamina, 10))