from random import randint

_hidden_numbers = []


def generate_number():
    number = []
    count = 0
    while count <= 3:
        if count == 0:
            num = randint(1, 9)
            number.append(num)
            count += 1
        else:
            num = randint(0, 9)
            if num not in number:
                number.append(num)
                count += 1
            else:
                continue
    return number


def make_number():
    _hidden_numbers.clear()
    _hidden_numbers.extend(generate_number())
    return _hidden_numbers


def check_number(number):
    result = {'bulls': 0, 'cows': 0}
    chk_numbers = []

    for char in map(int, number):
        chk_numbers.append(char)

    for pos, hidden_number in enumerate(_hidden_numbers):
        for chk_pos, number in enumerate(chk_numbers):
            if hidden_number == number:
                if pos == chk_pos:
                    result['bulls'] += 1
                    continue
                else:
                    result['cows'] += 1

    return result


def game_over():
    pass


if __name__ == '__main__':
    make_number()
    print(check_number('1234'))
    print(check_number('1235'))
