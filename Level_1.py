import pygame, os
import game_module as gm
import Level, Platform, Item


class Level_1(Level.Level):
    def __init__(self, player):
        super().__init__(player)
        self._create_platforms()
        self._create_items()


    def _create_platforms(self):
        platforms_cor = [[1000*70, 70, 70, gm.HEIGHT - 70],
                         [1000*70, 70, 200, gm.HEIGHT-740],
                         [70, 70, 1000, 370],
                         ]
        
        #platforms_cor = []
        for cor in platforms_cor:
            self.set_of_platforms.add(Platform.Platform(gm.BORDER_LIST, *cor))

    def _create_items(self):
        shotgun = Item.Item(gm.SHOTGUN2, 'shotgun', 700, 620)
        shotgun2 = Item.Item(gm.SHOTGUN2, 'shotgun', 750, 620)
        coin = Item.Item(gm.COIN, 'coin', 850, 520)
        dzida_laserowa = Item.Item(gm.LASEROWA_DZIDA, 'dzida_laserowa', 350, 520)
        self.set_of_items.add(shotgun, shotgun2, coin, dzida_laserowa)
        