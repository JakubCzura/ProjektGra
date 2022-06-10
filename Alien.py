import pygame, os
import GameModule as gm
import Bullet
import Music
import Player
import math

class Alien(pygame.sprite.Sprite):
    def __init__(self, image, player, left, bottom, level):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movementX = 0
        self.movementY = 0
        self.isLookingLeft = False
        self.isLookingDown = False
        self.speed = 1 #prędkość kosmity
        self.player = player
        self.rect.left = left
        self.rect.bottom = bottom
        self.level = level

    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    def MoveUp(self):
        self.movementY = -self.speed
        self.isLookingDown = False

    def MoveDown(self):
        self.movementY = self.speed
        self.isLookingDown = True

    def MoveRight(self):
        self.movementX = self.speed
        self.isLookingLeft = False

    def MoveLeft(self):
        self.movementX = -self.speed
        self.isLookingLeft = True

    def Update(self):
        if self.player.rect.x < self.rect.x:
            self.MoveLeft()
            self.rect.x -= 1
        else:
            self.MoveRight()
            self.rect.x += 1
        if self.player.rect.y < self.rect.y:
            self.MoveDown()
            self.rect.y -= 1
        else:
            self.MoveUp()
            self.rect.y += 1

        #aniamcja
        if self.movementX > 0:
            self._Move(gm.ALIEN_RIGHT)
        if self.movementX < 0:
            self._Move(gm.ALIEN_LEFT)
        

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.platforms,False)
        for p in colliding_platfoms:
            if self.movementX > 0:
                self.rect.right = p.rect.left
            if self.movementX < 0:
                self.rect.left = p.rect.right

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.platforms,False)
        for p in colliding_platfoms:
            if self.movementY > 0:
                self.rect.bottom = p.rect.top
                if self.movementX == 0:
                    if self.isLookingLeft:
                        self.image = gm.ALIEN_LEFT
                    else:
                        self.image = gm.ALIEN_RIGHT
            if self.movementY < 0:
                self.rect.top = p.rect.bottom
            self.movementY = 0
   

    def _Move(self, image):
        self.image = image

    def SpawnAlien(self):               
        return Alien(self.image, self.player, self.rect.left, self.rect.bottom, self.level)

