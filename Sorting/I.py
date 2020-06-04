N = int(input())
A = []
for i in range(N):
    A.append(list(input().split()))

for j in range(len(A)):
    M = j
    for i in range(j+1, len(A)):
        if float(A[M][1]) > float(A[i][1]):
            M = i
        elif float(A[M][1]) == float(A[i][1]):
            if float(A[M][0]) < float(A[i][0]):
                M = i
    if M != j:
        A[M], A[j] = A[j], A[M]



for i in A:
    print(format(float(i[0]), '.2f'), format(float(i[1]), '.3f'))
'''
Матпомощь

Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
При одинаковом весе сначала идет студент с большим ростом (тощий).

Формат входных данных
Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел (float) через пробел - рост в метрах и вес в килограммах одного студента.

Формат результата
Рост и вес (печатать рост с точностью до сантиметров, а вес - до граммов) по одному студенту на строку от первого студента в шеренге к последнему

Примеры
Входные данные
3
1.8 70
1.75 70
1.8 69.5

Результат работы
1.80 69.500
1.80 70.000            
1.75 70.000
'''