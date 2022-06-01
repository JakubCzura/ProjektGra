import pygame, os
import game_module as gm
import Player, Platform, Item, Level

pygame.init()

# centrowanie okna
os.environ["SDL_VIDEO_CENTERED"] = "1"

# tworzenie okna gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()



class Level_1(Level.Level):
    def __init__(self, player):
        super().__init__(player)
        self._create_platforms()
        self._create_items()


    def _create_platforms(self):
        platforms_cor = [[15*70, 70, 70, gm.HEIGHT - 70],
                         [4*70, 70, 200, 370],
                         [70, 70, 1000, 370]]

        for cor in platforms_cor:
            self.set_of_platforms.add(Platform.Platform(gm.GRASS_LIST, *cor))

    def _create_items(self):
        shotgun = Item.Item(gm.SHOTGUN2, 'shotgun', 700, 620)
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

