import pygame, os
import game_module as gm
import Bullet
import Music
import Player
import math

class Alien(pygame.sprite.Sprite):
    def __init__(self, image, player):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movementX = 0
        self.movementY = 0
        self.isLookingLeft = False
        self.isLookingDown = False
        self.speed = 1 #pr�dko�� kosmity
        self.player = player
        self.IsAlive = True
        

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

        # ruch w poziomie
        self.rect.x += self.movementX

        #aniamcja
        if self.movementX > 0:
            self._Move(gm.KAPITAN_RIGHT)
        if self.movementX < 0:
            self._Move(gm.KAPITAN_LEFT)
        

        #colliding_platfoms = pygame.sprite.spritecollide(
        #    self, self.level.platforms,False)
        #for p in colliding_platfoms:
        #    if self.movementX > 0:
        #        self.rect.right = p.rect.left
        #    if self.movementX < 0:
        #        self.rect.left = p.rect.right


        ## ruch w pionie
        #self.rect.y += self.movementY

        #colliding_platfoms = pygame.sprite.spritecollide(
        #    self, self.level.platforms,False)
        #for p in colliding_platfoms:
        #    if self.movementY > 0:
        #        self.rect.bottom = p.rect.top
        #        if self.movementX == 0:
        #            if self.isLookingLeft:
        #                self.image = gm.KAPITAN_L
        #            else:
        #                self.image = gm.KAPITAN_R

        #    if self.movementY < 0:
        #        self.rect.top = p.rect.bottom

        #    self.movementY = 0


    #def get_event(self, event):
     
    #    #K_UP                 
    #    #K_DOWN                
    #    #K_RIGHT               
    #    #K_LEFT   
        
    #    #keydown je�li klawisz jest wci�ni�ty
    #    if event.type == pygame.KEYDOWN:
    #        if event.key == pygame.K_RIGHT:
    #            self.MoveRight()
    #        if event.key == pygame.K_LEFT:
    #            self.TurnLeft()
    #        if event.key == pygame.K_UP:
    #            self.MoveUp()
    #        if event.key == pygame.K_DOWN:
    #            self.MoveDown()
    #        if event.key == pygame.K_SPACE:
    #            self.shoot()

    #    #keyup je�li klawisz si� zwalnia
    #    if event.type == pygame.KEYUP:
    #        if event.key == pygame.K_RIGHT:
    #            self.MoveRight()
    #        if event.key == pygame.K_LEFT:
    #            self.TurnLeft()
    #        if event.key == pygame.K_UP:
    #            self.MoveUp()
    #        if event.key == pygame.K_DOWN:
    #            self.MoveDown()
   

    def _Move(self, image):
        self.image = image

