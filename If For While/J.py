﻿m=int(input(''))
k=1
while True:
    N = int(input(''))
    if N:
        if m<N:
            m=N
            k=1
        elif m==N:            
            k+=1
    else:
        break
print(k)

'''
Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел (не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу. Числа, следующие за числом 0, считывать не нужно.

Формат входных данных
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).

Формат выходных данных
Выведите ответ на задачу (одно число).

Примеры
-> 1 ->7 ->9 ->0 -- <- 1

-> 1 ->3 ->3 ->1 ->0 -- <- 2 
'''