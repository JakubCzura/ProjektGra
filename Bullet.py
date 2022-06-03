import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_list, rotate_left,  pos_center_x, pos_center_y):
        super().__init__()
        self.image = image_list[1] if rotate_left else image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_center_x, pos_center_y]
        self.movement_x = -15 if rotate_left else 15

    def update(self):
        self.rect.x += self.movement_x
