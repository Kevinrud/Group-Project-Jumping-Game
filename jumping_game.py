
import os
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Global Constants
# Set the width and height of the screen [width, height]
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

#Define the List of Dino images
RUNNING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
    ]
#Define the variables SCREEN and BG
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

pygame.display.set_caption("Jumping game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

X_POS = 80
Y_POS = 310
 #Use to get movement to right and left to Dino, also move the BG
def move_dino(y,x):
    #Code from background function
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    #finish Code from background function

    image = pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png"))
    SCREEN.fill(WHITE) #Om jag remove these code the bg will be black
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))

    #code from background function
    SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        print(f"{x_pos_bg}")
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed
    #finish Code from background function
    SCREEN.blit(image, (x, y))


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    #print("Keydown")
    game_speed = 0.5 #move the BG with diff. velocity
    x_pos_bg = 0 #
    y_pos_bg = 380
    X_POS = 80
    Y_POS = 310

    #global variables
    run_img = RUNNING

    image = run_img[0]
    dino_rect = image.get_rect()
    dino_rect.x = X_POS
    dino_rect.y = Y_POS


    #new bacground image with Dino
    SCREEN.fill(WHITE) #Om jag remove these code the bg will be black
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
    SCREEN.blit(image, (dino_rect.x, dino_rect.y)) #Den här visar dino runner1 image

    pygame.display.flip() # show the new data om the screen
    # Now ska göra att Dino will move to the right and to the left
    x =  (SCREEN_WIDTH * 0.07 )
    y = (SCREEN_HEIGHT* 0.51 )
    x_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2
                elif event.key == pygame.K_RIGHT:
                    x_change = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    ######################

        x += x_change
        #Funcktion för att röra Dino litte
        move_dino(y,x)
        pygame.display.update()




if __name__=='__main__':

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Load and set up graphics.
        background_image = pygame.image.load(os.path.join("assets/Other", "Chrome Dino.gif"))
        #Eugenio add another background and change the size
        background_image = pygame.transform.scale(background_image, (1200, 800))

        #Eugenio add anotehr background
        # Set positions of graphics
        background_position = [0, 0]

        BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))
        # Copy image to screen:
        SCREEN.blit(background_image, background_position)

        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(30)

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    #print("Eug code run here")
                    main()


        # Close the window and quit.
        pygame.quit()
