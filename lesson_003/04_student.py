# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код

count = 0
student_income = educational_grant
month_expenses = 0
money_need = 0
while count < 10:
    if count == 0:
        month_expenses = expenses
    elif count >= 1:
        month_expenses *= 1.03
    count += 1
    diference = round(month_expenses - student_income, 2)
    money_need += diference
    print(f'Расходы в {count} месяце: {diference}! Итого за {count} месяц: {round(money_need, 2)}')
print(f'Студенту надо попросить {round(money_need, 2)} рублей')
