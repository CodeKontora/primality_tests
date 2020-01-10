from bruteforce import brute_force
from wilson import Wilson_test
from ferma import Fermat_test
from miller_rabin import Miller_Rabin_test
from prime_numbers import search_prime_number


# Проверяем на первых сорока четырёх простых числах
def test_on_first_44_prime_number():
    prime_numbers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                    67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    for num in prime_numbers:
        assert brute_force(num) == True
        assert Wilson_test(num) == True
        assert Fermat_test(num) == True
        assert Miller_Rabin_test(num) == True


# Проверяем на чётных числах 
def test_on_even_number():
    for num in range(4, 30, 2):
        assert brute_force(num) == False
        assert Wilson_test(num) == False
        assert Fermat_test(num) == False
        assert Miller_Rabin_test(num) == False


# Проверяем на положительных числах
def test_on_positive_number():
    for num in range(4, 1000, 1):
        assert brute_force(num) == Wilson_test(num) == Fermat_test(num) == Miller_Rabin_test(num)


# Проверяем на отрицательных числах
def test_on_negative_number():
    for num in range(1, -30, -1):
        assert brute_force(num) == False
        assert Wilson_test(num) == False
        assert Fermat_test(num) == False
        assert Miller_Rabin_test(num) == False


# Проверяем тест Миллера-Рабина на большом простом числе
def test_on_large_prime_number():
    large_prime_number = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
    assert Miller_Rabin_test(large_prime_number) == True


# Проверяем тест Миллера-Рабина на простых числах Белла
def test_on_Bell_numbers():
    prime_Bell_numbers = [2, 5, 877, 27644437, 35742549198872617291353508656626642567,
                          359334085968622831041960188598043661065388726959079837]
    for num in prime_Bell_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых числах Кэрола
def test_on_Carol_numbers():
    prime_Carol_numbers = [7, 47, 223, 3967, 16127, 1046527, 16769023, 1073676287,
                           68718952447, 274876858367, 4398042316799, 1125899839733759,
                           18014398241046527, 1298074214633706835075030044377087]
    for num in prime_Carol_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых числах Мерсенна
def test_on_Mersenne_numbers():
    prime_Mersenne_numbers = [3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951,
                              618970019642690137449562111, 162259276829213363391578010288127,
                              170141183460469231731687303715884105727]
    for num in prime_Mersenne_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых числах Ньюмена — Шэнкса — Уильямса
def test_on_NSW_numbers():
    prime_NSW_numbers = [7, 41, 239, 9369319, 63018038201, 489133282872437279, 19175002942688032928599,
                         123426017006182806728593424683999798008235734137469123231828679]
    for num in prime_NSW_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых числах Фибоначчи
def test_on_Fibonacci_numbers():
    prime_Fibonacci_numbers = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073,
                               99194853094755497, 1066340417491710595814572169, 19134702400093278081449423917]
    for num in prime_Fibonacci_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых уникальных числах
def test_on_unique_numbers():
    prime_unique_numbers = [3, 11, 37, 101, 9091, 9901, 333667, 909091, 99990001, 999999000001, 9999999900000001,
                            909090909090909091, 1111111111111111111, 11111111111111111111111, 900900900900990990990991]
    for num in prime_unique_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем тест Миллера-Рабина на простых факториальных числах
def test_on_factorials_numbers():
    prime_factorials_numbers = [2, 3, 5, 7, 23, 719, 5039, 39916801, 479001599, 87178291199, 10888869450418352160768000001,
                                265252859812191058636308479999999, 263130836933693530167218012159999999,
                                8683317618811886495518194401279999999]
    for num in prime_factorials_numbers:
        assert Miller_Rabin_test(num) == True


# Проверяем алгоритм поиска простых чисел через простой перебор и тест Ферма
def test_on_searched_prime_number():
    prime_numbers = []
    for num in range(2, 51):
        prime_numbers.append(search_prime_number(bit_length=num))
    for num in prime_numbers:
        assert brute_force(num) == Fermat_test(num)
