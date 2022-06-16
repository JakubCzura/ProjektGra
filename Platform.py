import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, width, height, coordinateX, coordinateY):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.rect = self.image.get_rect() #przetwarza zdjecie na obiekt
        self.rect.x = coordinateX
        self.rect.y = coordinateY

    def Draw(self, surface):
        surface.blit(self.image, self.rect)
