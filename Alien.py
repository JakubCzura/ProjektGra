import pygame
import Resources

class Alien(pygame.sprite.Sprite):
    def __init__(self, image, player, left, bottom, level, speed=2):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() #przeksztalca obrazek w klase
        self.movementX = 0
        self.movementY = 0
        self.isLookingLeft = False
        self.speed = speed #prędkość kosmity
        self.player = player
        self.rect.left = left
        self.rect.bottom = bottom
        self.level = level

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

    def Update(self):
        if self.player.rect.x < self.rect.x: #przyblizanie sie do gracza po osi X
            self.MoveLeft()
            self.rect.x -= self.speed
        else:
            self.MoveRight()
            self.rect.x += self.speed
        if self.player.rect.y < self.rect.y:  #przyblizanie sie do gracza po osi Y
            self.MoveDown()
            self.rect.y -= self.speed
        else:
            self.MoveUp()
            self.rect.y += self.speed

        #aniamcja kosmity
        if self.movementX >= 0:
            self._Move(Resources.ALIEN_RIGHT)
        else: 
            self._Move(Resources.ALIEN_LEFT)
        

        #kolizja z bocznymi krawędziami
        collidingGround = pygame.sprite.spritecollide(self, self.level.groundList,False)
        for ground in collidingGround:
            if self.movementX > 0:
                self.rect.right = ground.rect.left
            if self.movementX < 0:
                self.rect.left = ground.rect.right

        #kolizja z góry i dołu
        collidingGround = pygame.sprite.spritecollide(self, self.level.groundList,False)
        for ground in collidingGround:
            if self.movementY > 0:
                self.rect.bottom = ground.rect.top
                if self.movementX == 0:
                    if self.isLookingLeft:
                        self.image = Resources.ALIEN_LEFT
                    else:
                        self.image = Resources.ALIEN_RIGHT
            if self.movementY < 0:
                self.rect.top = ground.rect.bottom
            self.movementY = 0
   

    def _Move(self, image):
        self.image = image

    def SpawnAlien(self):               
        return Alien(self.image, self.player, self.rect.left, self.rect.bottom, self.level)

