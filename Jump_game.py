import pygame
import os
import random
from pygame.locals import *

pygame.init()

# Set the size of the game window
window = pygame.display.set_mode((1100, 600))  # set_mode((Tuple))

# global var using in menu() function
RUNNING = [
    pygame.image.load(os.path.join("razz", "jump2.png")),
    pygame.image.load(os.path.join("razz", "walk1.png")),
]


# Loads and scales background and object pictures for the game
def pictures():
    """Loads and scales background and object pictures for the game"""
    global bg, jumping_scale, stone_scaled, mushroom_scaled
    # Load and scale the background image
    bg_img = pygame.image.load('pictures/2d_background.jpg')
    bg = pygame.transform.scale(bg_img, (1100, 600))
    # Load image of character running
    jumping = pygame.image.load(os.path.join("razz", "jump2.png"))
    jumping_scale = pygame.transform.scale(jumping, (100, 100))
    # Load image of stone and scale it
    the_stone = pygame.image.load('pictures/stone.png')
    stone_scaled = pygame.transform.scale(the_stone, (125, 125))
    # Load image of stone and scale it
    the_mushroom = pygame.image.load('pictures/mushroom.png')
    mushroom_scaled = pygame.transform.scale(the_mushroom, (125, 125))


pictures()


# Load image of character running
def char_img_scaling():
    """Loads and scales player's character"""
    walk1 = pygame.image.load(os.path.join("razz", "walk1.png"))
    walk1_scale = pygame.transform.scale(walk1, (100, 100))
    walk2 = pygame.image.load(os.path.join("razz", "walk2.png"))
    walk2_scale = pygame.transform.scale(walk2, (100, 100))
    walk3 = pygame.image.load(os.path.join("razz", "walk3.png"))
    walk3_scale = pygame.transform.scale(walk3, (100, 100))
    walk4 = pygame.image.load(os.path.join("razz", "walk4.png"))
    walk4_scale = pygame.transform.scale(walk4, (100, 100))
    return [walk1_scale, walk2_scale, walk3_scale, walk4_scale]


# Set the name of the game window
pygame.display.set_caption("Jump Game")

# Clock
clock = pygame.time.Clock()


# Player's character
class Character:
    """Class object for the player's character and all it's actions"""
    JUMP_VEL = 2
    x = 250
    y = 395

    def __init__(self, x, y, velx, vely, jump):
        # Walk
        self.x = x
        self.y = y
        self.vel_x = velx
        self.vel_y = vely

        self.face_right = True
        self.stepIndex = 0
        self.count = 0
        self.index = 0

        self.jump = jump
        self.jump_vel = self.JUMP_VEL

        self.image = jumping_scale
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    # Character Movement (Jumping
    def move_char(self, userInput):
        # When player presses space bar set jump to True
        if not self.jump and userInput[pygame.K_SPACE]:
            self.jump = True

        # When jump is True
        if self.jump:
            self.make_a_jump(self.jump)

    # Displaying the character on the window
    def draw_char(self):

        if self.stepIndex >= 4:
            self.stepIndex = 0
        self.count += 1

        if self.jump:
            window.blit(char_img_scaling()[self.stepIndex], (self.image_rect.x, self.image_rect.y))
            self.hitbox = (self.x, self.image_rect.y, 100, 100)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

        elif self.face_right:
            window.blit(char_img_scaling()[self.stepIndex], (self.x, self.y))
            self.hitbox = (self.x, self.y, 100, 100)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

            if self.count > 25:
                self.stepIndex += 1
                self.count = 0

    # The jumping action
    def make_a_jump(self, jump):
        self.image_rect.y -= self.jump_vel
        self.jump_vel -= 0.015

        if self.jump_vel < -3:
            self.jump = False
            self.jump_vel = self.JUMP_VEL
            self.image_rect.y = self.y


# Stone object
class Stone(object):
    """Class object for the in-game stone and its attributes"""
    img = stone_scaled

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox1 = (x, y, width, height)
        self.hitbox2 = (x, y, width, height)
        self.hitbox3 = (x, y, width, height)
        self.count = 0

    # Displaying the stone on the game window
    def draw(self, window):
        self.hitbox1 = (self.x, self.y + 70, self.width + 45, self.height - 25)
        self.hitbox2 = (self.x + 15, self.y + 50, self.width + 30, self.height - 60)
        self.hitbox3 = (self.x + 40, self.y + 50, self.width - 20, self.height - 110)
        if self.count >= 8:
            self.count = 0
        window.blit(self.img, (self.x, 390))
        self.count += 1
        pygame.draw.rect(window, (255, 0, 0), self.hitbox1, 2)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox2, 2)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox3, 2)

    # If the character collides with the stone
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox1[0] and rect[0] < self.hitbox1[0] + self.hitbox1[2]:
            if rect[1] + rect[3] > self.hitbox1[1]:
                return True
        return False


# Mushroom object
class Mushroom(object):
    """Class object for the in-game mushroom and its attributes"""
    img2 = mushroom_scaled

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox1 = (x, y, width, height)
        self.hitbox2 = (x, y, width, height)
        self.hitbox3 = (x, y, width, height)
        self.count = 0

    # set all members to their initial value
    # Displaying the mushroom on the game window
    def draw(self, window):
        self.hitbox1 = (self.x, self.y + 70, self.width + 25, self.height - 25)
        self.hitbox2 = (self.x + 20, self.y + 50, self.width - 25, self.height - 80)
        self.hitbox3 = (self.x + 35, self.y + 50, self.width - 55, self.height - 120)
        if self.count >= 8:
            self.count = 0
        window.blit(self.img2, (self.x, 385))
        self.count += 1
        pygame.draw.rect(window, (255, 0, 0), self.hitbox1, 2)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox2, 2)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox3, 2)

    # If the mushroom collides with the character
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox1[0] and rect[0] < self.hitbox1[0] + self.hitbox1[2]:
            if rect[1] + rect[3] > self.hitbox1[1]:
                return True

        if rect[0] + rect[2] > self.hitbox2[0] and rect[0] < self.hitbox2[0] + self.hitbox2[2]:
            if rect[1] + rect[3] > self.hitbox2[1]:
                return True

        if rect[0] + rect[2] > self.hitbox3[0] and rect[0] < self.hitbox3[0] + self.hitbox3[2]:
            if rect[1] + rect[3] > self.hitbox3[1]:
                return True
        return False


