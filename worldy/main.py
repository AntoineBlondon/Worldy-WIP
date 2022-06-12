from pygame.locals import *
from constants import *
from player import *
from worldObjects import *
from world import *
import pygame
import sys

 
pygame.init()

 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Worldy")




P1 = Player()

world = World()

world.world1()

all_sprites, collide_sprites = world.load(0,0)

all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0))
    P1.update(collide_sprites)

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    pygame.display.update()
    FramePerSec.tick(FPS)