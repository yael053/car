import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()
size = height, width = (650, 650)
screen = pygame.display.set_mode(size)

road_w = width // 1.6  # the width of green rect
roadmark_w = width // 80
running = True
game_over = False

pygame.display.set_caption("Yael's car game")

black = (0, 150, 0)
screen.fill(black)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.display.update()

redCar = pygame.image.load("car.jpeg")
redCar_loc = redCar.get_rect()  # get and creat object of the size and the picture
# place the cars in the game
redCar_loc.center = right_lane, height * 0.8

blueCar = pygame.image.load("otherCar.jpeg")
blueCar_loc = blueCar.get_rect()
blueCar_loc.center = left_lane, height * 0.2
point = 0
while running:
    if not game_over:
        blueCar_loc[1] += speed  # moves the car
        if blueCar_loc[1] > height:
            blueCar_loc[1] = -1000  # bring the car back to the screen

            if random.randint(0, 1) == 0:  # choose between right or left
                blueCar_loc.center = right_lane, -1000
            else:
                blueCar_loc.center = left_lane, -1000

        if redCar_loc[0] == blueCar_loc[0] and redCar_loc[1] - blueCar_loc[1] < blueCar_loc.height:
            print(point)
            game_over = True

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_LEFT] and redCar_loc[0] > 325:
                    redCar_loc = redCar_loc.move([-road_w // 2, 0])
                    if redCar_loc[0] != blueCar_loc[0]:
                        point = point + 1
                if event.key in [K_RIGHT] and redCar_loc[0] < 325:
                    redCar_loc = redCar_loc.move([road_w // 2, 0])

        pygame.draw.rect(
            screen,
            (0, 0, 0),  # black
            (width / 2 - road_w / 2, 0, road_w, height))

        pygame.draw.rect(
            screen,
            (255, 240, 60),  # yellow
            (width / 2 - roadmark_w / 2, 0, roadmark_w, height))

        pygame.draw.rect(
            screen,
            (255, 255, 255),  # white
            (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))

        pygame.draw.rect(
            screen,
            (255, 255, 255),  # white
            (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

        screen.blit(redCar, redCar_loc)  # blit - show on the screean
        screen.blit(blueCar, blueCar_loc)

        if game_over:
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (162, 120, 325, 325))
            font = pygame.font.SysFont("bahnschrift", 25)
            text_n = str(point)
            text_p = font.render(f"POINTS: {text_n}", True, (0, 0, 0))


            if point in range(0, 6):
                font = pygame.font.SysFont("bahnschrift", 20)
                text_s = font.render("be focus!", True, (0, 0, 0))
                print("A")
            elif point in range(6, 50):
                font = pygame.font.SysFont("bahnschrift", 20)
                text_s = font.render("your are very good!", True, (0, 0, 0))
                print("D")
            else:
                font = pygame.font.SysFont("bahnschrift", 20)
                text_s = font.render("you love this game ha!", True, (0, 0, 0))
                print("S")

            font = pygame.font.SysFont("bahnschrift", 30)
            text_pl = font.render("PLAY AGAIN", True, (0, 0, 0))
            text_Q = font.render("QUIT", True, (0, 0, 0))
            if point in range(0, 6):
                screen.blit(text_s, (268, 190))
            else:
                screen.blit(text_s, (245, 190))
            screen.blit(text_p, (268, 150))


            screen.blit(text_pl, (240, 260))
            screen.blit(text_Q, (280, 320))







    pygame.display.update()

pygame.quit()
