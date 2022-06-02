import pygame, os
import game_module as gm

# og�lna klasa planszy
class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_platforms = pygame.sprite.Group()
        self.set_of_items = pygame.sprite.Group()
        self.world_shift = 0
        self.world_shift_y = 0


    def update(self):
        if self.player.rect.right >= 900:
            diff = self.player.rect.right - 900
            self.player.rect.right = 900
            self._shift_world(-diff)
        if self.player.rect.left <= 450:
            diff = 450 - self.player.rect.left
            self.player.rect.left = 450
            self._shift_world(diff)
        if self.player.rect.top >= 550:
            diff = self.player.rect.top - 550
            self.player.rect.top = 550
            self._shift_world_y(-diff)
        if self.player.rect.bottom <= 200:
            diff = 200 - self.player.rect.bottom
            self.player.rect.bottom = 200
            self._shift_world_y(diff)

    def draw(self, surface):
        for p in self.set_of_platforms:
            p.draw(surface)

        self.set_of_items.draw(surface)

    def _shift_world(self, shift_x):
        self.world_shift += shift_x

        for p in self.set_of_platforms:
            p.rect.x += shift_x

        for i in self.set_of_items:
            i.rect.x += shift_x

    def _shift_world_y(self, shift_y):
        self.world_shift_y += shift_y
       
        for p in self.set_of_platforms:
            p.rect.y += shift_y
      
        for i in self.set_of_items:
            i.rect.y += shift_y
          