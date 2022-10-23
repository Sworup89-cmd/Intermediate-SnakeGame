import pygame
import random


class Food():
    def __init__(self):
        self.food = pygame.Rect(self.get_randoms()[0], self.get_randoms()[1], 8, 8)

    def get_randoms(self):
        x_random = random.randint(20, 480)
        y_random = random.randint(20, 480)

        return x_random, y_random

    def setx(self):
        self.food.x = self.get_randoms()[0]

    def sety(self):
        self.food.y = self.get_randoms()[1]

    def getx(self):
        return self.food.x

    def gety(self):
        return self.food.y

    def draw_food(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.food)
