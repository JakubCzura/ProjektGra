import pygame, os
import GameModule as GM
import Player, Item, Level, Level1, Platform

class Level_1(Level):
    def __init__(self, player):
        super().__init__(player)
        self._create_pltforms()
        self._create_items()


    def _create_pltforms(self):
        platforms_cor = [[15*70, 70, 70, GM.HEIGHT - 70],
                         [4*70, 70, 200, 370],
                         [70, 70, 1000, 370]]

        for cor in platforms_cor:
            self.set_of_platforms.add(Platform(GM.GRASS_LIST, *cor))

    def _create_items(self):
        shotgun = Item(GM.SHOTGUN2, 'shotgun', 700, 620)
        self.set_of_items.add(shotgun)