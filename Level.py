import pygame
import Resources

# ogolna klasa poziomu
class Level:
    def __init__(self, player):
        self.player = player
        self.groundList = pygame.sprite.Group() #zbior wszystkich kafelkow na mapie
        self.ListOfWeapons = pygame.sprite.Group()
        self.KarabinekBullets = pygame.sprite.Group()
        self.DzidaBullets = pygame.sprite.Group()
        self.worldCoordinateX = 0 #wspolrzedna osi X do przesuwania swiata
        self.worldCoordinateY = 0 #wspolrzedna osi Y do przesuwania swiata

    def Update(self):
        if self.player.rect.right >= 1300:
            distanceDifference = self.player.rect.right - 1300
            self.player.rect.right = 1300
            self._MoveWorld(-distanceDifference)
        if self.player.rect.left <= 350:
            distanceDifference = 350 - self.player.rect.left
            self.player.rect.left = 350
            self._MoveWorld(distanceDifference)
        if self.player.rect.top >= 650:
            distanceDifference = self.player.rect.top - 650
            self.player.rect.top = 650
            self._MoveWorldY(-distanceDifference)
        if self.player.rect.bottom <= 300:
            distanceDifference = 300 - self.player.rect.bottom
            self.player.rect.bottom = 300
            self._MoveWorldY(distanceDifference)

        self.KarabinekBullets.update()
        self.DzidaBullets.update()

        pygame.sprite.groupcollide(self.KarabinekBullets, self.groundList, True, False)
        for karabinekBullet in self.KarabinekBullets:
            if karabinekBullet.rect.left > Resources.width or karabinekBullet.rect.right < 0:
                karabinekBullet.kill()

        pygame.sprite.groupcollide(self.DzidaBullets, self.groundList, True, False)
        for dzidaBullet in self.DzidaBullets:
            if dzidaBullet.rect.left > Resources.width or dzidaBullet.rect.right < 0:
                dzidaBullet.kill()

    def Draw(self, surface):
        for ground in self.groundList:
            ground.Draw(surface)

        self.ListOfWeapons.draw(surface)
        self.KarabinekBullets.draw(surface)
        self.DzidaBullets.draw(surface)

    def _MoveWorld(self, coordinateX):
        self.worldCoordinateX += coordinateX

        for ground in self.groundList:
            ground.rect.x += coordinateX

        for weapon in self.ListOfWeapons:
            weapon.rect.x += coordinateX

        for karabinekBullet in self.KarabinekBullets:
            karabinekBullet.rect.x += coordinateX

        for dzidaBullet in self.DzidaBullets:
            dzidaBullet.rect.x += coordinateX

    def _MoveWorldY(self, coordinateY):
        self.worldCoordinateY += coordinateY
       
        for ground in self.groundList:
            ground.rect.y += coordinateY
      
        for weapon in self.ListOfWeapons:
            weapon.rect.y += coordinateY
         