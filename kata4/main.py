import pygame, random, sys

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_start()

    if ball.colliderect(player) or ball.colliderect(opponenet):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 960

# colors
back_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

rectangulo = pygame.display.set_mode((screen_width, screen_height))
bola = pygame.Rect

def mover_rectangulo():
    global speed

    if rectangulo.top + 50 < screen_height:
        rectangulo.top += 3

def start_bola():
    global speed_bola_x, speed_bola_y

    if bola.left + 50 > screen_width:
        bola.top = screen_height // 2
        bola.left = 


def mover_bola():
    global speed_bola_x, speed_bola_y

    if bola.top + 50 > screen_height:
        speed_bola_x = -speed_bola_x
    if bola.left + 50 > screen_width:
    bola.top = screen_height // 2
    bola.left = screen_width // 2

bola.top += speed_bola_x
bola.left += speed_bola_y

rectangulo = pygame.Rect(10, 10, 50, 50)
bola = pygame.Rect(50, 10, 50, 50)

speed = 0
speed_bola_x = 3
speed_bola_y = 3

while True:
    screen.fill(light_gray)
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            speed = -3
        elif event.key == pygame.KEYUP:
            spedd = -3

mover_rectangulo()
mover_bola()

pygame.draw.rect(screen, white_color, rectangulo)


    pygame.display.flip()
    clock.tick(60)