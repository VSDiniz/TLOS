# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 07:58:09 2016

@author: vini_
"""
import pygame
class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height,colorkey = None):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
 
        # Return the image
        return image