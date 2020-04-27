s = input()
k = int(input())

if k >= 0:
    print(s*k)
else:
    k = -k
    if len(s)%k:
        print('NO SOLUTION')
    else:
        i = 0
        A = []
        L = len(s)
        if L%k or L == k:
            print('NO SOLUTION')
        else:
            l = int(L/k)
            while i < L:
                A.append(s[i:i+l])
                i += l
            #print(A)
            for i in range(k-1):
                if A[i] != A[i+1]:
                    print('NO SOLUTION')
                    break
            else:
                print(A[0])
'''
Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз). Например, третьей степенью строки abc является строка аbсаbсаbс.
Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.
Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.

Формат входных данных
На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k. Отрицательная степень означает взятие корня соответствующей степени.

Формат выходных данных
Вывести строку, являющуюуся ответом на задачу. Если такой строки нет, то нужно вывести 'NO SOLUTION' (без кавычек).

Примеры
Ввод 	    Вывод
abc         abcabcabc
3

Ввод 	    Вывод
abcdabcd    abcd
-2

Ввод 	    Вывод
abcd        NO SOLUTION
-4
'''