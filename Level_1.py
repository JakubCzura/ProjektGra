import pygame, os
import game_module as gm
import Level, Platform, Item


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