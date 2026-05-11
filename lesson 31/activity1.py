import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):


    def __init__(self, color, height, width):
    #Call to parent class (Sprite) constructor
        super().__init__()
        #Create the sprite's surface with dimentions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        #Set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

        #Method to update the sprite's position
        def update(self):
        #Move the sprite by its velocity
         self.rect.move_ip(self.velocity)
         #Flag to track if the sprite hits the boundary
         boundary_hit = False
         #Check for collision with left or right boundaries and reverse direction
         if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
            #Check for collision with top or bottom boundaries and reverse direction
         if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

            #if a boundary was hot, post events to change colors
            if boundary_hit:
               pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
               pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

               #Method to changethe sprite's color
               def change_color(self):
                  self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))


                  #Function to change the background color
                  def change_background_color():
                     global bg_color
                     bg