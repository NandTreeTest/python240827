import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록깨기 게임")

# 색상 설정
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# 공 설정
ball_width = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_width // 2
ball_dx = 4 * random.choice([-1, 1])
ball_dy = -4

# 패들 설정
paddle_width = 1000
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - paddle_height - 10
paddle_dx = 6

# 블록 설정
block_width = 75
block_height = 20
blocks = []
for i in range(6):
    for j in range(8):
        block_x = j * (block_width + 10) + 35
        block_y = i * (block_height + 10) + 50
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# 게임 루프
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_dx
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_dx

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 벽에 공이 닿으면 방향 전환
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # 패들에 공이 닿으면 방향 전환
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y < paddle_y + paddle_height):
        ball_dy = -ball_dy

    # 블록에 공이 닿으면 블록 삭제 및 방향 전환
    for block in blocks[:]:
        if block.collidepoint(ball_x + ball_width // 2, ball_y + ball_width // 2):
            blocks.remove(block)
            ball_dy = -ball_dy
            break

    # 공이 바닥에 닿으면 게임 종료
    if ball_y > screen_height:
        running = False

    # 패들 그리기
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # 공 그리기
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_width, ball_width))

    # 블록 그리기
    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    pygame.time.Clock().tick(60)

pygame.quit()
