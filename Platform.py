import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, width, height, rectX, rectY):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = rectX
        self.rect.y = rectY

    def Draw(self, surface):
        surface.blit(self.image, self.rect)
