from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления \n'
'квадратного корня из заданного числа'
print(message)


def square_root(number):
    """ Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    if your_number < 0:
        return 'ошибка'
    if your_number >= 0:
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет: {sqrt(your_number)}')
    return 'Нет такого числа'


print(message)
calc(25.5)
