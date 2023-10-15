# Anne Edwards, Miguel Mancera, Parker Nguyen
import pygame.font


class Button():

    def __init__(self, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        if (msg == "Ready!"):
            self.width, self.height = 100, 25
        else:
            self.width, self.height = 200, 50
        self.button_color = (0, 0, 0, 0)
        self.text_color = (255, 255, 255)
        if (msg == "Ready!"):
            self.font = pygame.font.SysFont(None, 25)
        else:
            self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = 360
        if(msg == "High Scores"):
            self.rect.y = 420
        if (msg == "Ready!"):
            self.rect.center = self.screen_rect.center
            self.rect.y += 35
            self.rect.x -= 80

        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)