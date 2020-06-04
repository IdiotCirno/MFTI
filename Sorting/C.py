n = int(input())
answer = list(map(int, input().split()))
#first - lier
cur_p = 0 #first person type
knights_1 = 0#counter
for i in reversed(answer):
    next_p = abs(i-1) if cur_p==0 else i #next person type
    knights_1 += next_p
    cur_p = next_p #for next iteration
#first - knight
cur_p = 1 #first person type
knights_2 = 0#counter
for i in reversed(answer):
    next_p = abs(i-1) if cur_p==0 else i #next person type
    knights_2 += next_p
    cur_p = next_p #for next iteration
print(min(knights_1,knights_2))

'''
На острове Буяне жили N человек, каждый из которых был либо рыцарем либо лжецом, встали в круг.
Рыцари говорят только правду, лжецы всегда только лгут.
Каждому человеку в кругу задали вопрос: «Кто ты и кто твой сосед слева: рыцарь или лжец?» При этом каждый человек сказал, что он – рыцарь.
А ответы всех людей о левом соседе были записаны в следующем формате: 1 – рыцарь 0 – лжец.
Все ответы записаны в строку через пробел. Последний спрошенный человек отвечал на вопрос о первом.

Написать программу, которая по ответам жителей определяет, какое количество рыцарей заведомо присутствует в круге.

Входные данные
Первое число ( 1 < N ≤ 255 ) - количество жителей. Следующие N чисел (0 или 1), разделенных пробелами - ответы жителей.

Примеры
Вход            Выход
4 0 1 0 1       2
  1 1 1 1
0 0
1 1
'''