﻿a = int(input())
b = int(input())
while b != 0:
    if a < b:
        a, b = b, a
    a, b = b, a%b
print(a)

'''
Необходимо найти НОД двух чисел, используя алгоритм Евклида.

Формат входных данных
На вход подаются два натуральных числа, по числу в новой строке.

Формат выходных данных
Одно число - НОД входных чисел.

Примеры
Ввод 	Вывод
30      6
18

Ввод 	Вывод
1071    21
462
'''
