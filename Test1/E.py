﻿A = [0, 0, 1]
n = 0
x = int(input())
t = 1

while t <= x:
    t = A[n] + A[n+1] + A[n+2]
    A.append(t)
    n += 1
print(n+2)

'''
Числа трибоначчи - последовательность целых чисел {t n }, заданная с помощью рекуррентного соотношения: t 0 = 0, t 1 = 0, t 2 = 1 , t n+3 = t n + t n+1 + t n+2 Нужно найти номер первого числа трибоначчи, превосходящего заданное. Нумерация начинается с 0 .

Формат входных данных
Одно целое число.

Формат выходных данных
Одно число — номер первого числа трибоначчи, превосходящее заданное во входных данных число.

Примеры
Ввод 	Вывод
10      7

Ввод 	Вывод
0       2

Ввод 	Вывод
13      8
'''