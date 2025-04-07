print("hello, world!")

import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame 테스트")

# 배경색 설정 (RGB: 연한 파랑)
background_color = (173, 216, 230)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)  # 배경색으로 채우기
    pygame.display.flip()          # 화면 업데이트

# 종료
pygame.quit()
sys.exit()
