import pygame, os
import game_module as gm
import Bullet
import Music

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movementX = 0
        self.movementY = 0
        self.isLookingLeft = False
        self.isLookingDown = False
        self.level = None
        self.speed = 4 #predkosc gracza
        self.weapon = '' #uzywana bron
        self.isAlive = True

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

    def shoot(self):
        if self.weapon == 'dzida_laserowa':
            MusicDzida = Music.Music('strzał_z_dzidy.wav', 0)
            MusicDzida.PlayShoot()
            self.level.DzidaBullets.add(
                Bullet.Bullet(gm.DZIDA_POCISK, self.isLookingLeft, self.rect.centerx, self.rect.centery - 10, 'dzida_laserowa'))
        if self.weapon == 'karabinek':
            MusicDzida = Music.Music('strzał_z_karabinu.wav', 0)
            MusicDzida.PlayShoot()
            self.level.KarabinekBullets.add(
                Bullet.Bullet(gm.BULLET_LIST, self.isLookingLeft, self.rect.centerx , self.rect.centery - 10, 'karabinek'))
        

    def Update(self):

        # ruch w poziomie
        self.rect.x += self.movementX

        # aniamcja
        if self.movementX > 0:
            self._Move(gm.KAPITAN_RIGHT)
        if self.movementX < 0:
            self._Move(gm.KAPITAN_LEFT)
        

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.platforms,False)
        for p in colliding_platfoms:
            if self.movementX > 0:
                self.rect.right = p.rect.left
            if self.movementX < 0:
                self.rect.left = p.rect.right


        # ruch w pionie
        self.rect.y += self.movementY

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


        # kolizja z przedmiotami
        weapons = pygame.sprite.spritecollide(
            self, self.level.ListOfWeapons, False)

        for weapon in weapons:
            if weapon.name == 'karabinek':
                self.weapon = 'karabinek'
            if weapon.name == 'dzida_laserowa':
                self.weapon = 'dzida_laserowa'

        print(self.weapon)

    def get_event(self, event):
     
        #K_UP                 
        #K_DOWN                
        #K_RIGHT               
        #K_LEFT   
        
        #keydown jeśli klawisz jest wciśnięty
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.MoveRight()
            if event.key == pygame.K_LEFT:
                self.MoveLeft()
            if event.key == pygame.K_UP:
                self.MoveUp()
            if event.key == pygame.K_DOWN:
                self.MoveDown()
            if event.key == pygame.K_SPACE:
                self.shoot()

        #keyup jeśli klawisz się zwalnia
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.MoveRight()
            if event.key == pygame.K_LEFT:
                self.MoveLeft()
            if event.key == pygame.K_UP:
                self.MoveUp()
            if event.key == pygame.K_DOWN:
                self.MoveDown()
            

    def _Move(self, image):
        self.image = image

