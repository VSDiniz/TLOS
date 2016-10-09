# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:49:28 2016

@author: vini_
"""

def check_collide(player, enemies):
    """checa a colisão de movimento entre o player e o inimigo"""
    for enemy in enemies:
        player.left = player.rect.centerx - 15
        player.right = player.rect.centerx + 15
        enemy.left = enemy.rect.centerx - 15
        enemy.right = enemy.rect.centerx + 15
        
        if enemy.live and (player.possible('move') or enemy.possible('move')):
            
            if (player.rect.bottom <= enemy.rect.bottom and player.rect.bottom >= enemy.rect.top + 120):# \
#            or (player.rect.top >= enemy.rect.top and player.rect.bottom <= enemy.rect.bottom) \
#            or (player.rect.top <= enemy.rect.top and player.rect.bottom >= enemy.rect.top + 70):
                if player.left < enemy.left and player.right > enemy.left:
                    player.rect.centerx = enemy.left - 15
                if player.right > enemy.right and player.left < enemy.right:
                    player.rect.centerx = enemy.right + 15

#        if player.latk:
#            if hit(player,enemy):
#                enemy.calc_damage()
#        if enemy.latk:
#            if hit(enemy,player):
#                player.calc_damage()
#        if player.hatk:
#            if hit(player,enemy):
#                enemy.calc_damage()
#        if enemy.hatk:
#            if hit(enemy,player):
#                player.calc_damage()
            
def hit(Hit1,Hit2):
    if Hit1.rect.colliderect(Hit2.rect):
        if Hit1.direction == 'R' and Hit1.rect.centerx < Hit2.rect.centerx:
            return True
        elif Hit1.direction == 'L' and Hit1.rect.centerx > Hit2.rect.centerx:
            return True