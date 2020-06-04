def to_bin(n):
    '''
    Converts number n to binary
    '''    
    if n <= 1:
        return(str(n))
    return(to_bin(n//2)+str(n%2))

def bin_to_hex(n):
    '''
    Converts number n to hex
    '''
    a = 0
    j = 3
    for i in range(8):
        if i == 4:
            answer = DEC[a]
            a = 0
            j = 7
        a += int(n[i]) * 2**(j-i)
    answer += DEC[a]
    return(answer)

def leading_zeros(n):
    '''
    Adds leading zeros to hex number
    '''
    r = ''
    for i in n:
        d = to_bin(HEX[i])
        if len(d)<4:
            d = '0' * (4 - len(d)) + d
        r += d
    if len(r) < 8:
        r = '0000' + r
    return(r)

HEX = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
DEC = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

a = input().lower().split()
n1 = leading_zeros(a[1])
n2 = leading_zeros(a[0])
xor = ''


for i in range(8):
    if n1[i] != n2[i]:
        xor += '1'
    else:
        xor += '0'

print(bin_to_hex(xor))


'''
Вычислите XOR от двух чисел.

Входные данные
Два целых шестнадцатеричных числа меньших FF.

Выходные данные
Побитовый XOR этих чисел в шестнадцетиричном виде

Примеры
Вход    Выход
1 23    22
f0 0f   ff
'''