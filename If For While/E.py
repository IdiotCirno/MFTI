﻿N = int(input(''))
k=1
test=2

while test<N:
    test*=2
    k+=1
print(k)

'''
По данному натуральному числу N выведите такое наименьшее целое число k , что 2^k >= N .

ВАЖНО! В данной задаче необходимо использовать цикл. Использование инструкции if запрещено. В этой задаче нельзя использовать возведение в степень.

формат входных данных
На вход программе подается натуральное число N , не превышающее 10000.

формат выходных данных
Требуется напечатать наименьшее k , удовлетворяющее условию задачи 
'''