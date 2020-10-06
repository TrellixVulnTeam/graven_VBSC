import pygame
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        self.player = Player()
        # Groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        #     "touche_fleche_droite": True,
        #     "touche_fleche_gauche": False
        # }

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)