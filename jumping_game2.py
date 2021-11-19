import os
import pygame

pygame.init()

# Set the size of the game window
window = pygame.display.set_mode((1100, 600))      # set_mode((Tuple))

# Load and scale the background image
bg_img = pygame.image.load('2d_background.jpg')
bg = pygame.transform.scale(bg_img, (1100, 600))

# Set the name of the game window
pygame.display.set_caption("Jump Game")

# Global Variables
x = 250
y = 395

jump = False
width = 1100
black = (0, 0, 0)


class Character:
    JUMP_VEL = 1.5
    X_POS = 80
    Y_POS = 450
    image=None
    jumpCount = 10
    def __init__(self, x, y, velx, vely, jump):
        # Walk
        self.x = x
        self.y = y
        self.vel_x = velx
        self.vel_y = vely
        self.jump = jump
        self.jump_vel = self.JUMP_VEL


        self.image = pygame.image.load(os.path.join("", "R1.png"))
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.X_POS
        self.image_rect.y = self.Y_POS
        self.jumpCount = self.jumpCount

    def move_char(self, userInput):
        # Moving left, right and jumping
        if userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel_x
        if userInput[pygame.K_RIGHT] and self.x < 1050:
            self.x += self.vel_x

        # When player presses K_UP set jump to True
        #if not self.jump and userInput[pygame.K_SPACE]:
        if not self.jump and userInput[pygame.K_UP]:
            self.jump = True

        # When jump is True
        if self.jump:
            self.make_a_jump(self.jump)
        # Eugenio Jag addet then här code to allow the rectangle to jump and move
        # Allows the player to "fly"
        if userInput[pygame.K_UP] and self.y > 0:
            self.y -= self.vel_y
        if userInput[pygame.K_DOWN] and self.y < 400: # Eugenio Change from 400 to 455
            self.y += self.vel_y

    # Eugenio added code här to Drawing the game
    def draw_char(self):
        # Eugenio Change the bg rectangle med image R1.png
        window.blit(self.image, (self.image_rect.x, self.image_rect.y))
        # The player's character for now is just a black rectangle. rect(window, color, (x, y, width, height))
        #pygame.draw.rect(window, black, (self.x, self.y, 50, 100))


    def make_a_jump(self,jump):

         self.image = self.image
         if self.jump:
             self.image_rect.y -= self.jump_vel
             self.jump_vel -= 0.01
         if self.jump_vel < -self.JUMP_VEL:
             print("test")
             self.image_jump = False
             #self.image_vel = self.JUMP_VEL
             self.image_vel =10


        # self.jumpCount = 10
        # if self.jumpCount >= -10:
        #     neg = 1
        #     if self.jumpCount < 0:
        #         neg = -1
        #     self.y -= (self.jumpCount ** 2) * 0.5 * neg
        #     self.jumpCount -= 1
        # else:
        #     self.isJump = False
        #     self.jumpCount = 10


def draw_game():
    global i

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


    # Eugenio add these code  to call the draw_game function
    #player.make_a_jump()
    player.draw_char()
    pygame.display.update()
    pygame.time.delay(2)


i = 0
player = Character(250, 395, 10, 10, False)

# The application start here
def main():

    # Main Loop
    # While run is True the game will run
    run = True
    while run:

        # pygame.QUIT = the red x button will close the window because run will be False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Allow the player to control the character
        userInput = pygame.key.get_pressed()

        # Movement
        player.move_char(userInput)

        # Draw game in window
        draw_game()


if __name__ == '__main__':
    main()