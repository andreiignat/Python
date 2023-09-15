# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

n = int(input("Введите число элементов массива  "))
for i in range(n):
    list_1 = [randint(-5,10) for i in range(n)]
print(list_1)
max = 10
min = 6
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(f"индекс {i} = {list_1[i]}")