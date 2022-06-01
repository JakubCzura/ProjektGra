import pygame, os
import GameModule as gm
import Player, Item, Level, Level1, Platform

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.movement_y = 0
        self.rotate_left = False
        self.press_right = False
        self.press_left = False
        self._count = 0
        self.level = None
        self.eq = {}

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = 6
        self.rotate_left = False

    def turn_left(self):
        self.movement_x = -6
        self.rotate_left = True

    def stop_x(self):
        self.movement_x = 0

    def stop_y(self):
        self.movement_y = 0

    def jump(self):
        self.rect.y += 2
        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        self.rect.y -= 2
        if colliding_platfoms:
            self.movement_y = -15

    def update(self):
        # grawitacja
        self._gravitation()


        # ruch w poziomie
        self.rect.x += self.movement_x


        # aniamcja
        if self.movement_x > 0:
            self._move(gm.PLAYER_WALK_LIST_R)
        if self.movement_x < 0:
            self._move(gm.PLAYER_WALK_LIST_L)

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right


        # ruch w pionie
        self.rect.y += self.movement_y

        colliding_platfoms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms,False)
        for p in colliding_platfoms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.movement_x == 0:
                    if self.rotate_left:
                        self.image = gm.KAPITAN_L
                    else:
                        self.image = gm.KAPITAN_R

            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0

        # zmiana grafiki gdy gracz skaka i spada
        if self.movement_y > 0:
            if self.rotate_left:
                self.image = gm.KAPITAN_L
            else:
                self.image = gm.KAPITAN_R

        if self.movement_y < 0:
            if self.rotate_left:
                self.image = gm.KAPITAN_L
            else:
                self.image = gm.KAPITAN_R


        # kolizja z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)

        for item in colliding_items:
            if item.name == 'shotgun':
                self.eq[item.name] = 1
                item.kill()

        print(self.eq)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.press_right = True
                self.turn_right()
            if event.key == pygame.K_LEFT:
                self.press_left = True
                self.turn_left()
            if event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if self.press_left:
                    self.turn_left()
                else:
                    self.stop_x()
                    self.image = gm.KAPITAN_R
                self.press_right = False
            if event.key == pygame.K_LEFT:
                if self.press_right:
                    self.turn_right()
                else:
                    self.stop_x()
                    self.image = gm.KAPITAN_L
                self.press_left = False


    def _move(self, image_list):
        self.image = image_list[self._count//4]

        self._count = (self._count + 1) % 32

    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 2
        else:
            self.movement_y += 0.35