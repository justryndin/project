import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

COLOR_RED = sd.COLOR_RED
COLOR_ORANGE = sd.COLOR_ORANGE
COLOR_YELLOW = sd.COLOR_YELLOW
COLOR_GREEN = sd.COLOR_GREEN
COLOR_CYAN = sd.COLOR_CYAN
COLOR_BLUE = sd.COLOR_BLUE
COLOR_PURPLE = sd.COLOR_PURPLE

color_choice = [COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE]


# TODO здесь ваш код
def draw_figure(start_point, side_count, angle, length, color, width=3):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3, width=width)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, width=width, color=color)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length, width=width)
            step += angle_step
        vector.draw(color=color)


def draw_triangle(start_point, angle=0, length=100, color=COLOR_YELLOW):
    side = 3
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_square(start_point, angle=0, length=100, color=COLOR_YELLOW):
    side = 4
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_pentagon(start_point, angle=0, length=100, color=COLOR_YELLOW):
    side = 5
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_hexagon(start_point, angle=0, length=100, color=COLOR_YELLOW):
    side = 6
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


if __name__ == '__main__':
    print('Приветствую тебя!\n')
    print('Возможные цвета:\n1: red\n2 : orange\n3: yellow\n4: green\n5: cyan\n6: blue\n7: purple\n')
    color_selection = int(input('Введите желаемый цвет: '))
    if 1 <= color_selection <= 7:
        point = sd.get_point(400, 400)
        draw_triangle(start_point=point, angle=20, length=100, color=color_choice[color_selection - 1])

        point = sd.get_point(100, 400)
        draw_square(start_point=point, angle=20, length=100, color=color_choice[color_selection - 1])

        point = sd.get_point(400, 100)
        draw_pentagon(start_point=point, angle=20, length=100, color=color_choice[color_selection - 1])

        point = sd.get_point(100, 100)
        draw_hexagon(start_point=point, angle=20, length=100, color=color_choice[color_selection - 1])

        sd.pause()
    else:
        print('Вы ввели некорректный номер!')
