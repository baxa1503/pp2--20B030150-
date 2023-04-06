import pygame
import keyboard

# initialize pygame
pygame.init()

# set the screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set the ball properties
ball_radius = 25
ball_color = (255, 0, 0)
ball_x = (screen_width - ball_radius) // 2
ball_y = (screen_height - ball_radius) // 2
ball_speed = 0.5

# define the ball movement function
def move_ball(direction):
    global ball_x, ball_y
    if direction == 'up':
        ball_y -= ball_speed
        if ball_y < ball_radius:
            ball_y = ball_radius
    elif direction == 'down':
        ball_y += ball_speed
        if ball_y > screen_height - ball_radius:
            ball_y = screen_height - ball_radius
    elif direction == 'left':
        ball_x -= ball_speed
        if ball_x < ball_radius:
            ball_x = ball_radius
    elif direction == 'right':
        ball_x += ball_speed
        if ball_x > screen_width - ball_radius:
            ball_x = screen_width - ball_radius

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # handle keyboard input
    if keyboard.is_pressed('up'):
        move_ball('up')
    elif keyboard.is_pressed('down'):
        move_ball('down')
    elif keyboard.is_pressed('left'):
        move_ball('left')
    elif keyboard.is_pressed('right'):
        move_ball('right')
    
    # draw the ball and background
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

# quit pygame
pygame.quit()
