import simple_draw as sd

point = sd.get_point(300, 5)


def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * 0.75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


for length in range(0, 51, 10):
    branch(point=point, angle=90, length=150, delta=length)
for length in range(-50, 1, 10):
    branch(point=point, angle=90, length=150, delta=length)

sd.pause()
