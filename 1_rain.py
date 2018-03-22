# homework 1: following the instructions in comments and make it rain!
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
pygame.display.set_caption("rain")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 600))
mike_img = pygame.image.load("images/Mike_umbrella.png").convert()
cloud_img = pygame.image.load("images/cloud.png").convert()

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = -5
        return

    def move(self):
        self.y += 5
        return

    # draw: draw the Raindrop on the screen as a line, with pygame.draw.line function
    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), 1)
        return

class Mike:
    def __init__(self):
        self.x = 400
        self.y = 400

    def hitby(self, x, y):
        r = pygame.Rect(self.x, self.y, 160, 192)
        h = r.collidepoint(x, y)
        return h

    def draw(self):
        screen.blit(mike_img, (self.x, self.y))

class Cloud:
    def __init__(self):
        self.x = 200
        self.y = 50

    def draw(self):
        screen.blit(cloud_img, (self.x, self.y))

raindrops = []
mike = Mike()
cloud = Cloud()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    raindrops.append(Raindrop())
    screen.fill((255, 255, 255))

    mike.draw()
    cloud.draw()
    for r in raindrops:
        if r.y >= 600 or mike.hitby(r.x, r.y):
            raindrops.remove(r)
        else:
            r.move()
            r.draw()
    pygame.display.update()
