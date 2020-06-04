def bubble_sort(A):
    ''' Сортировка пузырьком:
    Алгоритм состоит из повторяющихся проходов по сортируемому массиву.
    За каждый проход элементы последовательно сравниваются попарно и, если порядок в паре неверный, выполняется обмен элементов.
    Проходы по массиву повторяются N-1 раз или до тех пор, пока на очередном проходе не окажется, что обмены больше не нужны, что означает — массив отсортирован.
    При каждом проходе алгоритма по внутреннему циклу, очередной наибольший элемент массива ставится на своё место в конце массива рядом с предыдущим «наибольшим элементом»,
    а наименьший элемент перемещается на одну позицию к началу массива («всплывает» до нужной позиции, как пузырёк в воде — отсюда и название алгоритма).  '''
    for i in range(len(A)):
        flag = False
        for j in range(1, len(A) - i):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                flag = True
        if not(flag):
            return A
    return A


def insertion_sort(A):
    ''' Сортировка вставками:
    1 Suppose there exists a function called Insert designed to insert a value into a sorted sequence at the beginning of an array.
    It operates by beginning at the end of the sequence and shifting each element one place to the right until a suitable position is found for the new element.
    The function has the side effect of overwriting the value stored immediately after the sorted sequence in the array.
    2 To perform an insertion sort, begin at the left-most element of the array and invoke Insert to insert each element encountered into its correct position.
    The ordered sequence into which the element is inserted is stored at the beginning of the array in the set of indices already examined.
    Each insertion overwrites a single value: the value being inserted. '''
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A


def selection_sort(A):
    ''' Сортировка методом выбора:
    1 находим номер минимального значения в текущем списке
    2 производим обмен этого значения со значением первой неотсортированной позиции (обмен не нужен, если минимальный элемент уже находится на данной позиции)
    3 теперь сортируем хвост списка, исключив из рассмотрения уже отсортированные элементы '''
    j = m = 0
    while j < len(A):
        for i in range(j, len(A)):
            if A[i] < A[m]:
                m = i
        A[j], A[m] = A[m], A[j]
        j += 1
        m = j
    return A
    '''
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                print(A)
    return A
    '''


def merge_sort(A):
    ''' Сортировка слиянием:
    1 Сортируемый массив разбивается на две части примерно одинакового размера;
    2 Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
    3 Два упорядоченных массива половинного размера соединяются в один. '''
    if len(A) <= 1:        
        return
    C = []
    m = len(A) // 2
    l = list(A[i] for i in range(0, m))
    r = list(A[i] for i in range(m, len(A)))
    merge_sort(l)
    merge_sort(r)
    C = merge(l, r)
    for i in range(len(C)):
        A[i] = C[i]
    return


def merge(A, B):
    C = []
    i = j = 0
    while i < len(A):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            if j == len(B):
                for x in range(i, len(A)):
                    C.append(A[x])
                break
    while j < len(B):
        C.append(B[j])
        j += 1
    return C


def quick_sorting(a):
    ''' Быстрая сортировка, сортировка Хоара:
    1 Выбрать элемент из массива. Назовём его опорным.
    2 Разбиение: перераспределение элементов в массиве таким образом, что элементы меньше опорного помещаются перед ним, а больше или равные после.
    3 Рекурсивно применить первые два шага к двум подмассивам слева и справа от опорного элемента. Рекурсия не применяется к массиву, в котором только один элемент или отсутствуют элементы. '''
    if len(a) <= 1:
        return(a)
    l = []
    r = []
    m = []
    for i in range(len(a)):
        if a[i] < a[0]:
            l.append(a[i])
        elif a[i] > a[0]:
            r.append(a[i])
        else:
            m.append(a[i])
    l = sorting(l)
    r = sorting(r)
    c = l+m+r
    a = c
    return a


A = [12,22,5,1,2,3,9,53,3245,54,2,800]
print(A)
merge_sort(A)
print('Сортировка методом выбора:', selection_sort(A))
print('Сортировка вставками:', insertion_sort(A))
print('Сортировка пузырьком:', bubble_sort(A))
print('Сортировка слиянием:', A)