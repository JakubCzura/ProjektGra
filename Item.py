import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, image, name, coordinateX, coordinateY):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name
        self.rect.center = [coordinateX, coordinateY] # pozycja X i Y przedmiotu