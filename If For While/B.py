﻿x = int(input(''))
y = int(input(''))
x1 = int(input(''))
y1 = int(input(''))

if x==x1 or y==y1 or abs(x-x1)==abs(y-y1):
    print('YES')
else:
    print('NO')

'''
Шахматный ферзь может ходить на любое число клеток по горизонтали, по вертикали или по диагонали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом. Для простоты можно не рассматривать случай, когда данные клетки совпадают.

Формат входных данных
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

Формат выходных данных
Программа должна вывести YES, если из первой клетки ходом ферзя можно попасть во вторую. В противном случае - NO.

Примеры
Ввод 	Вывод
1       YES
1
8
8

Ввод 	Вывод
1       YES
1
8
1

Ввод 	Вывод
5       NO
5
7
4
'''