# Знакомство с Python

"""
 Задача №1. Решение в группах Семинар 1. 
 Ввод-вывод, операторы ветвления За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией 
 if и циклами. Input: n = 700 m = 750 Output: 2

a = int (input("сколько километров проезжает в день? "))
b = int (input("какое расстояние нужно проехать? "))
d = (b//-a)
print (f"Для того чтобы проехать {b} киллометров понадобится = {-d} день" )

"""


"""
Задача №3. 
Решение в группах В некоторой школе решили набрать три новых математических класса 
и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них. 

Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32


a = int (input("сколько учащихся в классе А "))
b = int (input("сколько учащихся в классе Б "))
c = int (input("сколько учащихся в классе В "))
print (((a + b + c) // -2) * -1)

"""



"""
Задача №7. Решение в группах Дано натуральное число. Требуется определить, 
является ли год с данным номером високосным. Если год является високосным, 
то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400. 

Input: 2016 Output: YES

a = int (input("введите год "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("yes")
else:
    print("no")
    
"""



"""                        Проверка счастливый билет или нет сумма первых 3 цифр и последних
n = 123456
a = str (n)
b = int (a[0]) + int (a[1]) + int (a[2])
c = int (a[3]) + int (a[4]) + int (a[5])

if b == c:
    print( "Это счастливый билет ")
else:
    print( "В следующий раз повезет ")

"""


"""                                      Деление шоколадки
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

"""

"""                            Сумма трех цифр

n = 123

res = 0
while n> 0:
    digit = n %10
    res +=digit
    n //=10
print (res)

"""



"""                 Сумма трех цифр еще один вариант
n= 123

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3

print (res)

"""