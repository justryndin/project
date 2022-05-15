# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.resolution = (800, 800)
SMILE_SIZE = 50
SMILE_COLOR = sd.COLOR_YELLOW
OCULUS_COLOR = sd.COLOR_DARK_CYAN
BEARD_COLOR = sd.COLOR_WHITE


def draw_smile(x, y, color):

    # рисуем лицо
    face_point = sd.get_point(x=x, y=y)
    sd.circle(center_position=face_point, radius=SMILE_SIZE, color=color, width=0)

    # рисуем очки
    oculus_radius = round(SMILE_SIZE * 0.3)
    oculus_distance = oculus_radius * 1.3

    # рисуем глаза
    eye_radius = round(SMILE_SIZE * 0.1)
    right_eye_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_eye_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)

    # рисуем улыбку
    step = SMILE_SIZE // 40
    smile_step = SMILE_SIZE // 10
    smile_y_pos = y
    smile_length = (SMILE_SIZE - round(SMILE_SIZE * (5 / 7)))

    for i in range(x-smile_length, x+smile_length+1, step):

        if i <= x:
            smile_step += step
        else:
            smile_step -= step

        point_start = sd.get_point(i, smile_y_pos-smile_length)
        point_end = sd.get_point(i, smile_y_pos-smile_length-smile_step)
        sd.line(point_start, point_end, sd.COLOR_RED, width=step)


# рисуем смайлы
for _ in range(10):
    rnd_point = sd.random_point()
    draw_smile(rnd_point.x, rnd_point.y, SMILE_COLOR)

sd.pause()