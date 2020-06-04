price, delta, m = map(int, input().split())
day = 1
week = 1
money = 0

while week <= m:
    money += price
    price += delta
    day +=1
    if day == 8:
        day =1
        week += 1

print(money)
'''
Деньги-1

Студент покупает рис каждый день.
В первую неделю рис стоит price монет.
Каждый день (перед началом рабочего дня) цена риса увеличивается на delta монет (price = price + delta).
Неделя - 7 дней.
Студент покупал рис m недель.

Написать программу (с циклом while), которая вычисляет сколько денег потратил студент.

Нужны переменные:
    day - чтобы считать дни.
    Сначала day = 1.
    Если day == 8, то это первый день новой недели day = 1
    week - чтобы считать недели. Сначала week = 1.
    Если day == 8, то началась новая неделя week = week + 1 

Входные данные
price - цена риса
delta - на сколько увеличивается цена
m - количество недель

Выходные данные
Число money - сколько денег потратил студент.

Примеры
Вход        Выход
10 1 1      91
'''