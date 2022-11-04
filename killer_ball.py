import numpy as np
import pygame
from pygame.draw import *
from random import randint
pygame.init()

# списки с координатами цетров шариков, их радиуами, цветом и временем жизни, и скоростью по осям
x_circle = []
y_circle = []
r_circle = []
c_circle = []
t_circle = []
name = []
v_x = []
v_y = []


def new_balls():
    """генерирует новые шарики"""
    n = randint(0, 1)
    for i in range(n):
        x = randint(100, x_pixels)
        x_circle.append(x)
        y = randint(100, y_pixels)
        y_circle.append(y)
        r = randint(10, 50)
        r_circle.append(r)
        color = COLORS[randint(0, 5)]
        c_circle.append(color)
        name.append("circle")
        t = randint(0, 95)
        t_circle.append(t)
        vx = randint(-30, 30)
        v_x.append(vx)
        vy = randint(-30, 30)
        v_y.append(vy)


def draw():
    """Рисует созданные шарики"""
    for i in range(len(r_circle)):
        if t_circle[i] <= 100:
            circle(screen, c_circle[i], (x_circle[i], y_circle[i]), r_circle[i])


def maturation():
    """Увеличивает возраст шариков"""
    for i in range(len(t_circle)):
        t_circle[i] += 1


def reflection():
    """Отражение шариков от стен"""
    for i in range(len(x_circle)):
        if x_circle[i] <= v_x[i] <= 0:
            v_x[i] = -v_x[i]
        if x_circle[i] >= x_pixels - v_x[i] and v_x[i] >= 0:
            v_x[i] = -v_x[i]
        if y_circle[i] <= v_y[i] <= 0:
            v_y[i] = -v_y[i]
        if y_circle[i] >= y_pixels - v_y[i] and v_y[i] >= 0:
            v_y[i] = -v_y[i]


def motion():
    """Движение шариков"""
    for i in range(len(x_circle)):
        x_circle[i] += v_x[i]
        y_circle[i] += v_y[i]


def distanсe(x1, y1, x2, y2):
    """Считает расстояние между точками (x1, y1) и (x2, y2)"""
    d = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d


def is_in_circle(x, y, x0, y0, r):
    """Проверяет попадает ли точка в круг

    точка (x, y)
    центр круга (x0, y0)
    радиус круга r
    """
    if distanсe(x, y, x0, y0) <= r:
        return True
    else:
        return False


def special_ball():
    """Создаёт мишень-убийцу"""
    x = randint(100, x_pixels)
    y = randint(100, y_pixels)
    r = randint(10, 100)
    r_circle.append(r)
    color = (255, 255, 255)
    t = 0
    vx = randint(-20, 20)
    vy = randint(-20, 20)
    x_circle.append(x)
    y_circle.append(y)
    t_circle.append(t)
    c_circle.append(color)
    v_x.append(vx)
    v_y.append(vy)
    name.append("killer_ball")
    print


def killed_by_ball():
    for j in range(len(r_circle)):
        if name[j] == "killer_ball":
            for i in range(len(r_circle)):
                if name[i] == "circle" and is_in_circle(
                    x_circle[i],
                    y_circle[i],
                    x_circle[j],
                    y_circle[j],
                    r_circle[j]
                ):
                    t_circle[i] = 101
                    

def killer(i):
    t_circle[i] = 101


def points_counter(i, points):
    """
    Считает баллы за попадание

    r -- радиус мишени, от него зависит количество баллов
    points -- текущий счёт
    """
    if name[i] == "circle":
        points += 100/r_circle[i]
    if name[i] == "killer_ball":
        points += 1000
    return points


def click(event, x_circle, y_circle, r_circle, points):
    """
    Обрабатывает попадание мышкой по шарикам
    С координатам центра, записанными в x_circle, y_circle
    и радиусом в r_circle
    points -- текущий счёт
    """
    x, y = event.pos[0], event.pos[1]
    for i in range(len(r_circle)):
        if is_in_circle(x, y, x_circle[i], y_circle[i], r_circle[i]):
            points = points_counter(i, points)
            killer(i)
    return points


FPS = 10
x_pixels = 1200
y_pixels = 600
screen = pygame.display.set_mode((x_pixels, y_pixels))
# задаём цвета:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False
t = 0

while not finished:
    clock.tick(FPS)
    t += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points = click(event, x_circle, y_circle, r_circle, points)
    motion()
    reflection()
    killed_by_ball()
    new_balls()
    if t % 10 == 0:
        special_ball()
    draw()
    maturation()
    pygame.display.update()
    screen.fill(BLACK)

print("Your score is:", points, sep=" ")
pygame.quit()
