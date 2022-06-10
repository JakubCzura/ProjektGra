import pygame
import Resources

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
            self._Move(Resources.ALIEN_RIGHT)
        if self.movementX < 0:
            self._Move(Resources.ALIEN_LEFT)
        

        collidingPlatforms = pygame.sprite.spritecollide(self, self.level.platforms,False)
        for platform in collidingPlatforms:
            if self.movementX > 0:
                self.rect.right = platform.rect.left
            if self.movementX < 0:
                self.rect.left = platform.rect.right

        collidingPlatforms = pygame.sprite.spritecollide(self, self.level.platforms,False)
        for platform in collidingPlatforms:
            if self.movementY > 0:
                self.rect.bottom = platform.rect.top
                if self.movementX == 0:
                    if self.isLookingLeft:
                        self.image = Resources.ALIEN_LEFT
                    else:
                        self.image = Resources.ALIEN_RIGHT
            if self.movementY < 0:
                self.rect.top = platform.rect.bottom
            self.movementY = 0
   

    def _Move(self, image):
        self.image = image

    def SpawnAlien(self):               
        return Alien(self.image, self.player, self.rect.left, self.rect.bottom, self.level)

