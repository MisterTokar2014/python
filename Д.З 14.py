import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Установка размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Погоня от полиции")

# Загрузка изображений машин и дороги
player_car = pygame.image.load('car-top-view-icon-13-transformed.png')
police_car = pygame.image.load('i_(1)-jI2Bkx5U4S-transformed.png')
road = pygame.image.load('3542a7bf6f74fe1.png')

# Начальные положения машин
player_car_x = 370
player_car_y = 480

police_car_x = random.randint(100, 600)
police_car_y = -100
police_car_speed = 5

# Флаг для проверки окончания игры
game_over = False

clock = pygame.time.Clock()

# Основной игровой цикл
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_car_x -= 5
    if keys[pygame.K_RIGHT]:
        player_car_x += 5

    police_car_y += police_car_speed
    if police_car_y > screen_height:
        police_car_y = -100
        police_car_x = random.randint(100, 600)

    # Отрисовка игровых объектов
    screen.fill(WHITE)
    screen.blit(road, (0, 0))
    screen.blit(player_car, (player_car_x, player_car_y))
    screen.blit(police_car, (police_car_x, police_car_y))

    # Проверка на столкновение игрока с полицейской машиной
    if player_car_x < police_car_x + 50 and player_car_x + 50 > police_car_x:
        if player_car_y < police_car_y + 100 and player_car_y + 100 > police_car_y:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
