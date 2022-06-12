import pygame
from constants import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, name,x,y):
        super().__init__() 
        self.name = name
        self.surf = pygame.Surface((32, 32))
        self.surf.fill(self.color())
        self.rect = self.surf.get_rect(center = (x*32+16, y*32+16))
        self.hitbox = self.rect.inflate(-2,-2)

    def color(self):
        return tiles[self.name][0]
    
    def isCollidable(self):
        return tiles[self.name][1]