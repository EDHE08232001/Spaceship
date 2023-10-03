import pygame


class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        ##  We assign the screen to an attribute of Ship, so we can access it easily in all the methods in this class.
        self.screen = ai_game.screen

        self.settings = ai_game.settings

        ## We access the screen's rect attribute using the get_rect() method and assign it to [self.screen_rect]. Doing so allows us to place the ship in the correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        ## Load the ship image and get its rect.
        ## Using pygame.image.load() to load images and giving it the location of our ship image ('images/ship.bmp'). This function returns a surface representing the ship, which assign to self.image.
        self.image = pygame.image.load('images/ship.bmp')
        ## When the image is loaded, we call get_rect() to access the ship surface's rect attribute so we can later use it to place the ship.
        self.rect = self.image.get_rect()

        ## Start each new ship at the bottom centre of the screen.
        ## To do so, make the value of self.rect.midbottom match the midbottom attribute of the screen's rect.
        self.rect.midbottom = self.screen_rect.midbottom

        ## Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        ## Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        ## Update the ship's x value, not the rect
        ## The code self.rect.right returns the x-coordinate of the right edge of the ship's rect. If this value is less than the value returned by self.screen_rect.right, the ship hasn't reached the right edge of the screen. The same goes for the block of the code that detects whther the left edge of ship rect reaches the left edge of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        ## update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
