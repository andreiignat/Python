
from random import randint

list_1 = list(randint(1, 10) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)

a = int(input('Введите номер куста: '))
n = 0

if a == 1:
    n = list_1[0] + list_1[1] + list_1[-1] # для первого куста
elif a == len(list_1):
    n = list_1[-2] + list_1[-1] + list_1[0] # для последнего куста
else:
    n = list_1[a-1] + list_1[a-2] + list_1[a] 

print('максимальное количество ягод :',  n )