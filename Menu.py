import pygame

#klasa menu do wyswietlania obrazkow

class Menu():
    def __init__(self, coordinateX, coordinateY, image):
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self.image = pygame.image.load(f"images/{image}.png")
 
    def Draw(self, screen):      
        screen.blit(self.image, (self.coordinateX, self.coordinateY))



