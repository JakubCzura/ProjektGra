import pygame

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"images/{image}.png")
 
    def Draw(self, screen):      
        screen.blit(self.image, (self.x, self.y))



