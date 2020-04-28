﻿A = []

for i in range(3):
    A.append(int(input()))

A.sort()

if A[0] + A[1] > A[2]:
    if A[0] ** 2 + A[1] ** 2 < A[2] ** 2:
        print('obtuse')
    elif A[0] ** 2 + A[1] ** 2 > A[2] ** 2  or A[0] == A[1] == A[2]:
        print('acute')
    else:
        print('right')
else:
    print('impossible')

'''
Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.

Формат входных данных
Даны три натуральных числа – стороны треугольника. Каждое число вводится с новой строки.

Формат выходных данных
Необходимо вывести одно из слов: right для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного треугольника или impossible, треугольника с такими сторонами не существует.

Примеры
Ввод 	Вывод
3       right
4
5
'''