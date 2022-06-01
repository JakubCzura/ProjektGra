import pygame, os
import game_module as gm
import Player, Pltform

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()




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
            self.set_of_platforms.add(Pltform.Pltform(gm.GRASS_LIST, *cor))

    def _create_items(self):
        shotgun = Item(gm.SHOTGUN2, 'shotgun', 700, 620)
        self.set_of_items.add(shotgun)


#konkretyzacja obiekt�w
player = Player.Player(gm.KAPITAN_R)
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

