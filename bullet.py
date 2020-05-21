import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    ''' Bullets control class'''
    def __init__(self, ai_game):
        #Create object of bullets in same position as the ship
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create the position of Bullet (0,0) and position it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Saving position in float format
        self.y = float(self.rect.y)

    def update(self):
        #Update bullet position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        #Show the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
