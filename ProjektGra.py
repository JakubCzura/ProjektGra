#import pygame, os
#import GameModule as gm
#import Player, Item, Level, Level1, Platform

#pygame.init()

## centrowanie okna
#os.environ["SDL_VIDEO_CENTERED"] = "1"

## tworzenie okna gry
#screen = pygame.display.set_mode(gm.SIZESCREEN)
#clock = pygame.time.Clock()


##konkretyzacja obiekt�w
#player = Player(gm.KAPITAN_R)
#player.rect.left = 150
#player.rect.bottom = gm.HEIGHT - 70
#current_level = Level_1(player)
#player.level = current_level


#window_open = True
##p�tla gry
#while window_open:
#    screen.fill(gm.LIGHTBLUE)
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            window_open = False
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_ESCAPE:
#                window_open = False
#        player.get_event(event)

#    # aktualziacja i rysowanie obiekt�w
#    player.update()
#    current_level.update()

#    player.draw(screen)
#    current_level.draw(screen)


#    #aktualizacja okna gry
#    pygame.display.flip()
#    clock.tick(30)

#pygame.quit()

import pygame, os
import game_module as gm

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()


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



class Pltform(pygame.sprite.Sprite):
    def __init__(self, image_list, width, height, pos_x, pos_y):
        super().__init__()
        self.image_list = image_list
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, surface):
        # self.image.fill(gm.DARKGREEN)
        # surface.blit(self.image, self.rect)

        if self.width == 70:
            surface.blit(self.image_list[0], self.rect)
        else:
            surface.blit(self.image_list[1], self.rect)
            for i in range(70, self.width-70, 70):
                surface.blit(self.image_list[2], [self.rect.x + i,
                                                  self.rect.y])
            surface.blit(self.image_list[3], [self.rect.x + self.width - 70,
                                              self.rect.y])


class Item(pygame.sprite.Sprite):
    def __init__(self, image, name, pos_center_x, pos_center_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name
        self.rect.center = [pos_center_x, pos_center_y]

# og�lna klasa planszy
class Level:
    def __init__(self, player):
        self.player = player
        self.set_of_platforms = pygame.sprite.Group()
        self.set_of_items = pygame.sprite.Group()
        self.world_shift = 0


    def update(self):
        if self.player.rect.right >= 500:
            diff = self.player.rect.right - 500
            self.player.rect.right = 500
            self._shift_world(-diff)
        if self.player.rect.left <= 150:
            diff = 150 - self.player.rect.left
            self.player.rect.left = 150
            self._shift_world(diff)


    def draw(self, surface):
        for p in self.set_of_platforms:
            p.draw(surface)

        self.set_of_items.draw(surface)

    def _shift_world(self, shift_x):
        self.world_shift += shift_x

        for p in self.set_of_platforms:
            p.rect.x += shift_x

        for i in self.set_of_items:
            i.rect.x += shift_x



class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        self._create_pltforms()
        self._create_items()


    def _create_pltforms(self):
        platforms_cor = [[15*70, 70, 70, gm.HEIGHT - 70],
                         [4*70, 70, 200, 370],
                         [70, 70, 1000, 370]]

        for cor in platforms_cor:
            self.set_of_platforms.add(Pltform(gm.GRASS_LIST, *cor))

    def _create_items(self):
        shotgun = Item(gm.SHOTGUN2, 'shotgun', 700, 620)
        self.set_of_items.add(shotgun)


#konkretyzacja obiekt�w
player = Player(gm.KAPITAN_R)
player.rect.left = 150
player.rect.bottom = gm.HEIGHT - 70
current_level = Level_1(player)
player.level = current_level


window_open = True
#p�tla gry
while window_open:
    screen.fill(gm.LIGHTBLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        player.get_event(event)

    # aktualziacja i rysowanie obiekt�w
    player.update()
    current_level.update()

    player.draw(screen)
    current_level.draw(screen)


    #aktualizacja okna gry
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

