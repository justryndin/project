import my_burger


# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.
def double_cheeseburger():
    my_burger.add_bun()
    my_burger.add_cutlets()
    my_burger.add_cucumbers()
    my_burger.add_mustard()
    my_burger.add_ketchup()
    my_burger.add_onion()
    my_burger.add_cheese()


# double_cheeseburger()
# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


def my_favotite_burger():
    double_cheeseburger()
    for _ in range(5):
        my_burger.add_cheese()

my_favotite_burger()