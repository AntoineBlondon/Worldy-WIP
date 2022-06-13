import pygame

vec = pygame.math.Vector2  # 2 for two dimensional
HEIGHT = 32*17
WIDTH = 32*17
ACC = 0.5
FRIC = -0.12
FPS = 60


tiles = {"tree_leaf": ((112, 141, 19), True), 
         "path": ((130, 212, 53), False), 
         "air": ((0,0,0), False),
         "teleporter": ((255,255,255),False),}

world = [[[],[]],
         [[],[]],
         [[],[]],
         [[],[]]]