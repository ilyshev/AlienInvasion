class Settings():
    ''' Game settings'''

    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 20
        #fleet_direction = 1 moving right, -1 moving left
        self.fleet_direction = 1