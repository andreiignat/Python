from random import randint

list_1 = list(randint(1, 10) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort(list_1))