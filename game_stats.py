class GameStats():
    '''Checking game statistic'''

    def __init__(self, ai_game):
        #Statistic inicializing
        self.settings = ai_game.settings
        self.reset_stats()

        #Game starts in active condition
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit