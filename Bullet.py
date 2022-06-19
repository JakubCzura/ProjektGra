import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_list, isLeftRotated,  coordinateX, coordinateY, weapon):
        super().__init__()
        self.image = image_list[1] if isLeftRotated else image_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = [coordinateX, coordinateY] #ustawianie poczatkowego polozenia pocisku
        self.weapon = weapon
        self.movementX = -10 if isLeftRotated else 10
        if weapon=='karabinek':
            self.movementX = -20 if isLeftRotated else 20
        if weapon=='dzida_laserowa':
            self.movementX = -30 if isLeftRotated else 30

    def update(self):
        self.rect.x += self.movementX
