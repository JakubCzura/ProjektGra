import pygame, os
import game_module as gm

# og�lna klasa planszy
class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_platforms = pygame.sprite.Group()
        self.list_of_weapons = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()
        self.set_of_dzida_bullets = pygame.sprite.Group()
        self.world_shift = 0
        self.world_shift_y = 0


    def update(self):
        if self.player.rect.right >= 1000:
            diff = self.player.rect.right - 1000
            self.player.rect.right = 1000
            self._shift_world(-diff)
        if self.player.rect.left <= 350:
            diff = 350 - self.player.rect.left
            self.player.rect.left = 350
            self._shift_world(diff)
        if self.player.rect.top >= 550:
            diff = self.player.rect.top - 550
            self.player.rect.top = 550
            self._shift_world_y(-diff)
        if self.player.rect.bottom <= 200:
            diff = 200 - self.player.rect.bottom
            self.player.rect.bottom = 200
            self._shift_world_y(diff)

        self.set_of_bullets.update()
        self.set_of_dzida_bullets.update()

        pygame.sprite.groupcollide(self.set_of_bullets, self.set_of_platforms, True, False)
        for b in self.set_of_bullets:
            if b.rect.left > gm.WIDTH or b.rect.right < 0:
                b.kill()

        pygame.sprite.groupcollide(self.set_of_dzida_bullets, self.set_of_platforms, True, False)
        for d in self.set_of_dzida_bullets:
            if d.rect.left > gm.WIDTH or d.rect.right < 0:
                d.kill()

    def draw(self, surface):
        for p in self.set_of_platforms:
            p.draw(surface)

        self.list_of_weapons.draw(surface)
        self.set_of_bullets.draw(surface)
        self.set_of_dzida_bullets.draw(surface)

    def _shift_world(self, shift_x):
        self.world_shift += shift_x

        for p in self.set_of_platforms:
            p.rect.x += shift_x

        for i in self.list_of_weapons:
            i.rect.x += shift_x

        for b in self.set_of_bullets:
            b.rect.x += shift_x

        for d in self.set_of_dzida_bullets:
            d.rect.x += shift_x

    def _shift_world_y(self, shift_y):
        self.world_shift_y += shift_y
       
        for p in self.set_of_platforms:
            p.rect.y += shift_y
      
        for i in self.list_of_weapons:
            i.rect.y += shift_y
         