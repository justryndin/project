import simple_draw as sd

sd.resolution = (1200, 800)

point_0 = sd.get_point(850, 30)


def draw_branches_v2(point, angle, length=100):
    if length < 5:
        return
    if length > 25:
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=10)
    else:
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
    if length < 10:
        vector.draw(color=sd.COLOR_DARK_GREEN)
    else:
        vector.draw(color=sd.COLOR_DARK_ORANGE)

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


if __name__ == '__main__':
    root_point = sd.get_point(850, 30)
    draw_branches_v2(point=root_point, angle=90, length=70)
    sd.pause()
