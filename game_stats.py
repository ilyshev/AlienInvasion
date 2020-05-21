class GameStats():
    '''Checking game statistic'''

    def __init__(self, ai_game):
        #Statistic inicializing
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit