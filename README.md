# Алгоритмы проверки на простоту  
[Разбор алгоритмов проверки чисел на простоту на Код Конторе](https://code-kontora.ru/?go=all/is-prime-number/)  

## [bruteforce.py](/bruteforce.py)  
Простой перебор всех чисел от 2 до sqrt(n)  

## [wilson.py](/wilson.py)  
Проверка через теорему Вильсона  

## [ferma.py](/ferma.py)  
Проверка через тест Ферма  

## [miller_rabin.py](/miller_rabin.py)  
Проверка через тест Миллера-Рабина

## [prime_numbers.py](/prime_numbers.py)  
Алгоритм поиска простых чисел нужного размера с помощью теста Миллера-Рабина  

## [test.py](/test.py)  
Тесты для алгоритмов проверки числа на простоту.  
1. Если pytest не установлен, то нужно поставить его: `pip3 install pytest`   
2. Чтобы запустить тесты: `pytest test.py`  
[![asciicast](https://asciinema.org/a/C1va4NUMjdt7Q7a0NxhoEC40c.svg)](https://asciinema.org/a/C1va4NUMjdt7Q7a0NxhoEC40c)
