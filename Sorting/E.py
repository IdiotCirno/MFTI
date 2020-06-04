word = input()

def brakets(word):
    if word[0] == ')':
        return('NO')
    opn = 0
    for letter in word:
        if letter == '(':   
            opn += 1
        else:
            opn -= 1
        if opn < 0:
            return('NO')
    if not(opn):
        return('YES')
    return('NO')

print(brakets(word))
'''
Скобочки

Некоторые скобочные структуры правильные, другие — неправильные. Ваша задача — определить правильная ли скобочная структура.

Входные данные
Слово в алфавите из двух круглых скобочек ( и ). Длина слова меньше 4001

Выходные данные
Либо NO, либо YES

Примеры
Вход        Выход
()          YES
)(          NO
()(())()	YES
'''