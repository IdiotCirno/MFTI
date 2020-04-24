N = int(input())

A = []

def summ(A):
    s = 0
    for a in A:
        s += a
    return s

for i in range(N):
    #A.append([0])
    A.append([])

while True:
    x = input()
    if x == '#':
        break
    else:
        x = x.split()
        A[int(x[0])].append(int(x[1]))
        #A[int(x[0])][0] += int(x[1])

for i,z in enumerate(A):
    A[i].sort(key=lambda x: x, reverse=True)

A.sort(key=summ, reverse=True)

for a in A:
    if len(a):
        for i in a:
            print(i, end=' ')


'''
Есть результаты работы студентов в семестре. Студентов выводить в порядке суммы их баллов. Требутеся вывести отсортированные результаты работ для каждого студента.
Данные вводятся как: student_id value
student_id принимает значения от 0 до N. value от 1 до 10

Пример входных данных: 0 3 0 5 1 3 1 2
Тут представленны данные о двух студента: 0 и 1. Сумма балов студента 0 - 8. Студента 1 - 5. Значит, сначала должны быть напечатаны результаты 0 студента, затем 1. Таким образом сначала надо вывести отсортированные результаты студента 0, затем студента 1:
5 3 3 2

Напомним, что у list в питоне есть встроенный метод sort и есть функция sorted. У них есть параметр key, который определяет по каким значениям будет сортироваться объект. Например код ниже будет сортировать лист по длинне его элементов. Так же есть параметр reverse.
a = ['###', '@', '??']
a.sort(key=lambda x: len(x)) #a ['@', '??', '###']
a.sort(key=lambda x: len(x), reverse=True) # a ['###', '??', '@']

Что такое лямбда функция вы узнаете в дальнейшем (так же всегда есть сайт google). Для выполнения этого задания достаточно понять, на что надо заменить функцию len.

Формат входных данных
В первой строке N - количество студентов. Далее идет какое-то количество строк (не равное N) с результатами студентов в формате: student_id value. 0 <= student_id < N. Значения разделены пробелом. Ввод заканчивается #.

Формат выходных данных
Вывести отсортированные результаты студентов в одну строку. Сначала печатаются результаты лучшего по сумме баллов студента, потом второго и так далее. Результаты в одну строку

Примеры
Ввод 	Вывод
3       10 3 4 3 2
0 3
0 10
2 3
2 2
2 4
#

'''