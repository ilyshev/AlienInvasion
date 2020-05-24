import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''Ship control class'''
    def __init__(self, ai_game):
        '''Ship start position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        '''Ship image load'''
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        '''Ship start position - midbottom'''
        self.rect.midbottom = self.screen_rect.midbottom

        '''Saving ship center coordinate'''
        self.x = float(self.rect.x)

        '''Moving flag'''
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update ship position '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        '''Update rect attribute'''
        self.rect.x = self.x

    def bltime(self):
        '''Drawing ship in actual position'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)