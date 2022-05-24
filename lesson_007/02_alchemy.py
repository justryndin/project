# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
from termcolor import cprint


class Water():  # Вода

    def __init__(self):
        self.name = "Вода"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if isinstance(other, Air):
            element = Storm()

        elif isinstance(other, Fire):
            element = Steam()

        elif isinstance(other, Earth):
            element = Dirt

        else:
            return None

        return element


class Air():  # Воздух

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if isinstance(other, Fire):
            element = Lightning()
        elif isinstance(other, Earth):
            element = Dust
        else:
            return None
        return element


class Fire():  # Огонь

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if isinstance(other, Earth):
            element = Lava()
        else:
            return None
        return element


class Earth():  # Земля
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name


class Storm():  # Шторм

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name


class Steam():  # Пар
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name


class Dirt():  # Грязь
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name


class Lightning():  # Молния
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name


class Dust():  # Пыль
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name


class Lava():  # Лава
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

print(Water())
