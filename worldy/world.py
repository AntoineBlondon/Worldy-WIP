import pygame
from tile import *


class World():
    def __init__(self):
        self.map = []

    def world1(self):
        self.map = world
    
    def load(self,x,y):
        all_sprites = pygame.sprite.Group()
        collide_sprites = pygame.sprite.Group()

        
        file1 = open('levels/world1.txt', 'r')
        Lines = file1.readlines()
  
        level = []

        count = 0
        a = False
        ycount = 0

        for line in Lines:
            count += 1
            if line.startswith("."):
                if int(line[1:].split(',')[0]) == x and int(line[1:].split(',')[1]) == y:
                    a = True
                else:
                    a = False
            if a and not line.startswith("."):
                ycount += 1

                theLine = line.split(",")
                if theLine[-1].endswith("\n"): theLine[-1] = theLine[-1].strip()
                level.append(theLine)
            
        file1.close()
            
        for yd, line in enumerate(level):
            for xd, name in enumerate(line):
                tile = Tile(name,xd,yd)
                all_sprites.add(tile)
                if tile.isCollidable(): collide_sprites.add(tile)
        return all_sprites, collide_sprites

    def getLine(self,nline,x,y):
        

        count = 0
        a = False
        ycount = -1

        dotExists = False

        while self.nbLine(x,y) < 17:
            self.addLine(x,y,self.nbLine(x,y)-1,"air,air,air,air,air,air,air,air,air,air,air,air,air,air,air,air,air")

        file1 = open('levels/world1.txt', 'r')
        Lines = file1.readlines()
        for line in Lines:
            count += 1
            if line.startswith("."):
                
                if int(line[1:].split(',')[0]) == x and int(line[1:].split(',')[1]) == y:
                    dotExists = True
                    a = True
                else:
                    a = False
            if a and not line.startswith("."):
                
                ycount += 1
                
                if ycount == nline:
                    file1.close()
                    return line
        file1.close()
        if not dotExists:
            file1 = open('levels/world1.txt', 'a')
            file1.write(f".{x},{y}")
            file1.close()
            return self.getLine(nline,x,y)

        

        
                
            
        

    def set(self,x,y,xd,yd,name):
        file1 = open('levels/world1.txt', 'r')
        Lines = file1.readlines()

        count = 0
        a = False
        ycount = -1

        theLine = self.getLine(yd,x,y).split(',')
        realLine = ""
        theLine[xd] = name
        for i,c in enumerate(theLine):
            theLine[i] = theLine[i].strip()
        
        for i,c in enumerate(str(theLine)):
            if not c in ['[',']','\'',' ']:
                realLine += c
        fileLines = """"""

        for line in Lines:
            count += 1
            if line.startswith("."):
                if int(line[1:].split(',')[0]) == x and int(line[1:].split(',')[1]) == y:
                    a = True
                else:
                    a = False
            if a and not line.startswith("."):
                ycount += 1

                if ycount == yd:
                    fileLines += realLine +"\n"
                else:
                    fileLines += line
            else:
                fileLines += line
        file1.close()
        file1 = open('levels/world1.txt','w')
        file1.write(fileLines)
        file1.close()


    def addLine(self,x,y,yd,newLine):
        file1 = open('levels/world1.txt', 'r')
        Lines = file1.readlines()

        count = 0
        a = False
        ycount = -1
        
        fileLines = """"""

        for line in Lines:
            count += 1
            if line.startswith("."):
                if int(line[1:].split(',')[0]) == x and int(line[1:].split(',')[1]) == y:
                    a = True
                else:
                    a = False
            if a and not line.startswith("."):
                ycount += 1

                if ycount == yd:
                    fileLines += newLine +"\n"    
                fileLines += line
            else:
                fileLines += line
        file1.close()
        file1 = open('levels/world1.txt','w')
        file1.write(fileLines)
        file1.close()
    
    def nbLine(self,x,y):
        file1 = open('levels/world1.txt', 'r')
        Lines = file1.readlines()

        count = 0
        a = False
        ycount = -1

        for line in Lines:
            count += 1
            if line.startswith("."):
                
                if int(line[1:].split(',')[0]) == x and int(line[1:].split(',')[1]) == y:
                    a = True
                else:
                    a = False
            if a and not line.startswith("."):
                
                ycount += 1
        file1.close()
        return ycount+1