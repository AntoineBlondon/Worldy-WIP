from pygame.locals import *
from constants import *
from player import *
from worldObjects import *
import pygame
import sys

 
pygame.init()

 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")



 
PT1 = object("wow")
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    displaysurface.fill((0,0,0))
    P1.move()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    pygame.display.update()
    FramePerSec.tick(FPS)