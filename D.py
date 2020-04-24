count = 0
triplesum = 0

x = input()
try:
    x = int(x)
except:
    A = x.split()
    x = A[0]
    A = A[1:]
    A.append(x)
    s = ' '
    print(s.join(A))
    pass
else:
    if x != '#':
        x = int(x)
        min = max = sum = triple = x
        count = 1
        
    while True:
        x = input()
        if x != '#':
            x = int(x)
            count += 1
            if min > x:
                min = x
            if max < x:
                max = x
            sum += x
            triple += x
            if not(count%3):
                triplesum += triple%x
                triple = 0
        else:
            break

    mean = round(sum/count, 3)

    print(mean, max, min, triplesum)


'''
На вход программа получает набор чисел, заканчивающихся решеткой. Вам требуется найти: среднее, максимальное и минимальное число в последовательности. Так же нужно вывести cумму остатков от деления суммы троек на последнее число тройки (каждые 3 введеных числа образуют тройку).
Для понимания рассмотрим пример входных данных: 1 2 3 4 5 6 среднее: (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5 максимум: 6 минимум: 1 сумма остатков троек: (1 + 2 + 3) mod 3 + (4 + 5 + 6) mod 6 = 6 mod 3 + 15 mod 6 = 0 + 3 = 3
Среднее выводить, округлив до трех знаков после запятой. Для этого нужно использовать функцию round(x, 3)
Того ваша программа должна вывести: 3.5 6 1 3
Подумайте, имеет ли смысл хранить всю последовательность.

Формат входных данных
Последовательность чисел, заканчивающися '#'. Все числа от 1 до 100. Количество чисел в последовательности кратно трем. Одно число на строку.

Формат выходных данных
Четыре числа, разделенных пробелом.

Примеры
Ввод 	Вывод
1       3.5 6 1 3
2
3
4
5
6
#
'''