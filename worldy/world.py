import pygame
from tile import *


class World():
    def __init__(self):
        self.map = []

    def world1(self):
        self.map = [[[["tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf"],["tree_leaf","path"],["tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf","tree_leaf"],[],[],["path","path","path","path","path","path","path","path","path","path"]],[]],
                    [[],[]]]
    
    def load(self,x,y):
        all_sprites = pygame.sprite.Group()
        collide_sprites = pygame.sprite.Group()
        for yd, line in enumerate(self.map[y][x]):
            for xd, name in enumerate(line):
                tile = Tile(name,xd,yd)
                all_sprites.add(tile)
                if tile.isCollidable(): collide_sprites.add(tile)
        return all_sprites, collide_sprites

        