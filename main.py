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
    os.environ["SDL_VIDEO_WINDOW_POS"] = '150,50'
    screen = pygame.display.set_mode((1, 1))
    
    # Define ícone e label da janela
    icon = pygame.image.load("images/triforceicon.png")
    pygame.display.set_caption("The Legend Of Souls")
    pygame.display.set_icon(icon)
    
    # Esconde o cursor do mouse
    pygame.mouse.set_visible(0)
    
    # Cria os inimigos
    boss1 = boss.Boss()
    
    # Cria o player
    player1 = player.Player()
 
    # Cria todos os levels
    level_list = []
    level_list.append(levels.Level_01(player1, boss1, screen))
    level_list.append(levels.Level_02(player1, boss1, screen))
 
    # Define o level atual
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player1.level = current_level
    boss1.level = current_level
    
    
    # Define posição inicial do player
    player1.rect.x = 6000#1075
    player1.rect.y = constants.SCREEN_HEIGHT - (player1.rect.height - 45)
    active_sprite_list.add(player1)
    
    # Define posição inicial do enemy
    boss1.rect.x = 750
    boss1.rect.y = constants.SCREEN_HEIGHT - boss1.rect.height - 30
    active_sprite_list.add(boss1)
 
    #Loop até o usuário fechar o jogo
    ingame = True
 
    # Controla quão rápido a janela atualiza
    clock = pygame.time.Clock()
    
    # Mostra a tela de início
    levels.start_screen()
    
    # Mostra a tela de instruções
    levels.instructions()
    
    levels.play(current_level_no)
    
    current_position = 0
    
#    printa = pygame.USEREVENT + 1
#    pygame.time.set_timer(printa, 500)
    estus_regen = pygame.USEREVENT + 2
    stm_regen = pygame.USEREVENT + 3
    pygame.time.set_timer(stm_regen, 100)
    player_roll = pygame.USEREVENT + 4
    boss_roll = pygame.USEREVENT + 5
 
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
                    if player1.possible("move"):
                        player1.go_left()
                if event.key == pygame.K_LEFT:
                    boss1.go_left()
                    
                # Move o player para a direita
                if event.key == pygame.K_d:
                    if player1.possible("move"):
                        player1.go_right()
                        
                if event.key == pygame.K_RIGHT:
                    boss1.go_right()
                    
                # Faz o player pular
                if event.key == pygame.K_w:
                    if player1.possible("jump"):
                        player1.jump()
                if event.key == pygame.K_UP:
                    boss1.jump()
                    
                # Faz o player recuperar vida
                if event.key == pygame.K_e:                 
                    if player1.possible("estus"):
                        player1.recovering = True
                        player1.use_estus()
                        pygame.time.set_timer(estus_regen, 100)
                    
                # Calcula o dano recebido pelo player
                if event.key == pygame.K_q:
                    if not player1.defending:
                        player1.takedmg = True
                    player1.calc_damage(20)
                    
                if event.key == pygame.K_p:
                    if player1.possible("latk"):
                        player1.calc_stamina(15)
                        player1.latk = True
#                    boss1.calc_damage(200)
                    
                if event.key == pygame.K_o:
                    if player1.possible("hatk"):
                        player1.calc_stamina(25)
                        player1.hatk = True
                    
                if event.key == pygame.K_i:
                    if player1.possible("parry"):
                        player1.calc_stamina(15)
                        player1.parrying = True
                    
                if event.key == pygame.K_l:
                    boss1.latk = True

                if event.key == pygame.K_k:
                    boss1.hatk = True                    
                    
                # Calcula a stamina gasta pelo player
                if event.key == pygame.K_r:
                    player1.stamina = player1.maxstamina
#                    boss1.parrying = True
                    
                if event.key == pygame.K_SPACE:
                    if player1.possible("roll"):
                        player1.active_roll()
                        pygame.time.set_timer(player_roll, 1)
#                    if not boss1.jumping:
#                        boss1.active_roll()
#                        pygame.time.set_timer(boss_roll, 1)
                    
                # Coloca o player em posição de defesa
                if event.key == pygame.K_z:
                    if player1.possible("move"):
                        player1.defend()
#                    boss1.defend()
                
                # Abre a tela de instruções
                if event.key == pygame.K_RETURN or pressed[pygame.K_KP_ENTER]:
                    levels.instructions()
            
            # Calcula a regeneração de vida do player
            if event.type == estus_regen:
                player1.life_regen(estus_regen)
                    
            # Calcula a regeneração de stamina do player
            if event.type == stm_regen:
                player1.stamina_regen()
                
            if event.type == player_roll:
                player1.rolling = True
                
            if event.type == boss_roll:
                boss1.rolling = True
                       
                        
            """ -------------------- PRINTA -------------------- """            
#            if event.type == printa:
#                print(player1.defending, player1.guard)
                    
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
                    
                # Tira o player da posição de defesa
                if event.key == pygame.K_z:
                    player1.defending = False
#                    player1.guard = True
#                    boss1.defending = False
#                    boss1.guard = True
                    
        if constants.player_roll_frames <= 0:            
            pygame.time.set_timer(player_roll, 0)
                    
        # Atualiza o player
        active_sprite_list.update()
 
        # Atualiza os itens no level
        current_level.update()
 
        # Se o player chegar perto do lado direito, muda o world para a esquerda (-x)
        if player1.rect.right >= 700:
            diff = player1.rect.right - 700
            player1.rect.right = 700
            current_level.shift_world(-diff)
  
        # Se o player chegar perto do lado esquerdo, muda o world para a direita (+x)
        if player1.rect.left <= 120:
            diff = 120 - player1.rect.left
            player1.rect.left = 120
            current_level.shift_world(diff)
        
#==============================================================================
#         # Se o player chegar perto do fundo, muda o world para cima (-y)
#         if player1.rect.bottom >= 550:
#             diff = player1.rect.bottom - 550
#             player1.rect.bottom = 550
#             current_level.shift_world(-diff)
#             
#         # Se o player chegar perto do topo, muda o world para baixo (+y)
#         if player1.rect.top <= 100:
#             diff = 100 - player1.rect.top
#             player1.rect.top = 100
#             current_level.shift_world(diff)      
#==============================================================================
 
        # Se o player chegar ao fim do level, vai para o próximo level
        pressed = pygame.key.get_pressed()
        current_position = player1.rect.x + abs(current_level.world_shift)
        if (current_position > current_level.level_limit) and current_level_no != 1 and pressed[pygame.K_SPACE] and player1.on_ground:
            player1.rect.x = 650
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player1.level = current_level
                
#        if (player1.rect.x < 180) and current_level_no == 1:
#            player1.stop()

        # Todo código de desenhar
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        player1.player_hud(screen)
        if current_level_no == 1:
            boss1.boss_hud(screen)
        if current_position > current_level.level_limit:
            levels.msg_player("Press SPACE on the fog wall", screen)
        
        # Limita os frames por segundo
        clock.tick(constants.FPS)
        
        if not player1.live:        
            player.dead_screen(screen, player1)
        elif not boss1.live:
            boss.dead_screen(screen)
 
        # Atualiza a janela com o que foi desenhado
        pygame.display.update()
 
    pygame.quit() #Termina o jogo
    quit()
 
if __name__ == "__main__":
    main()