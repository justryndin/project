# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Дарья', "Егор", "Иван"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Дарья", 165],
    ["Егор", 185],
    ["Иван", 180]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост Дарьи - {my_family_height[0][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print(f'Общий рост моей семьи - {my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]} см')