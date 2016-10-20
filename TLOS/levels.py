# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:53:45 2016

@author: vini_
"""

import pygame, constants, platforms, sounds, sys

class Level():
    # Classe genérica para definir um level
 
    def __init__(self, player, enemy, screen, bonfire):
        # Lista de sprites usadas em todos os levels
        self.platform_list = None
        self.enemy_list = None
        self.bonfire_list = None
 
        # Imagem de background
        self.background = None
 
        # Quanto o world se deslocou esquerda/direita
        self.world_shift = 0
        self.world_shifty = 0
        self.level_limit = -900
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.bonfire_list = pygame.sprite.Group()
        self.player = player
        self.enemy = enemy
        self.bonfire = bonfire
 
    # Atualiza tudo num level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.bonfire_list.update()
 
    def draw(self, screen):
        # Desenha tudo num level 
        # Desenha o background
        screen.fill(constants.SKYBLUE)
        # Faz o world se deslocar mais lentamente que o player
        screen.blit(self.background, (self.world_shift, self.world_shifty))
 
        # Desenha todas as listas de sprites
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.bonfire_list.draw(screen)
         
    def shift_world(self, shift_x):
        # Desloca o world quando o player se move
        # Mantém controle de quanto o world se desloca
        self.world_shift += shift_x
#        self.world_shifty += shift_y

        # Passa por toda a lista de sprites e altera
        for platform in self.platform_list:
            platform.rect.x += shift_x
#            platform.rect.y += shift_y
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
#            enemy.rect.y += shift_y
            
    def shifty_world(self, shift_y):
        
        self.world_shifty += shift_y
        
        for platform in self.platform_list:
            platform.rect.y += shift_y
            
        for enemy in self.enemy_list:
            enemy.rect.y += shift_y
            
# Cria as plataformas para o level
class Level_01(Level):
 
    def __init__(self, player, enemy, screen, bonfire):
 
        Level.__init__(self, player, enemy, screen, bonfire)
 
        self.background = pygame.image.load("images/map1(3).png").convert()
        self.background = pygame.transform.scale2x(self.background)
        self.level_limit = 9150
 
        # Array com o tipo de plataforma e coordenadas (x,y) para localização
#        level = [[platforms.plat1, 928, 550],
#                 [platforms.plat2, 1760, 550],
#                 [platforms.plat3, 2624, 550],
#                 [platforms.plat4, 3616, 550],
#                 [platforms.plat5, 4832, 550],
#                 [platforms.plat2, 5696, 550],
#                 [platforms.plat6, 6500, 550],
#                 [platforms.stone_wall, 6750, 0],
#                 [platforms.floatplat, 4450, 390],
#                 [platforms.floatplat, 5442, 390],
#                 [platforms.block2, 4192, 581],
#                 [platforms.block1, 4384, 550],
#                 [platforms.block1, 4608, 550],
#                 [platforms.block2, 4768, 581]]
        level = [[platforms.plat1, 864, 548],
                 [platforms.plat1, 1920, 548],
                 [platforms.plat1, 2976, 548],
                 [platforms.plat1, 4032, 548],
                 [platforms.plat1, 5440, 548],
                 [platforms.plat1, 6496, 548],
                 [platforms.plat1, 8032, 548],
                 [platforms.plat1, 9056, 548],
                 [platforms.plat3, 7232, 548],
                 [platforms.plat3, 7776, 548],
                 [platforms.floatplat3, 642, 228],
#                 [platforms.floatplat3, 7584, 358],
                 [platforms.floatplat3, 482, 356],
                 [platforms.floatplat3, 642, 451],
                 [platforms.floatplat4, 5056, 452],
                 [platforms.stone_wall, 9248, 0],
                 [platforms.plat2, 9952, 548],
                 [platforms.stone_wall, 9952, 0],
                 [platforms.stone_wall, 10909, 0],
                 [platforms.black_wall, 6912, 612],
                 [platforms.black_wall, 8320, 612],
                 [platforms.block1, 7584, 676],
                 [platforms.block1, 7744, 804],
                 [platforms.block1, 7008, 932],
                 [platforms.block1, 7264, 932],
                 [platforms.block1, 7584, 932],
                 [platforms.block1, 7872, 932],
                 [platforms.block1, 7744, 1060],
                 [platforms.block1, 8000, 1060],
                 [platforms.block1, 8160, 1060],
                 [platforms.block1, 7008, 1188],
                 [platforms.block1, 7264, 1188],
                 [platforms.block1, 7584, 1188],
                 [platforms.block1, 7872, 1188],
                 [platforms.block1, 8000, 1316],
                 [platforms.block1, 8128, 1412],
                 [platforms.block2, 8256, 804],
                 [platforms.block3, 7104, 804],
                 [platforms.block3, 7360, 804],
                 [platforms.block3, 8000, 804],
                 [platforms.block3, 7104, 1060],
                 [platforms.block3, 7360, 1060],
                 [platforms.black_floor, 7904, 1572],]
 
        # Passa pelo array e adiciona plataformas
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            block.enemy = self.enemy
            self.platform_list.add(block)
 
#==============================================================================
#         # Adiciona uma plataforma móvel
#         block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
#         block.rect.x = 1350
#         block.rect.y = 380
#         block.boundary_left = 1350
#         block.boundary_right = 1600
#         block.change_x = 1
#         block.player = self.player
#         block.enemy = self.enemy
#         block.level = self
#         self.platform_list.add(block)
#==============================================================================
 
 
class Level_02(Level):
 
    def __init__(self, player, enemy, screen, bonfire):
 
        Level.__init__(self, player, enemy, screen, bonfire)
 
        self.background = pygame.image.load("images/map2(1).png").convert()
        self.background = pygame.transform.scale2x(self.background)
        self.level_limit = 3600
 
        level = [[platforms.plat2, 0, 550],
                 [platforms.stone_wall, 129, 0],
                 [platforms.stone_wall, 1086, 0]]
 
 
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
#==============================================================================
#         block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
#         block.rect.x = 1500
#         block.rect.y = 300
#         block.boundary_top = 100
#         block.boundary_bottom = 550
#         block.change_y = -1
#         block.player = self.player
#         block.level = self
#         self.platform_list.add(block)
#==============================================================================
        
def start_screen():
    
    # Inicializa o joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 1:
        joystick = pygame.joystick.Joystick(1)
        joystick.init()
        
    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    pygame.mixer.music.load("sounds/TLOZ/Main Theme (Classic).wav")
    pygame.mixer.music.play(-1)
        
    game_title = constants.soulsFont_M.render("THE LEGEND OF SOULS", True, constants.WHITE, None)
    if pygame.joystick.get_count() > 1:
        press_start = constants.bitsFont_M.render("Press OPTIONS", True, constants.WHITE, None)
        not_start = constants.bitsFont_P.render("I said OPTIONS", True, constants.WHITE, None)
    else:
        press_start = constants.bitsFont_M.render("Press ENTER", True, constants.WHITE, None)
        not_start = constants.bitsFont_P.render("I said ENTER", True, constants.WHITE, None)
    
    instart = True

    while instart:
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
        game_title_rect = game_title.get_rect()
        game_title_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 525)
        screen1.blit(game_title, game_title_rect)
        press_start_rect = press_start.get_rect()
        press_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 100)
        screen1.blit(press_start, press_start_rect)
        pygame.display.update()
        
        for event in pygame.event.get():
            if pygame.joystick.get_count() > 1:
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 9:
                        instart = False
                    else:
                        not_start_rect = not_start.get_rect() # Zoa o usuário
                        not_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 75)
                        screen1.blit(not_start, not_start_rect)
                        pygame.display.update()
                        pygame.event.wait()
            else:
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.KEYDOWN:
                    if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                        sys.exit()#pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                        
                    elif pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]:# or event.button == 9:
                        instart = False # Sai da tela de início
                    else:
                        not_start_rect = not_start.get_rect() # Zoa o usuário
                        not_start_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 75)
                        screen1.blit(not_start, not_start_rect)
                        pygame.display.update()
                        pygame.event.wait()
                                        
                    
def instructions(player):
    
    # Inicializa o joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 1:
        joystick = pygame.joystick.Joystick(1)
        joystick.init()
    
    background = pygame.image.load("images/scroll.jpg").convert()
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        
    scroll1 = constants.scrollFont_M.render("INSTRUCTIONS", True, constants.BLACK, None)
    scroll12 = constants.scrollFont_P.render("to switch to statistics", True, constants.BLACK, None)
    if pygame.joystick.get_count() <= 1:
        scroll2 = constants.scrollFont_P.render("Press A or LEFT Arrow and D or RIGHT Arrow to move", True, constants.BLACK, None)
        scroll3 = constants.scrollFont_P.render("Press W or UP Arrow to jump", True, constants.BLACK, None)
        scroll4 = constants.scrollFont_P.render("Press O to recover HP", True, constants.BLACK, None)
        scroll5 = constants.scrollFont_P.render("Press J to light attack and K to heavy attack", True, constants.BLACK, None)
        scroll6 = constants.scrollFont_P.render("Press L to defend", True, constants.BLACK, None)
        scroll7 = constants.scrollFont_P.render("Press I to parry and light attack to riposte", True, constants.BLACK, None)
        scroll8 = constants.scrollFont_P.render("Press SPACE to roll", True, constants.BLACK, None)
        scroll9 = constants.scrollFont_P.render("Press ENTER to exit the instructions", True, constants.BLACK, None)
        scroll10 = constants.scrollFont_P.render("Press E or Q to look around", True, constants.BLACK, None)
        scroll11 = constants.scrollFont_P.render("Press A or LEFT Arrow and D or RIGHT Arrow", True, constants.BLACK, None)
    else:
        scroll2 = constants.scrollFont_P.render("Press the D Pad or LEFT Analog to move", True, constants.BLACK, None)
        scroll3 = constants.scrollFont_P.render("Press X to jump", True, constants.BLACK, None)
        scroll4 = constants.scrollFont_P.render("Press SQUARE to recover HP", True, constants.BLACK, None)
        scroll5 = constants.scrollFont_P.render("Press R1 attack and R2 to heavy attack", True, constants.BLACK, None)
        scroll6 = constants.scrollFont_P.render("Press L1 to defend", True, constants.BLACK, None)
        scroll7 = constants.scrollFont_P.render("Press L2 to parry and light attack to riposte", True, constants.BLACK, None)
        scroll8 = constants.scrollFont_P.render("Press CIRCLE to roll", True, constants.BLACK, None)
        scroll9 = constants.scrollFont_P.render("Press OPTIONS to exit the instructions", True, constants.BLACK, None)
        scroll10 = constants.scrollFont_P.render("Move the RIGHT Analog to look around", True, constants.BLACK, None)
        scroll11 = constants.scrollFont_P.render("Press the D Pad or LEFT Analog", True, constants.BLACK, None)
        
    instruct = True

    while instruct:
        
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
    
        scroll1_rect = scroll1.get_rect()
        scroll1_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 525)
        screen1.blit(scroll1, scroll1_rect)
        scroll2_rect = scroll2.get_rect()
        scroll2_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 450)
        screen1.blit(scroll2, scroll2_rect)
        scroll3_rect = scroll3.get_rect()
        scroll3_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 420)
        screen1.blit(scroll3, scroll3_rect)
        scroll4_rect = scroll4.get_rect()
        scroll4_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 390)
        screen1.blit(scroll4, scroll4_rect)
        scroll5_rect = scroll5.get_rect()
        scroll5_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 360)
        screen1.blit(scroll5, scroll5_rect)
        scroll6_rect = scroll6.get_rect()
        scroll6_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 330)
        screen1.blit(scroll6, scroll6_rect)
        scroll7_rect = scroll7.get_rect()
        scroll7_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 300)
        screen1.blit(scroll7, scroll7_rect)
        scroll8_rect = scroll8.get_rect()
        scroll8_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 270)
        screen1.blit(scroll8, scroll8_rect)
        scroll9_rect = scroll9.get_rect()
        scroll9_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 50)
        screen1.blit(scroll9, scroll9_rect)
        scroll10_rect = scroll10.get_rect()
        scroll10_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 240)
        screen1.blit(scroll10, scroll10_rect)
        scroll11_rect = scroll11.get_rect()
        scroll11_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 110)
        screen1.blit(scroll11, scroll11_rect)
        scroll12_rect = scroll12.get_rect()
        scroll12_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 80)
        screen1.blit(scroll12, scroll12_rect)

        pygame.display.update()
        
        for event in pygame.event.get():
            if pygame.joystick.get_count() > 1:
                axis_lh = joystick.get_axis(0)
                hat = joystick.get_hat(0)
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 9:
                        sounds.menu_close.play()
                        instruct = False
                    elif (hat == ((-1,0) or (-1,1) or (-1,-1))) or (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5 or axis_lh <= -0.5:
                        sounds.menu_cursor.play()
                        instruct = False
                        statistics(player)
            else:            
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.KEYDOWN:
                    if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                        sys.exit()#pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                        
                    elif pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]:
                        sounds.menu_close.play()
                        instruct = False # Sai da tela de instruções
                    elif pressed[pygame.K_a] or pressed[pygame.K_d] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
                        sounds.menu_cursor.play()
                        instruct = False
                        statistics(player)
                        
def statistics(player):
    
    # Inicializa o joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() > 1:
        joystick = pygame.joystick.Joystick(1)
        joystick.init()
    
    background = pygame.image.load("images/scroll.jpg").convert()
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        

    scroll1 = constants.scrollFont_M.render("STATISTICS", True, constants.BLACK, None)
    scroll2 = constants.scrollFont_P.render("Number of DEATHS: " + str(player.DEATH), True, constants.BLACK, None)
    scroll3 = constants.scrollFont_P.render("Number of KILLS: " + str(player.KILL), True, constants.BLACK, None)
    scroll4 = constants.scrollFont_P.render("Total DAMAGE taken: " + str(int(player.DMG_TAKEN)), True, constants.BLACK, None)
    scroll5 = constants.scrollFont_P.render("Total DAMAGE dealt: " + str(player.DMG_DEALT), True, constants.BLACK, None)
    scroll7 = constants.scrollFont_P.render("to switch to instructions", True, constants.BLACK, None)
    if pygame.joystick.get_count() <= 1:
        scroll6 = constants.scrollFont_P.render("Press A or LEFT Arrow and D or RIGHT Arrow", True, constants.BLACK, None)
        scroll9 = constants.scrollFont_P.render("Press ENTER to exit the statistics", True, constants.BLACK, None)
    else:
        scroll6 = constants.scrollFont_P.render("Press the D Pad or LEFT Analog", True, constants.BLACK, None)
        scroll9 = constants.scrollFont_P.render("Press OPTIONS to exit the statistics", True, constants.BLACK, None)
        
    instats = True

    while instats:
        
        screen1 = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        screen1.blit(background, (0,0))
    
        scroll1_rect = scroll1.get_rect()
        scroll1_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 525)
        screen1.blit(scroll1, scroll1_rect)
        scroll2_rect = scroll2.get_rect()
        scroll2_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 450)
        screen1.blit(scroll2, scroll2_rect)
        scroll3_rect = scroll3.get_rect()
        scroll3_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 420)
        screen1.blit(scroll3, scroll3_rect)
        scroll4_rect = scroll4.get_rect()
        scroll4_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 390)
        screen1.blit(scroll4, scroll4_rect)
        scroll5_rect = scroll5.get_rect()
        scroll5_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 360)
        screen1.blit(scroll5, scroll5_rect)
        scroll6_rect = scroll6.get_rect()
        scroll6_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 110)
        screen1.blit(scroll6, scroll6_rect)
        scroll7_rect = scroll7.get_rect()
        scroll7_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 80)
        screen1.blit(scroll7, scroll7_rect)
        scroll9_rect = scroll9.get_rect()
        scroll9_rect.center = (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 50)
        screen1.blit(scroll9, scroll9_rect)

        pygame.display.update()
        
        for event in pygame.event.get():
            if pygame.joystick.get_count() > 1:
                axis_lh = joystick.get_axis(0)
                hat = joystick.get_hat(0)
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 9:
                        sounds.menu_close.play()
                        instats = False
                    elif (hat == ((-1,0) or (-1,1) or (-1,-1))) or (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5 or axis_lh <= -0.5:
                        sounds.menu_cursor.play()
                        instats = False
                        instructions(player)
            else:            
                pressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()#pygame.quit() # Fecha a janela se o usuário clicar em fechar
                if event.type == pygame.KEYDOWN:
                    if ((pressed[pygame.K_LALT] and pressed[pygame.K_F4]) or (pressed[pygame.K_RALT] and pressed[pygame.K_F4])):
                        sys.exit()#pygame.quit() # Fecha a janela se o usuário pressionar ALT+F4
                        
                    elif pressed[pygame.K_RETURN] or pressed[pygame.K_KP_ENTER]:
                        sounds.menu_close.play()
                        instats = False # Sai da tela de instruções
                    
                    elif pressed[pygame.K_a] or pressed[pygame.K_d] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
                        sounds.menu_cursor.play()
                        instats = False
                        instructions(player)
    
def play(current_level_no):
    if current_level_no == 0:
        pygame.mixer.music.load("sounds/TLOZ/Gerudo Valley Theme.wav")
        pygame.mixer.music.play(-1)
    elif current_level_no == 1:
        pygame.mixer.music.load("sounds/DS/Bloodborne Soundtrack OST - Cleric Beast.wav")
        pygame.mixer.music.play(-1)
#    c = current_level_no
#    k = current_level_no + 1
#    if c == 0:
#        pygame.mixer.music.load("sounds/TLOZ/Gerudo Valley Theme.wav")
#        pygame.mixer.music.play(-1)
#        c += 1
#        return True
#    if k == 1:
#        pygame.mixer.music.load("sounds/DS/Bloodborne Soundtrack OST - Cleric Beast.wav")
#        pygame.mixer.music.play(-1)
#        k += 1
    

def msg_player(msge, screen):
    
    msg = constants.bitsFont_P.render(msge, True, constants.YELLOW, None)
    msg_rect = msg.get_rect()
    msg_rect.centerx = (constants.SCREEN_WIDTH / 2)
    msg_rect.y = constants.SCREEN_HEIGHT / 2 - 200
    screen.blit(msg, (msg_rect.x, msg_rect.y))
    