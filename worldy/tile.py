import pygame
from constants import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, name,x,y):
        super().__init__() 
        self.name = name
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(self.color())
        self.rect = self.surf.get_rect(center = (x*30+15, y*30+15))
        self.hitbox = self.rect.inflate(-2,-2)

    def color(self):
        dico = {"tree_leaf": (112, 141, 19),"path": (130, 212, 53)}
        return dico[self.name]
    
    def isCollidable(self):
        dico = {"tree_leaf": True, "path": False}
        return dico[self.name]