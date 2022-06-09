import pygame, os
import game_module as gm
import Bullet
import Music
import Player

class Alien(pygame.sprite.Sprite):
    def __init__(self, image, player):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movementX = 0
        self.movementY = 0
        self.isLookingLeft = False
        self.isLookingDown = False
        #self.level = None
        self.speed = 2 #prêdkoœæ gracza
        self.player = player

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

    def TurnLeft(self):
        self.movementX = -self.speed
        self.isLookingLeft = True

   

    def Update(self):

        # ruch w poziomie
        self.rect.x += self.movementX

        # ruch w pionie
        self.rect.y += self.movementY

        # aniamcja
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
                        self.image = gm.KAPITAN_L
                    else:
                        self.image = gm.KAPITAN_R

            if self.movementY < 0:
                self.rect.top = p.rect.bottom

            self.movementY = 0


    def get_event(self):
     
        #K_UP                 
        #K_DOWN                
        #K_RIGHT               
        #K_LEFT   

        #keydown jeœli klawisz jest wciœniêty
        if self.player.event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.MoveRight()
            if event.key == pygame.K_LEFT:
                self.TurnLeft()
            if event.key == pygame.K_UP:
                self.MoveUp()
            if event.key == pygame.K_DOWN:
                self.MoveDown()
            if event.key == pygame.K_SPACE:
                self.shoot()

        #keyup jeœli klawisz siê zwalnia
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.MoveRight()
            if event.key == pygame.K_LEFT:
                self.TurnLeft()
            if event.key == pygame.K_UP:
                self.MoveUp()
            if event.key == pygame.K_DOWN:
                self.MoveDown()

    def _Move(self, image):
        self.image = image

