# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:22:09 2016

@author: vini_
"""
 
import pygame, constants, levels, os, player, boss, random
  
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
    player1.enemies.append(boss1)
    boss1.players.append(player1)
 
    # Cria todos os levels
    level_list = []
    level_list.append(levels.Level_01(player1, boss1, screen))
    level_list.append(levels.Level_02(player1, boss1, screen))
 
    # Define o level atual
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player1.level = current_level
#    if current_level == 1:
    boss1.level = current_level

    # Define posição inicial do enemy
    boss1.rect.x = constants.bsp_x
    boss1.rect.y = constants.bsp_y - boss1.rect.height
    active_sprite_list.add(boss1)
    
    # Define posição inicial do player
    player1.rect.x = constants.psp_x
    player1.rect.y = constants.psp_y - player1.rect.height
    active_sprite_list.add(player1)
     
    #Loop até o usuário fechar o jogo
    ingame = True
 
    # Controla quão rápido a janela atualiza
    clock = pygame.time.Clock()
    
    # Inicializa o joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 1:
        joystick = pygame.joystick.Joystick(1)
        joystick.init()
    button_triangle = False
    
    # Mostra a tela de início
    levels.start_screen()
    
    # Mostra a tela de instruções
    levels.instructions()
    
    # Toca música de fundo
    levels.play(current_level_no)
    
    current_position = 0
    
    printa = pygame.USEREVENT + 1
    pygame.time.set_timer(printa, 1)
    estus_regen = pygame.USEREVENT + 2
    stm_regen = pygame.USEREVENT + 3
    pygame.time.set_timer(stm_regen, 100)
    player_roll = pygame.USEREVENT + 4
    boss_roll = pygame.USEREVENT + 5
 
    # -------- Main Program Loop -----------
    while ingame:
        
        if pygame.joystick.get_count() > 1:
            # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo horizontal, onde (0) é parado
            axis_lh = joystick.get_axis(0)
            
            # Recebe valor inteiro de (-1) e (1) para os botões direcionais, onde (0) é parado
            hat = joystick.get_hat(0)
            
            # Mapa de botões, recebem valor booleano quando pressionados
#            button_square = joystick.get_button(0)
#            button_x = joystick.get_button(1)
#            button_circle = joystick.get_button(2)
            button_triangle = joystick.get_button(3)
#            button_L1 = joystick.get_button(4)
#            button_R1 = joystick.get_button(5)
#            button_L2 = joystick.get_button(6)
#            button_R2 = joystick.get_button(7)
#            button_start = joystick.get_button(9)
        
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            
            # Fecha a janela se o usuário clicar em fechar
            if event.type == pygame.QUIT:
                ingame = False
                
#==============================================================================
#             Eventos de Joystick
#==============================================================================
            if pygame.joystick.get_count() > 1:
                
                if (hat == ((-1,0) or (-1,1) or (-1,-1))) or axis_lh <= -0.5:
                    if player1.possible("move"):
                        player1.go_left()
                        
                if (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5:
                    if player1.possible("move"):
                        player1.go_right()
                        
                if (hat == ((0,0) or (0,1) or (0,-1))) and (-0.5 < axis_lh < 0.5) and (player1.change_x != 0):
                    player1.stop()
                    
                if event.type == pygame.JOYBUTTONDOWN:
                        
#                    if button_x:
                    if event.button == 1:
                        if player1.possible("jump"):
                            player1.jump()
                            
#                    if button_circle:
                    if event.button == 2:
                        if player1.possible("roll"):
                            player1.active_roll()
                            pygame.time.set_timer(player_roll, 1)
                            
#                    if button_square:
                    if event.button == 0:
                        player1.drinking = True
                        if player1.possible("estus"):
                            player1.recovering = True
                            player1.use_estus()
                            pygame.time.set_timer(estus_regen, 100)
                            
#                    if button_L1:
                    if event.button == 4:
                        if player1.possible("defend"):
                            player1.defend()
                        
#                    if button_L2:
                    if event.button == 6:
                        if player1.possible("parry"):
                            player1.calc_stamina(15)
                            player1.parrying = True
                            
#                    if button_R1:
                    if event.button == 5:
                        if player1.possible("latk"):
                            player1.calc_stamina(15)
                            player1.latk = True
                            
#                    if button_R2:
                    if event.button == 7:
                        if player1.possible("hatk"):
                            player1.calc_stamina(25)
                            player1.hatk = True
                            
#                    if button_start:
                    if event.button == 9:
                        if current_level_no != 1:
                            levels.instructions()
                            
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 4:
                        player1.defending = False
                    
#==============================================================================
#             Eventos de Teclado
#==============================================================================
                
            if event.type == pygame.KEYDOWN:
                
                # Fecha a janela se o usuário pressionar ALT+F4
                if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                    ingame = False
                    
    #                if pygame.joystick.get_count() == 0:
                # Move o player para a esquerda
                if (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                    if player1.possible("move"):
                        player1.go_left()
                    
                # Move o player para a direita
                if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                    if player1.possible("move"):
                        player1.go_right()
                # Faz o player pular
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if player1.possible("jump"):
                        player1.jump()
                    
                # Faz o player recuperar vida
                if event.key == pygame.K_e:
                    player1.drinking = True
                    if player1.possible("estus"):
                        player1.recovering = True
                        player1.use_estus()
                        pygame.time.set_timer(estus_regen, 100)
                    
                # Calcula o dano recebido pelo player
                if event.key == pygame.K_q:
#                        player1.health -= 10
                        boss1.health -= 100
                    
                if event.key == pygame.K_p:
                    if player1.possible("latk"):
                        player1.calc_stamina(15)
                        player1.latk = True
                    
                if event.key == pygame.K_o:
                    if player1.possible("hatk"):
                        player1.calc_stamina(25)
                        player1.hatk = True
                    
                if event.key == pygame.K_i:
                    if player1.possible("parry"):
                        player1.calc_stamina(15)
                        player1.parrying = True
                    
                if event.key == pygame.K_l:
                    if boss1.possible("latk"):
                        boss1.latk = True
    
                if event.key == pygame.K_k:
                    if boss1.possible("hatk"):
                        boss1.hatk = True
                    
                # Calcula a stamina gasta pelo player
                if event.key == pygame.K_r:
                    player1.stamina = player1.maxstamina
                    player1.estus_rn = 5
                    
                if event.key == pygame.K_t:
                    boss1.health += 100
                    
                if event.key == pygame.K_SPACE:
                    if player1.possible("roll"):
                        player1.active_roll()
                        pygame.time.set_timer(player_roll, 1)
                    
                # Coloca o player em posição de defesa
                if event.key == pygame.K_z:
                    if player1.possible("defend"):
                        player1.defending = True
            
                # Abre a tela de instruções
                if event.key == pygame.K_RETURN or pressed[pygame.K_KP_ENTER]:
                    if current_level_no != 1:
                        levels.instructions()
                        
                if event.key == pygame.K_m:
                    current_level.shift_world(-player1.look_dist)
                    boss1.rect.right -= player1.look_dist
                    player1.rect.right -= player1.look_dist
                    player1.direction = "R"
                    
                if event.key == pygame.K_n:
                    current_level.shift_world(player1.look_dist)
                    boss1.rect.right += player1.look_dist
                    player1.rect.right += player1.look_dist
                    player1.direction = "L"
                
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
#                print()
                    
            if event.type == pygame.KEYUP:
                
                # Para o movimento do player
                if event.key == pygame.K_a and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_LEFT and player1.change_x < 0:
                    player1.stop()
                if event.key == pygame.K_d and player1.change_x > 0:
                    player1.stop()
                if event.key == pygame.K_RIGHT and player1.change_x > 0:
                    player1.stop()
                    
                # Tira o player da posição de defesa
                if event.key == pygame.K_z:
                    player1.defending = False
#                    player1.guard = True
#                    boss1.defending = False
#                    boss1.guard = True
                    
                if event.key == pygame.K_n:
                    current_level.shift_world(-player1.look_dist//2)
                    boss1.rect.right -= player1.look_dist//2
                    player1.rect.right -= player1.look_dist//2
                    
                if event.key == pygame.K_m:
                    current_level.shift_world(player1.look_dist//2)
                    boss1.rect.right += player1.look_dist//2
                    player1.rect.right += player1.look_dist//2
                    
#==============================================================================
#         Outros Eventos
#==============================================================================
        
        # Habilita/impede o roll do player/boss
        if boss1.rolling:
            pygame.time.set_timer(boss_roll, 1)
            
        if constants.player_roll_frames <= 0:
            pygame.time.set_timer(player_roll, 0)
        if constants.boss_roll_frames <= 0:
            pygame.time.set_timer(boss_roll, 0)
                    
        # Atualiza o player
        active_sprite_list.update()
 
        # Atualiza os itens no level
        current_level.update()
 
        current_position = player1.rect.x + abs(current_level.world_shift)
        if (current_position > 600 and current_position < 9000 and current_level_no != 1) \
        or (current_position > 150 and current_position < 840 and current_level_no == 1):
            # Se o player chegar perto do lado direito, muda o world para a esquerda (-x)
            if player1.rect.right >= 700:
                diff = player1.rect.right - 700
                player1.rect.right = 700
                current_level.shift_world(-diff)
                boss1.rect.right -= diff
      
            # Se o player chegar perto do lado esquerdo, muda o world para a direita (+x)
            if player1.rect.left <= 120:
                diff = 120 - player1.rect.left
                player1.rect.left = 120
                current_level.shift_world(diff)
                boss1.rect.left += diff
        
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
        if (current_position > current_level.level_limit) and current_level_no != 1 and (pressed[pygame.K_SPACE] or button_triangle) and player1.on_ground:
            player1.rect.x = 150
            pygame.mixer.music.stop()
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player1.level = current_level
                levels.play(current_level_no)
                
        # Todo código de desenhar
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        if current_level_no == 0:
            black_surf = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
            black_surf.fill((0, 0, 0, 10))
            screen.blit(black_surf, (0, 0))
        player1.player_hud(screen)
        if current_level_no == 1:
            boss1.boss_hud(screen)
        if current_position > current_level.level_limit:
            if pygame.joystick.get_count() > 1:
                levels.msg_player("Press TRIANGLE on the fog wall", screen)
            else:
                levels.msg_player("Press SPACE on the fog wall", screen)
        
        # Limita os frames por segundo
        clock.tick(constants.FPS)
        
        # Constantes auxiliares para AI do boss
        if constants.a > 60:
            constants.a = 0
            boss1.l = random.choice([0, 1, 2, 3, 4])
            boss1.m = random.choice([0, 1])
            boss1.n = random.uniform(0, 1)
            boss1.o = random.uniform(0, 1)
#            print("-----CHOICE-----",boss1.l)
        else:
            constants.a += 1
        
        # Retira a animação de dano do player após 30 frames
        if player1.takedmg:
            if constants.b > 30:
                player1.takedmg = False
                constants.b = 0
            else:
                constants.b += 1

        # AI do boss
        boss1.AI(player1, clock)
        
        # Mostra tela de morte/vitória
        if not player1.live:        
            player.dead_screen(screen, player1, current_position)
            pygame.mixer.music.stop()
        elif not boss1.live:
            boss.dead_screen(screen, boss1, current_position)
            pygame.mixer.music.stop()
            player1.stop()
 
        # Atualiza a janela com o que foi desenhado
        pygame.display.update()
 
    pygame.quit() #Termina o jogo
    quit()
 
if __name__ == "__main__":
    main()