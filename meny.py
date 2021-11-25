import threading

import pygame
import sys

import jumping_game_v2
#import registration_form
#import login_form

# --- constants --- (UPPER_CASE_NAMES)

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

YELLOW = (255,255, 0)

# --- classes --- (CamelCaseNanes)

# empty

# --- functions --- (lower_case_names_
#Tet formatering i buttons
def button_create(text, rect, inactive_color, active_color, action):

    font = pygame.font.Font(None, 25)#storlek på texten

    button_rect = pygame.Rect(rect)

    text = font.render(text, True, BLACK) #Button Text color
    text_rect = text.get_rect(center=button_rect.center)

    return [text, text_rect, button_rect, inactive_color, active_color, action, False]


def button_check(info, event):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if event.type == pygame.MOUSEMOTION:
        # hover = True/False
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()


def button_draw(screen, info):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)

# ---

def on_click_button_1():
    global stage
    stage = 'game'
    jumping_game_v2.main()
    #jumping_game.main()
    print('You clicked Button 1')

def on_click_button_2():
    global stage
    stage = 'registration'
    #registration_form.start()
    print('You clicked Button 2')

def on_click_button_3():
    global stage
    stage = 'exit'
    print('You clicked Button 3 Exit')
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def on_click_button_4():
    global stage
    stage = 'login'
    #login_form.function here
    print('You clicked Button 4')



def on_click_button_return():
    global stage
    stage = 'menu'

    print('You clicked Button Return')


# --- main ---  (lower_case_names)

# - init -

pygame.init()
# Load and scale the background image
bg_img = pygame.image.load('pictures/2d_background.jpg')
bg = pygame.transform.scale(bg_img, (1100, 600))

# - objects -

stage = 'menu'

button_1 = button_create("Start the Game", (440, 100, 200, 75), WHITE , GREEN, on_click_button_1)
button_2 = button_create("Registration", (440, 200, 200, 75), WHITE , GREEN, on_click_button_2)
button_3 = button_create("Exit", (440, 400, 200, 75), WHITE , GREEN, on_click_button_3)
button_4 = button_create("Login", (440, 300, 200, 75), WHITE , GREEN, on_click_button_4)

button_return = button_create("Restart", (440, 400, 200, 75), RED, GREEN, on_click_button_return)

# - mainloop -


def main():
    running = True
    while running:
        # - events -
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if stage == 'menu':
            button_check(button_1, event)
            button_check(button_2, event)
            button_check(button_4, event)
            button_check(button_3, event)
        elif stage == 'game':
            button_check(button_return, event)
        elif stage == 'registration':
            button_check(button_return, event)
        elif stage == 'login':
            button_check(button_return, event)


        # - draws -
        screen = pygame.display.set_mode((1100,600))
        #screen_rect = screen.get_rect()
        # The first background picture
        screen.fill(WHITE) #Om jag remove these code the bg will be black
        screen.blit(bg, (0, 0))

        pygame.display.set_caption("Jumping game")


        if stage == 'menu':
            button_draw(screen, button_1)
            button_draw(screen, button_2)
            button_draw(screen, button_4)
            button_draw(screen, button_3)
        elif stage == 'game':
            button_draw(screen, button_return)
        elif stage == 'registration':
            button_draw(screen, button_return)
        elif stage == 'login':
            button_draw(screen, button_return)
        #elif stage == 'exit':
        #    pass
        pygame.display.update()


    pygame.display.quit()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()


