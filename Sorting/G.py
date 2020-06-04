word = input()
A = []
for i in word:
    if i == '.':
        break
    else:
        A.append(i)

def selection_sort(A):
    j = m = 0
    while j < len(A):
        for i in range(j, len(A)):
            if A[i] < A[m]:
                m = i
        A[j], A[m] = A[m], A[j]
        j += 1
        m = j
    return A

answer = ''
for i in selection_sort(A):
    answer += i
answer += '.'
print(answer)
'''
Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.

Входные данные
Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.

Выходные данные
Отсортированная строка с точкой на конце.

Примеры
Вход                Выход
qwe Rty5, yu! Mama.    !,5MRaaemqtuwyy.
'''