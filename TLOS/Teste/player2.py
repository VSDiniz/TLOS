import pygame

class player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=36
        self.height=48
        self.velocity=0
        
    def update(self,gravity):
        self.velocity+=gravity
        self.y-=self.velocity
        
    def render(self,window):
        
         if (collision==True):
             
            pygame.draw.rect(window,red,(self.x,self.y,self.width,self.height))
 
        else:
 
            pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))
            