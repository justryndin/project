import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

sd.resolution = (1200, 800)
point_0 = sd.get_point(600, 30)


def draw_branches_v1(point, angle, length=100):
    if length < 2:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    vector.draw()

    next_point = vector.end_point
    delta = 30
    length *= 0.75

    next_angle = angle - delta * 0.7
    draw_branches_v1(next_point, next_angle, length)

    next_angle = angle + delta * 0.7
    draw_branches_v1(next_point, next_angle, length)


root_point = point_0
draw_branches_v1(point=root_point, angle=90, length=100)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75

# Пригодятся функции
# sd.random_number()
def draw_branches_v2(point, angle, length=100):
    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point

    delta = 20
    delta_deviation = delta * 0.4
    delta += sd.random_number(-delta_deviation, delta_deviation)

    length = length * 0.75
    length_deviation = round(length * 0.2)
    length += sd.random_number(0, length_deviation)

    next_angle = round(angle + delta)
    draw_branches_v2(next_point, next_angle, int(length))

    next_angle = round(angle - delta)
    draw_branches_v2(next_point, next_angle, int(length))


# root_point = point_0
# draw_branches_v2(point=root_point, angle=90, length=100)

sd.pause()
