import pygame, os
import GameModule as GM
import Player, Item, Level, Level1, Platform

class Platform(pygame.sprite.Sprite):
    def __init__(self, image_list, width, height, pos_x, pos_y):
        super().__init__()
        self.image_list = image_list
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, surface):
        # self.image.fill(gm.DARKGREEN)
        # surface.blit(self.image, self.rect)

        if self.width == 70:
            surface.blit(self.image_list[0], self.rect)
        else:
            surface.blit(self.image_list[1], self.rect)
            for i in range(70, self.width-70, 70):
                surface.blit(self.image_list[2], [self.rect.x + i,
                                                  self.rect.y])
            surface.blit(self.image_list[3], [self.rect.x + self.width - 70,
                                              self.rect.y])