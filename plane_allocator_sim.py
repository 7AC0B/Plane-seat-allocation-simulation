import pygame, sys, os

path = "/Users/JacobThomsen/Documents/GitHub/plane_seat_allocator"
os.chdir(path)    # Set directory
os.getcwd()


###################### SETUP ######################

screen_width = 200    
screen_height = 800 
screen = pygame.display.set_mode((screen_width,screen_height))    # Specifies size of display

sim_active = True

screen = pygame.display.set_mode((screen_width,screen_height))    # Specifies size of display
clock = pygame.time.Clock()     # Creates clock for frame rate options
fps = 60

######## LOAD IMAGES ########

plane_surface = pygame.image.load('art/plane.png').convert_alpha()
plane_surface = pygame.transform.smoothscale(plane_surface, (screen_width,screen_height))

# health_heart = pygame.image.load('jungle_art/heart.png').convert_alpha()
# health_heart = pygame.transform.smoothscale(health_heart, (59,59))

# game_over_surface = pygame.image.load('jungle_art/game_over_message.png').convert_alpha()
# game_over_surface = pygame.transform.smoothscale(game_over_surface, (int(screen_width/2),int(screen_height/4)))
# game_over_rect = game_over_surface.get_rect(center = (int(screen_width/2),int(screen_height/2)))



pygame.init()

while True:

    #### UPDATE BACKGROUND SURFACE #### 
    screen.blit(plane_surface, (0,0))

    #### EVENTS ####
    for event in pygame.event.get():

        if event.type == pygame.QUIT:     # Sets option to quit the game by clicking top left x to close window
            pygame.quit()
            sys.exit()      # Makes sure programme stops running when game is ended. 


    