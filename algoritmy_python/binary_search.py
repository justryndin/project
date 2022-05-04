"""
Бинарный поиск работает только в том случае,
если список отсортирован.
Например, имена в телефонной книге хранятся в алфавитном порядке,
и вы можете воспользоваться бинарным поиском.
А что произойдет, если имена не будут отсортированы?
"""


def binary_search(list, item):
    """
    В переменных low и high хранятся границы той части списка
    в которой выполняется поиск
    :param list: Список
    :param item: Значение
    :return:
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
my_list1 = [i for i in range(1, 1000000)]
print(binary_search(my_list, 3))
print(binary_search(my_list1, 45656))
