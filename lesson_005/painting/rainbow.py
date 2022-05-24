import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_rainbow(x=350, y=10, radius=800, width=10):
    step = 0

    for color in rainbow_colors:
        start_point = sd.get_point(x, -y)
        sd.circle(center_position=start_point, radius=radius + step, color=color, width=width + 1)
        step += width


if __name__ == '__main__':
    draw_rainbow()
    sd.pause()
