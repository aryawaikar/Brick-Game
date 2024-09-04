import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
BRICK_ROWS = 5
BRICK_COLUMNS = 10
BRICK_PADDING = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_dx = BALL_SPEED * random.choice((-1, 1))
ball_dy = -BALL_SPEED

# Bricks
bricks = []
colors = [RED, ORANGE, YELLOW, WHITE ,BLUE, PURPLE]
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        brick_x = col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_PADDING
        brick_y = row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_PADDING + 50
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append((brick, colors[row % len(colors)]))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(10, 0)

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick, color in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove((brick, color))
            ball_dy = -ball_dy
            break

    # Ball out of bounds
    if ball.bottom >= HEIGHT:
        running = False  # Game over

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
