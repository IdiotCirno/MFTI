﻿m=int(input(''))
while True:
    N = int(input(''))
    if N:
        if m<N:
            m=N
    else:
        break
print(m)

'''
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.

Числа, следующие за нулем, считывать не нужно.

Формат входных данных
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).

Формат выходных данных
Выведите ответ на задачу (одно число).

Примеры
Ввод 	Вывод
1       9
7
9
0
'''