# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:22:09 2016

@author: vini_
"""
 
import pygame, constants, levels, os, player, boss


  
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
    player1 = player.Player()
    
    # Cria os inimigos
    boss1 = boss.Boss()
 
    # Cria todos os levels
    level_list = []
    level_list.append(levels.Level_01(player1, boss1))
    level_list.append(levels.Level_02(player1, boss1))
 
    # Define o level atual
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player1.level = current_level
    boss1.level = current_level
    
    
    # Define posição inicial do player
    player1.rect.x = 150
    player1.rect.y = constants.SCREEN_HEIGHT - player1.rect.height - 12
    active_sprite_list.add(player1)
    
    # Define posição inicial do enemy
    boss1.rect.x = 550
    boss1.rect.y = constants.SCREEN_HEIGHT - boss1.rect.height - 32
    active_sprite_list.add(boss1)
 
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
            
            # Fecha a janela se o usuário clicar em fechar
            if event.type == pygame.QUIT:
                ingame = False               
                
            if event.type == pygame.KEYDOWN:
                
                # Fecha a janela se o usuário pressionar ALT+F4
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                    ingame = False 
                    
                # Move o player para a esquerda
                if event.key == pygame.K_a:
                    player1.go_left()
                if event.key == pygame.K_LEFT:
                    boss1.go_left()
                    
                # Move o player para a direita
                if event.key == pygame.K_d:
                    player1.go_right()
                if event.key == pygame.K_RIGHT:
                    boss1.go_right()
                    
                # Faz o player pular
                if event.key == pygame.K_w:
                    player1.jump()
                if event.key == pygame.K_UP:
                    boss1.jump()
                    
                # Faz o player recuperar vida
                if event.key == pygame.K_e:
                    player1.use_estus()
                    
                # Calcula o dano recebido pelo player
                if event.key == pygame.K_q:
                    player1.calc_damage(40, player1.defending)
                if event.key == pygame.K_p:
                    boss1.calc_damage(200)
                    
                # Calcula a stamina gasta pelo player
                if event.key == pygame.K_r:
                    player1.calc_stamina(15)
                    
                # Regenera a stamina gasta pelo player
                if event.key == pygame.K_f:
                    pygame.time.set_timer(pygame.USEREVENT+1, 5)
                    
                # Coloca o player em posição de defesa
                if event.key == pygame.K_z:
                    player1.defending = True                    
                    player1.defend()
            
            # Calcula a regeneração de stamina do player
            if event.type == pygame.USEREVENT+1:
                player1.stamina_regen()                
                    
            if event.type == pygame.KEYUP:
                
                # Para o movimento do player
                if event.key == pygame.K_a and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_LEFT and boss1.change_x < 0:
                    boss1.stop()
                if event.key == pygame.K_d and player1.change_x > 0:
                    player1.stop()
                if event.key == pygame.K_RIGHT and boss1.change_x > 0:
                    boss1.stop()
                    
                # Para a regeneração de stamina
                if event.key == pygame.K_f:
                    pygame.time.set_timer(pygame.USEREVENT+1, 0)
                    
                # Tira o player da posição de defesa
                if event.key == pygame.K_z:
                    player1.defending = False
 
        # Atualiza o player
        active_sprite_list.update()
 
        # Atualiza os itens no level
        current_level.update()
 
        # Se o player chegar perto do lado direito, muda o world para a esquerda (-x)
        if player1.rect.right >= 500:
            diff = player1.rect.right - 500
            player1.rect.right = 500
            current_level.shift_world(-diff)
  
        # Se o player chegar perto do lado esquerdo, muda o world para a direita (+x)
        if player1.rect.left <= 120:
            diff = 120 - player1.rect.left
            player1.rect.left = 120
            current_level.shift_world(diff)
 
        # Se o player chegar ao fim do level, vai para o próximo level
        current_position = player1.rect.x + current_level.world_shift
        if (current_position < current_level.level_limit) and current_level_no != 0:
            player1.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player1.level = current_level
 
        # Todo código de desenhar
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        player.player_hud(screen, player1.health, player1.stamina, player1.estus_rn)
        boss.boss_hud(screen, boss1.health)
        
        # Limita os frames por segundo
        clock.tick(constants.FPS)
 
        # Atualiza a janela com o que foi desenhado
        pygame.display.update()
 
    pygame.quit() #Termina o jogo
 
if __name__ == "__main__":
    main()