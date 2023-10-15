# Anne Edwards, Miguel Mancera, Parker Nguyen

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 680
        self.pacmanspeed = 2
        self.rectsize = 15
        self.pacmansize = self.rectsize * 5

        self.game_active = False

        self.victory_fanfare = False