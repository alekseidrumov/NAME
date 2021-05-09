'''
ЗАДАНИЕ ПО ЗМЕЙКЕ
'''
"""
# підключаємо бібліотеки 
from turtle import * # черепашка
from random import randrange # рандом
from freegames import square, vector # freegames - вектори

food = vector(0, 10) # 0, 10 початкові координати
snake = [vector(360, 300)] # 360, 300 початкові координати змійки
aim = vector(-10, 0) # -10, 0 початковий напрям змійки
timer = 100
def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    # Перевірка на те чи ми знаходимось всередині карти
    # Границі карти в пікселях, можна міняти
    return -400 < head.x < 380 and -400 < head.y < 380

def move():
    global timer
    # рух змійки
    head = snake[-1].copy()
    head.move(aim)
    # Створюємо червоний квадрат перед змійкою, якщо вона вилазить за межі карти
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
    # рандомна поява їжі
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-40, 40) * 10
        food.y = randrange(-40, 40) * 10
        timer = timer - 1

    else:
        snake.pop(0)

    clear()
    # колір змійки 
    
    for body in snake:
        square(body.x, body.y, 9, 'green')
    
    # колір їжі
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, timer)
# початковий розмір екрану
setup(840, 820, 370, 0)
bgcolor("#1E1E1E")
hideturtle()
tracer(False)
listen()
# клавіші управління, можна міняти
onkey(lambda: change(10, 0), 'Right') # d
onkey(lambda: change(-10, 0), 'Left') # a
onkey(lambda: change(0, 10), 'Up') # w
onkey(lambda: change(0, -10), 'Down') # s
move()
done()
"""


'''
ЗАДАНИЕ ПО Flapy Bird
'''

"""
Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""


from random import * # рандомні числа (випадкові числа)
from turtle import *  # бібліотека для графіки
from freegames import vector # додаткова бібліотека для turtle
speed = 100
bird = vector(0, 0) # птах
balls = [] # це м'ячі
# функція для нажимання на екран, підстрибування
def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 50) # 0,50 це відстань на яку ми підстрибуємо
    bird.move(up)
# перевірка на те чи ми заходимо за межі карти
def inside(point):
    "Return True if point on screen."
    return -300 < point.x < 300 and -300 < point.y < 300
# для малювання кольорів і графіки
def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)
# якщо ми живі то світимося фіолетовим кольором
    if alive:
        dot(10, 'purple')
    else:
        dot(10, 'black') # якщо помираємо світимося чорним кольором
# м'ячі позначені фіолетовим кольором
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, '#6a0c6e')

    update()

def move():
    global speed
    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-299, 299)
        ball = vector(299, y)
        balls.append(ball)
        ran_speed = randrange(0,4)
        if ran_speed == 1:
            speed = speed - 1
            print("скорость:",speed)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, speed)
bgcolor("#1E1E1E")
setup(630, 630, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
