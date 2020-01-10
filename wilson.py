from math import factorial


def Wilson_test(number):
    # Если число меньше 2, то проверять его не нужно
    if number < 2:
        return False
    else:
        # Вычисляем числитель
        numerator = factorial(number - 1) + 1
        # Делим числитель на знаменатель number по модулю
        # Если разделилось нацело, значит число простое
        if numerator % number == 0:
            return True
    # Иначе – составное
    return False
