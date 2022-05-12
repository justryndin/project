# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp = goods['Лампа']
total_lamp_quantity = store[lamp][0]['quantity']
total_lamp_price = store[lamp][0]['price']
total_lamp_amount = total_lamp_quantity * total_lamp_price

table = goods["Стол"]
total_table_quantity = store[table][0]['quantity'] + store[table][1]['quantity']
total_table_price = store[table][0]['price'] + store[table][1]['price']
total_table_amount = total_table_quantity * total_table_price

sofa = goods['Диван']
total_sofa_quantity = store[sofa][0]['quantity'] + store[sofa][1]['quantity']
total_sofa_price = store[sofa][0]['price'] + store[sofa][1]['price']
total_sofa_amount = total_sofa_quantity * total_sofa_price

chair = goods['Стул']
total_chair_quantity = store[chair][0]['quantity'] + store[chair][1]['quantity'] + store[chair][2]['quantity']
total_chair_price = store[chair][0]['price'] + store[chair][1]['price'] + store[chair][2]['price']
total_chair_amount = total_chair_quantity * total_chair_price

print(f'Лампа - {total_lamp_quantity} шт, стоимость {total_lamp_amount} руб')
print(f'Стол - {total_table_quantity} шт, стоимость {total_table_amount} руб')
print(f'Диван - {total_sofa_quantity} шт, стоимость {total_sofa_amount} руб')
print(f'Стул - {total_chair_quantity} шт, стоимость {total_chair_amount} руб')

# Рассчитать на какую сумму лежит каждого товара на складе


# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
