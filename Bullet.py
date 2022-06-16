import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, imageList, rotatedLeft, coordinateX, coordinateY, weapon):
        super().__init__()
        self.image = imageList[1] if rotatedLeft else imageList[0] #zdj�cie pocisku lecacego w lewo lub prawo
        self.rect = self.image.get_rect() #get_rect() zwraca obiekt z uzytego obrazka
        self.rect.center = [coordinateX, coordinateY] #wspolrzedne X i Y pocisku
        self.weapon = weapon
        self.movement_x = -10 if rotatedLeft else 10
        if weapon=='karabinek':
            self.movement_x = -20 if rotatedLeft else 20
        if weapon=='dzida_laserowa':
            self.movement_x = -30 if rotatedLeft else 30

    def update(self):
        self.rect.x += self.movement_x
