from random import randint

n=int(input('Введите какое кол-во элементов будет в первом списке :  '))
k=int(input('Введите какое кол-во элементов будет во втором списке :  '))

list_1 = {randint(1,10) for i in range(n)}
print(list_1)

list_2 = {randint(1,10) for i in range(k)}
print(list_2)

print(list_1.intersection(list_2))

