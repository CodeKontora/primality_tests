from math import sqrt


def brute_force(number):
    # Если число меньше 2, то проверять его не нужно
    if number < 2:
        return False
    else:
        # Ставим лимит
        limit = int(sqrt(number))
        # Счётчик для проверки
        counter = 2
        while counter <= limit:
            # Если мы разделили нацело, значит number составное
            # Возвращаем False
            if number % counter == 0:
                return False
            counter += 1
    # Если значения не разделились нацело, значит number простое число
    return True
