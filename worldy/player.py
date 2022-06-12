import pygame
from pygame.locals import *
from constants import *
 

class Player(pygame.sprite.Sprite):
    def __init__(self,world,x,y):
        super().__init__() 
        self.surf = pygame.Surface((32, 32))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center=(WIDTH/2,HEIGHT/2))
        self.hitbox = self.rect.inflate(0,-2)

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.currentx, self.currenty = x,y
        self.world = world


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_d]:
            theInput = input("Action ?\n")

            theInput = theInput.split(".")
            if theInput[0] == "set":
                x,y,name = int(theInput[1]), int(theInput[2]),str(theInput[3])


                self.world.set(self.currentx,self.currenty,x,y,name)



    def move(self,speed,collide_sprites):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal',collide_sprites)
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical',collide_sprites)
        self.rect.center = self.hitbox.center
        

    def collision(self,direction,collide_sprites):
        if direction == 'horizontal':
            for sprite in collide_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in collide_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self,collide_sprites):
        self.input()
        self.move(self.speed, collide_sprites)