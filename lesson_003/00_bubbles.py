from random import random

import simple_draw as sd
sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def draw_circle(point, radius, step, amount):
    radius = radius
    for _ in range(amount):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=sd.random_color())


# point = sd.get_point(200, 200)
# draw_circle(point=point, radius=50, step=10, amount=5)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# for i in range(100, 1001, 100):
#     point = sd.get_point(i, 200)
#     draw_circle(point=point, radius=50, step=10, amount=3)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for i in range(100, 301, 100):
#     for k in range(100, 1001, 100):
#         point = sd.get_point(k, i)
#         draw_circle(point=point, radius=50, step=10, amount=3)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(101):
    point = sd.random_point()
    step = random()
    draw_circle(point=point, radius=40, step=step, amount=3)

sd.pause()