# Main display for the game window
def draw_game():
    """Main display for the game window"""
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

    player.draw_char()

    for objectt in objects:
        objectt.draw(window)

    pygame.display.update()


# Variables
width = 1100
i = 0
black = (0, 0, 0)
# Eug added these var 24/11
global death_count
death_count = 0
height = 600

pygame.time.set_timer(USEREVENT + 2, (random.randrange(2000, 4000)))
player = Character(250, 395, 10, 10, False)
objects = []
# Eugen add these global variable used in update function in Mushroom class
game_speed = 17


# Eugenio added to clean the object and restart again
def restart_game(objects, player, objectt):
    global score, paused, running, points
    objects.clear()
    del objectt
    del objects
    del player
    points = 0
    paused = False
    running = True
    main()


# Euge Show when the game collide
def menu(death_count, objects, player, objectt):
    global points
    points = 0
    global FONT_COLOR
    objects = objects
    player = player
    objectt = objectt

    run = True
    while run:

        # Eug add these window when the object death
        FONT_COLOR = (0, 0, 0)  # Text color will be black
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        window.fill((128, 128, 128))
        window.blit(bg, (0, 0))  # Euge thi s is the first background bg
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            # text2 = font.render("The player has eaten Mushroom and died!!!!!", True, FONT_COLOR)
            text = font.render("Press any Key to Start", True, RED)
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, FONT_COLOR)
            score = font.render("Your Score: " + str(points), True, FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (width // 2, height // 2 + 50)
            window.blit(score, scoreRect)
            f = open("score.txt", "a")
            f.write(str(points) + "\n")
            f.close()
            with open("score.txt", "r") as f:
                score = (
                    f.read()
                )  # Read all file in case values are not on a single line
                score_ints = [int(x) for x in score.split()]  # Convert strings to ints
            highscore = max(score_ints)  # sum all elements of the list
            hs_score_text = font.render(
                "High Score : " + str(highscore), True, FONT_COLOR
            )
            hs_score_rect = hs_score_text.get_rect()
            hs_score_rect.center = (width // 2, height // 2 + 100)
            window.blit(hs_score_text, hs_score_rect)
        textRect = text.get_rect()
        # textRect2 = text2.get_rect()

        textRect.center = (width // 2, height // 2)
        # textRect2.center = (width // 2, height // 5)
        window.blit(text, textRect)
        # window.blit(text2, textRect2)
        window.blit(RUNNING[0], (width // 2 - 20, height // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                # Eugenio here need to reset the game
                restart_game(objects, player, objectt)


def main():  # The application start here
    global death_count, points
    death_count = 0
    points = 0

    # Main Loop
    # Eugen added function score
    def score():
        global points, game_speed
        font = pygame.font.Font("freesansbold.ttf", 20)
        # Eug add these window when the object death
        FONT_COLOR = (0, 0, 0)  # Text color will be black
        points += 1

        if points % 100 == 0:
            game_speed += 1

        with open("score.txt", "r") as f:
            score_ints = [int(x) for x in f.read().split()]
            highscore = max(score_ints)
            if points > highscore:
                highscore = points
            text = ("High Score test: " + str(highscore) + "  Points: " + str(points))
            text = font.render(text, True, FONT_COLOR)
            text1 = "You can Press 'P' to pause."
            text1 = font.render(text1, True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (900, 40)
        textRect1 = text1.get_rect()
        textRect1.center = (900, 80)
        window.blit(text, textRect)
        window.blit(text1, textRect1)

    def unpause():
        global pause, run
        pause = False
        run = True

    def paused():
        global pause
        global FONT_COLOR
        # Eug add these window when the object death
        FONT_COLOR = (0, 0, 0)  # Text color will be black
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Game Paused, Press 'u' to Unpause", True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 3)
        window.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    # While run is True the game will run
    run = True
    while run:

        # pygame.QUIT = the red x button will close the window because run will be False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Eug new code to allow the user to pause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()

            if event.type == USEREVENT + 2:
                r = random.randrange(0, 2)
                if r == 0:
                    objects.append(Stone(1100, 380, 80, 80))
                else:
                    objects.append(Mushroom(1100, 360, 100, 100))

        # Allow the player to control the character
        # movet these code to these position to allow me have controll when collide
        userInput = pygame.key.get_pressed()

        # Movement
        player.move_char(userInput)

        for objectt in objects:
            str_objectt = str(objectt)
            for char in str_objectt:
                if char == "M":
                    if objectt.collide(player.hitbox):
                        run = False
                        # Eugenio add all these code to call the menu function
                        death_count += 0
                        pygame.time.delay(100)
                        menu(death_count, objects, player, objectt)

                if char == "S":
                    if objectt.collide(player.hitbox):
                        run = False
                        death_count += 1
                        pygame.time.delay(100)
                        menu(death_count, objects, player, objectt)

            objectt.x -= 1
            if objectt.x < objectt.width * -1:
                objects.pop(objects.index(objectt))

        # Draw game in window
        draw_game()
    score()  # Euge will be done later added these call to score function


if __name__ == '__main__':
    main()
