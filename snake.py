import pygame
import selenium

class Snake():
    def __init__(self):
        self.segments = []
        self.segments.append(pygame.Rect(250, 250, 20, 20))
        self.segments.append(pygame.Rect(230, 250, 20, 20))
        self.segments.append(pygame.Rect(210, 250, 20, 20))
        self.initial_head = "RIGHT"

    def get_inital_head(self):
        return self.initial_head

    def extend(self):
        self.segments.append(pygame.Rect(self.segments[-1].x, self.segments[-1].y, 20, 20))

    def move(self, direction):
        for segment in range(len(self.segments) - 1, -1, -1):
            if segment == 0:
                if direction == "RIGHT":
                    self.segments[segment].x += 10
                elif direction == "LEFT":
                    self.segments[segment].x -= 10
                elif direction == "UP":
                    self.segments[segment].y -= 10
                elif direction == "DOWN":
                    self.segments[segment].y += 10
            else:
                self.segments[segment].x = self.segments[segment - 1].x
                self.segments[segment].y = self.segments[segment - 1].y

        return direction

    def draw_snake(self, screen):
        for index in range(0, len(self.segments)):
            pygame.draw.rect(screen, (200, 0, 0), self.segments[index])

    def get_snake_head(self):
        return self.segments[0]

    def get_snake_body(self):
        return self.segments[2:]
