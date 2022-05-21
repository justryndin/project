import simple_draw as sd

sd.resolution = (1200, 800)


def draw_sun(x=150, y=450):
    sd.circle(center_position=sd.get_point(x, y), radius=50, width=0)
    for i in range(0, 331, 30):
        sd.vector(start=sd.get_point(x, y), angle=i + 10, length=100, width=4)


if __name__ == '__main__':
    draw_sun()
    sd.pause()
