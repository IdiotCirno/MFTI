def to_bin(n):
    '''
    Converts number n to binary
    '''    
    if n <= 1:
        return(str(n))
    return(to_bin(n//2)+str(n%2))

a = to_bin(int(input()))
c = 0
for i in a:
    if i == '1':
        c += 1

print(c)


'''
Сколько 1 в бинарной записи числа

Найти, сколько единиц содержит бинарная запись числа.

Входные данные
Целое неотрицательное число K.

Выходные данные
Сколько единиц содержит бинарная запись числа.

Примеры
Вход    Выход
5       2
'''