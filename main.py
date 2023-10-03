## sys module has the function to exit a game when a player quits
import sys

## pygame module contains everything we need to make a game
import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

print("Press 'q' to quit the game")
print("Right arrow key to go right")
print("Left arrow key to go left")
print("Space to shoot")


class AlienInvasion:
    """overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        ## pygame.init() function initializes the background settings that Pygame needs to work properly.
        pygame.init()

        ## set an attribute, and make it an instance of the Settings class. This make our easier if we need to change the values of certain attributes because we can just set the new values in the settings.py module
        self.settings = Settings()

        ## Display Window
        """To create a display window"""
        ## The object we assign to self.screen is called a SURFACE. A surface in Pygame is a part of screen where a game element can be displayed.
        ## The surface returned by display.set_mode() represents the entire game window.
        ## When we activate the game's animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes triggered by user input.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        ## The self argument here refers to the current instance of AlienInvasion. This is the parameter that gives Ship access to the game's resources, such as screen object. We assign this Ship to self.ship.
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        """A list of bullets"""
        ## Create a group in AlienInvasion to store all the live bullets so we can manage the bullets that have already been fired. This group will be an instance of the pygame.sprite.Group() class, which behaves like a list with some extra functionality that is helpful when building games.

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            ## To call a method from within a class, use dot notation with the variable [self]
            self._check_events()

            self.ship.update()

            self._update_bullets()

            ## Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        ## This is an helper method. A helper method does work inside a class but it is not meant to be called through an instance. In Python, a single leading underscore indicates a hepler method.
        ## An event is an action that the user performs while playing the game.
        ## Use pygame.event.get() to access the events that Pygame detects. This function returns a list of events that have taken place since the last time this function was called. Any keyboard or mouse event will cause this for loop to run.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        ## Update bullet positions
        self.bullets.update()

        ## Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """update images on the screen, and flip to the new screen."""
        ## fill the screen with the customized during each loop with fill() method.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        ## Make the most recently drawn screen visible.
        ## In this case, it simply draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible. creating the illusion of smooth movement.
        pygame.display.flip()


if __name__ == '__main__':
    ## Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
