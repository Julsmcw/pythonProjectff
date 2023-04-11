error = 'Начнем заново!'
whole_numbers = input('Введите целые числа через пробел: ')
new_number = int(input('Новое число: '))

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in whole_numbers:
    print('\nНет пробелов! Введите числа как в условии')
    whole_numbers = input('Введите целые числа через пробел: ')
if not is_int(whole_numbers):
    print('\nЭто не числа, читаем условие!\n')
    print(error)
else:
    whole_numbers = whole_numbers.split()

list_whole_numbers = [int(item) for item in whole_numbers]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_whole_numbers = merge_sort(list_whole_numbers)

def qsort(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return qsort(array, element, left, middle - 1)
        else:
            return qsort(array, element, middle + 1, right)
    except IndexError:
        return 'Нужно ввести меньше число!'

print(f'Список по возрастанию: {list_whole_numbers}')

if not qsort(list_whole_numbers, new_number, 0, len(list_whole_numbers)):
    rI = min(list_whole_numbers, key=lambda x: (abs(x - new_number), x))
    ind = list_whole_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < new_number:
        print(f'''Нет этого элемента! 
Меньший элемент: {rI} с индексом: {ind}
Больший элемент: {list_whole_numbers[max_ind]} с индексом: {max_ind}''')
    elif min_ind < 0:
        print(f'''Нет этого элемента!
Больший элемент: {rI}, с индексом: {list_whole_numbers.index(rI)}
Меньшего элемента нет''')
    elif rI > new_number:
        print(f'''Нет этого элемента!
Больший элемент: {rI}, с индексом: {list_whole_numbers.index(rI)}
Меньший элемент: {list_whole_numbers[min_ind]} с индексом: {min_ind}''')
    elif list_whole_numbers.index(rI) == 0:
        print(f'Индекс элемента: {list_whole_numbers.index(rI)}')
else:
    print(f'Индекс элемента: {qsort(list_whole_numbers, new_number, 0, len(list_whole_numbers))}')