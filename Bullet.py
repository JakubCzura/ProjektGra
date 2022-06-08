import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_list, rotate_left,  pos_center_x, pos_center_y, weapon):
        super().__init__()
        self.image = image_list[1] if rotate_left else image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_center_x, pos_center_y]
        self.weapon = weapon
        self.movement_x = -10 if rotate_left else 10
        if weapon=='karabinek':
            self.movement_x = -20 if rotate_left else 20
        if weapon=='dzida_laserowa':
            self.movement_x = -30 if rotate_left else 30

    def update(self):
        self.rect.x += self.movement_x
