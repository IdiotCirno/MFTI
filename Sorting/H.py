N = input()
A = list(i[::-1] for i in list(input().split()))

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
A = selection_sort(A)
for i in A:
    answer += i[::-1] + ' '

print(answer)
'''
Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц, потом десятков, потом сотен и тп.

Входные данные
Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих 30000, через пробел.

Выходные данные
Числа по возрастанию единиц, при равных единиц - по возрастанию десятков, при равных единицах и десятков - по возрастанию сотен и тп.

Примеры
Вход	        Выход
5               3 23 123 43 5
5 23 3 43 123
'''