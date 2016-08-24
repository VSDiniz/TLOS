# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:22:09 2016

@author: vini_
"""
 
import pygame, constants, levels, os
from player import Player
from enemy import Enemy

  
def main():
    # Main Program
    pygame.init()
 
    # Define altura, largura e posição inicial da janela
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    os.environ["SDL_VIDEO_WINDOW_POS"] = '200,50'
    screen = pygame.display.set_mode((1, 1))
    
    # Define ícone e label da janela
    icon = pygame.image.load("images/triforceicon.png")
    pygame.display.set_caption("The Legend Of Souls")
    pygame.display.set_icon(icon)
    
    # Esconde o cursor do mouse
    pygame.mouse.set_visible(0)
 
    # Cria o player
    player = Player()
    
    # Cria os inimigos
    enemy = Enemy()
 
    # Cria todos os levels
    level_list = []
    level_list.append(levels.Level_01(player, enemy))
    level_list.append(levels.Level_02(player, enemy))
 
    # Define o level atual
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    enemy.level = current_level
    
    
    # Define posição inicial do player
    player.rect.x = 150
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 12
    active_sprite_list.add(player)
    
    # Define posição inicial do enemy
    enemy.rect.x = 550
    enemy.rect.y = constants.SCREEN_HEIGHT - enemy.rect.height - 32
    active_sprite_list.add(enemy)
 
    #Loop até o usuário fechar o jogo
    ingame = True
 
    # Controla quão rápido a janela atualiza
    clock = pygame.time.Clock()
    
    # Mostra a tela de início
    levels.start_screen()
 
    # -------- Main Program Loop -----------
    while ingame:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                ingame = False # Fecha a janela se o usuário clicar em fechar
            if event.type == pygame.KEYDOWN:
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                    ingame = False # Fecha a janela se o usuário pressionar ALT+F4
                    
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_LEFT:
                    enemy.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_RIGHT:
                    enemy.go_right()
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_UP:
                    enemy.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_LEFT and enemy.change_x < 0:
                    enemy.stop()
                if event.key == pygame.K_RIGHT and enemy.change_x > 0:
                    enemy.stop()
 
        # Atualiza o player
        active_sprite_list.update()
 
        # Atualiza os itens no level
        current_level.update()
 
        # Se o player chegar perto do lado direito, muda o world para a esquerda (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
  
        # Se o player chegar perto do lado esquerdo, muda o world para a direita (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # Se o player chegar ao fim do level, vai para o próximo level
        current_position = player.rect.x + current_level.world_shift
        if (current_position < current_level.level_limit) and current_level_no != 0:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        # Todo código de desenhar
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        
        # Limita os frames por segundo
        clock.tick(60)
 
        # Atualiza a janela com o que foi desenhado
        pygame.display.flip()
 
    pygame.quit() #Termina o jogo
 
if __name__ == "__main__":
    main()