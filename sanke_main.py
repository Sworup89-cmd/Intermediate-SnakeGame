import pygame
from snake import Snake
from Food import Food
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))

snake = Snake()
direction = snake.get_inital_head()

food = Food()

running = True
while running:
    pygame.time.delay(100)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if direction != "RIGHT":
                direction = snake.move("LEFT")
        if keys[pygame.K_RIGHT]:
            if direction != "LEFT":
                direction = snake.move("RIGHT")
        if keys[pygame.K_UP]:
            if direction != "DOWN":
                direction = snake.move("UP")
        if keys[pygame.K_DOWN]:
            if direction != "UP":
                direction = snake.move("DOWN")

    if snake.get_snake_head().collidepoint(food.getx(), food.gety()):
        food.setx()
        food.sety()
        snake.extend()

    if snake.get_snake_head().x > 490 or snake.get_snake_head().y > 490 or snake.get_snake_head().x < 0 or snake.get_snake_head().y < 0:
        pygame.quit()
        sys.exit()

    for snake_body_part in snake.get_snake_body():
        if snake.get_snake_head().x == snake_body_part.x and snake.get_snake_head().y == snake_body_part.y:
            pygame.quit()
            sys.exit()

    snake.draw_snake(screen)
    food.draw_food(screen)
    snake.move(direction)
    pygame.display.update()

pygame.quit()
