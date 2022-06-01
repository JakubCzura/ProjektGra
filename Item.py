import pygame, os
import game_module as gm


class Item(pygame.sprite.Sprite):
    def __init__(self, image, name, pos_center_x, pos_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name
        self.rect.center = [pos_center_x, pos_center_y]