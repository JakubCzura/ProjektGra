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

    #def Draw(self, surface):

    #    if self.width == 70:
    #        surface.blit(self.image_list[0], self.rect)
    #    else:
    #        surface.blit(self.image_list[1], self.rect)
    #        for i in range(70, self.width-70, 70):
    #            surface.blit(self.image_list[2], [self.rect.x + i,
    #                                              self.rect.y])
    #        surface.blit(self.image_list[3], [self.rect.x + self.width - 70,
    #                                          self.rect.y])

    def Draw(self, surface):
        surface.blit(self.image, self.rect)
