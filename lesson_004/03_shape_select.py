import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
COLOR_RED = sd.COLOR_RED
COLOR_ORANGE = sd.COLOR_ORANGE
COLOR_YELLOW = sd.COLOR_YELLOW
COLOR_GREEN = sd.COLOR_GREEN
COLOR_CYAN = sd.COLOR_CYAN
COLOR_BLUE = sd.COLOR_BLUE
COLOR_PURPLE = sd.COLOR_PURPLE

color_list = [COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE]


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
    print("Выберите фигуру:\n"
          "1 :Треугольник\n"
          "2 :Квадрат\n"
          "3 :Пятиугольник\n"
          "4 :Шестиугольник\n")
    choice_figure = int(input('Введите желаемую фигуру: '))
    point = sd.get_point(250, 250)
    if 1 <= choice_figure < 5:
        if choice_figure == 1:
            draw_triangle(start_point=point, angle=10)
        elif choice_figure == 2:
            draw_square(start_point=point, angle=10)
        elif choice_figure == 3:
            draw_pentagon(start_point=point, angle=10)
        elif choice_figure == 4:
            draw_hexagon(start_point=point, angle=10)

        sd.pause()
    else:
        print('Вы ввели некорректный номер!')


