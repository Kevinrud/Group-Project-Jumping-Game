import pygame

pygame.init()

# Set the size of the game window
window = pygame.display.set_mode((1100, 600))      # set_mode((Tuple))

# Load and scale the background image
bg_img = pygame.image.load('2d_background.jpg')
bg = pygame.transform.scale(bg_img, (1100, 600))

# Set the name of the game window
pygame.display.set_caption("Jump Game")

#Global Variables
x = 250
y = 395

radius = 15
vel_x = 10
vel_y = 10
jump = False
width = 1100
black = (0, 0, 0)


class Character:
    def __init__(self, x, y, velx, vely, jump):
        # Walk
        self.x = x
        self.y = y
        self.vel_x = velx
        self.vel_y = vely
        self.jump = jump

    def move_char(self, userInput):
        # Moving left, right and jumping
        if userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= vel_x
        if userInput[pygame.K_RIGHT] and self.x < 1050:
            self.x += vel_x
        # When player presses space bar set jump to True
        if not self.jump and userInput[pygame.K_SPACE]:
            self.jump = True
        # When jump is True
        if self.jump:
            self.y -= self.vel_y*4
            self.vel_y -= 1
            if self.vel_y < -10:
                self.jump = False
                self.vel_y = 10

        #Eugenio Jag addet then här code to allow the rectangle to jump and move
        # Allows the player to "fly"
        if userInput[pygame.K_UP] and self.y > 0:
            self.y -= self.vel_y
        if userInput[pygame.K_DOWN] and self.y < 455: #Eugenio Change from 400 to 455
            self.y += self.vel_y

        # Eugenio added code här to Drawing the game
    def draw_game(self):
        #window.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        # The player's character for now is just a black rectangle. rect(window, color, (x, y, width, height))
        pygame.draw.rect(window, black, (self.x, self.y, 50, 100))


# The application start here
def main():
    i = 0
    player = Character(250, 395, 10, 10, False)

    # Main Loop
    # While run is True the game will run
    run = True
    while run:

        # pygame.QUIT = the red x button will close the window because run will be False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Create a black canvas behind the background picture
        window.fill(black)
        # The first background picture
        window.blit(bg, (i, 0))
        # Repeat the first background picture in a "slideshow"
        window.blit(bg, (width + i, 0))
        # Loop the background pic infinitely
        if i == -width:
            window.blit(bg, (width + i, 0))
            i = 0
        i -= 1

        #Eugenio Change the bg rectangle med image R1.png
        # The player's character for now is just a black rectangle. rect(window, color, (x, y, width, height))
        # Allow the player to control the character
        userInput = pygame.key.get_pressed()
        #Eugenio add these code  to call the draw_game function
        player.draw_game()
        player.move_char(userInput)
        pygame.time.delay(5)
        pygame.display.update()
if __name__=='__main__':
    main()