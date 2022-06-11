import pygame
from pygame.locals import *
from constants import *
 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2+30))
        self.pos = vec((WIDTH/2, HEIGHT/2))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC        
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_DOWN]:
            self.acc.y = ACC
        if pressed_keys[K_UP]:
            self.acc.y = -ACC
        
        
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc         
        if self.pos.x > WIDTH-15:
            self.pos.x = WIDTH-15
        if self.pos.x < 15:
            self.pos.x = 15
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 30:
            self.pos.y = 30
            
        self.rect.midbottom = self.pos
    def collide(self, sprites):
        hits = pygame.sprite.spritecollide(self , sprites, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
 