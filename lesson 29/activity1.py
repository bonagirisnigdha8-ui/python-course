#Import Nessessary Libraries
import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))

#Create a loop to run till game is quit by user
done = False
while not done:

# Clear the event queue
 for event in pygame.event.get():
    if event. type == pygame.QUIT:
        pygame.quit()

        # Make the changes visible
        pygame.display.flip()