import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1180
        self.rect.y = 537
        self.velocity = 2

    def forward(self):
        self.rect.x -= self.velocity