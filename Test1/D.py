﻿m = 0
x = int(input())

while x != 0:
    if not(x%2) and x > m:
        m = x
    x = int(input())
print(m)

'''
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего четного элемента последовательности. Числа, следующие за нулем, считывать не нужно.

Формат входных данных
Последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит). Каждое число на новой строке.

Формат выходных данных
Одно число — максимальное четное число в последовательности, если четные числа в ней присутствуют, иначе - 0.

Примеры
Ввод 	Вывод
1       4
2
4
7
4
0

Ввод 	Вывод
1       0
3
5
0
'''
