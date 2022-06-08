import pygame, os
import game_module as gm
import Bullet
import Music

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.rotate_left = False
        self.rotate_down = False
        self._count = 0
        self.level = None
        self.speed = 4 #prędkość gracza
        self.weapon = '' #używana broń

    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    def MoveUp(self):
        self.movement_y = -self.speed
        self.rotate_down = False

    def MoveDown(self):
        self.movement_y = self.speed
        self.rotate_down = True

    def MoveRight(self):
        self.movement_x = self.speed
        self.rotate_left = False

    def TurnLeft(self):
        self.movement_x = -self.speed
        self.rotate_left = True

    #def Stop_x(self):
    #    self.movement_x = 0

    #def Stop_y(self):
    #    self.movement_y = 0

    def shoot(self):
        if self.weapon == 'dzida_laserowa':
            MusicDzida = Music.Music('strzał_z_dzidy.wav', 0)
            MusicDzida.PlayShoot()
            self.level.set_of_bullets.add(
                Bullet.Bullet(gm.DZIDA_POCISK, self.rotate_left, self.rect.centerx, self.rect.centery-10, 'dzida_laserowa'))
        if self.weapon == 'karabinek':
            MusicDzida = Music.Music('strzał_z_karabinu.wav', 0)
            MusicDzida.PlayShoot()
            self.level.set_of_bullets.add(
                Bullet.Bullet(gm.BULLET_LIST, self.rotate_left, self.rect.centerx , self.rect.centery -10, 'karabinek'))
        

    def Update(self):

        # ruch w poziomie
        self.rect.x += self.movement_x

        # aniamcja
        if self.movement_x > 0:
            self._Move(gm.KAPITAN_RIGHT)
        if self.movement_x < 0:
            self._Move(gm.KAPITAN_LEFT)
        

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right


        # ruch w pionie
        self.rect.y += self.movement_y

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.movement_x == 0:
                    if self.rotate_left:
                        self.image = gm.KAPITAN_L
                    else:
                        self.image = gm.KAPITAN_R

            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0


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
                self.TurnLeft()
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
                self.TurnLeft()
            if event.key == pygame.K_UP:
                self.MoveUp()
            if event.key == pygame.K_DOWN:
                self.MoveDown()
            

    def _Move(self, image):
        self.image = image

