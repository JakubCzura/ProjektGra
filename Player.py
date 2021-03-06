import pygame
import Resources
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
        self.level = None
        self.speed = 5 #predkosc gracza
        self.weapon = '' #uzywana bron

    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    def MoveUp(self):
        self.movementY = -self.speed

    def MoveDown(self):
        self.movementY = self.speed

    def MoveRight(self):
        self.movementX = self.speed
        self.isLookingLeft = False

    def MoveLeft(self):
        self.movementX = -self.speed
        self.isLookingLeft = True

    def Shoot(self):
        if self.weapon == 'dzida_laserowa':
            MusicDzida = Music.Music('strzał_z_dzidy.wav', 0)
            MusicDzida.PlayShoot()
            self.level.DzidaBullets.add(
                Bullet.Bullet(Resources.DZIDA_POCISK, self.isLookingLeft, self.rect.centerx, self.rect.centery - 10, 'dzida_laserowa'))
        if self.weapon == 'karabinek':
            MusicDzida = Music.Music('strzał_z_karabinu.wav', 0)
            MusicDzida.PlayShoot()
            self.level.KarabinekBullets.add(
                Bullet.Bullet(Resources.BULLET_LIST, self.isLookingLeft, self.rect.centerx , self.rect.centery - 10, 'karabinek'))
        

    def Update(self):
        # ruch w poziomie
        self.rect.x += self.movementX

        # aniamcja obrotu w lewo i prawo
        if self.movementX >= 0:
            self._Move(Resources.KAPITAN_RIGHT)
        else:
            self._Move(Resources.KAPITAN_LEFT)
        
        #kolizja z przeszkodami z boku
        collidingGroundList = pygame.sprite.spritecollide(self, self.level.groundList,False)
        for ground in collidingGroundList:
            if self.movementX > 0:
                self.rect.right = ground.rect.left
            if self.movementX < 0:
                self.rect.left = ground.rect.right

        # ruch w pionie
        self.rect.y += self.movementY

        #kolizja z przeszkodami z góry
        collidingGroundList = pygame.sprite.spritecollide(self, self.level.groundList,False)
        for ground in collidingGroundList:
            if self.movementY > 0:
                self.rect.bottom = ground.rect.top
                if self.movementX == 0:
                    if self.isLookingLeft:
                        self.image = Resources.KAPITAN_L
                    else:
                        self.image = Resources.KAPITAN_R
            if self.movementY < 0:
                self.rect.top = ground.rect.bottom
            self.movementY = 0


        # podniesienie broni
        weapons = pygame.sprite.spritecollide(self, self.level.ListOfWeapons, False)
        for weapon in weapons:
            if weapon.name == 'karabinek':
                self.weapon = 'karabinek'
            if weapon.name == 'dzida_laserowa':
                self.weapon = 'dzida_laserowa'

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
                self.Shoot()           

    def _Move(self, image):
        self.image = image

