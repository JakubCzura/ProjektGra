import pygame
import Resources

# ogolna klasa poziomu
class Level:
    def __init__(self, player):
        self.player = player
        self.platforms = pygame.sprite.Group()
        self.ListOfWeapons = pygame.sprite.Group()
        self.KarabinekBullets = pygame.sprite.Group()
        self.DzidaBullets = pygame.sprite.Group()
        self.worldShift = 0
        self.worldShiftY = 0

    def Update(self):
        if self.player.rect.right >= 1300:
            diff = self.player.rect.right - 1300
            self.player.rect.right = 1300
            self._MoveWorld(-diff)
        if self.player.rect.left <= 350:
            diff = 350 - self.player.rect.left
            self.player.rect.left = 350
            self._MoveWorld(diff)
        if self.player.rect.top >= 650:
            diff = self.player.rect.top - 650
            self.player.rect.top = 650
            self._MoveWorldY(-diff)
        if self.player.rect.bottom <= 300:
            diff = 300 - self.player.rect.bottom
            self.player.rect.bottom = 300
            self._MoveWorldY(diff)

        self.KarabinekBullets.update()
        self.DzidaBullets.update()

        pygame.sprite.groupcollide(self.KarabinekBullets, self.platforms, True, False)
        for karabinekBullet in self.KarabinekBullets:
            if karabinekBullet.rect.left > Resources.width or karabinekBullet.rect.right < 0:
                karabinekBullet.kill()

        pygame.sprite.groupcollide(self.DzidaBullets, self.platforms, True, False)
        for dzidaBullet in self.DzidaBullets:
            if dzidaBullet.rect.left > Resources.width or dzidaBullet.rect.right < 0:
                dzidaBullet.kill()

    def Draw(self, surface):
        for platform in self.platforms:
            platform.Draw(surface)

        self.ListOfWeapons.draw(surface)
        self.KarabinekBullets.draw(surface)
        self.DzidaBullets.draw(surface)

    def _MoveWorld(self, shiftX):
        self.worldShift += shiftX

        for platform in self.platforms:
            platform.rect.x += shiftX

        for weapon in self.ListOfWeapons:
            weapon.rect.x += shiftX

        for karabinekBullet in self.KarabinekBullets:
            karabinekBullet.rect.x += shiftX

        for dzidaBullet in self.DzidaBullets:
            dzidaBullet.rect.x += shiftX

    def _MoveWorldY(self, shiftY):
        self.worldShiftY += shiftY
       
        for platform in self.platforms:
            platform.rect.y += shiftY
      
        for weapon in self.ListOfWeapons:
            weapon.rect.y += shiftY
         