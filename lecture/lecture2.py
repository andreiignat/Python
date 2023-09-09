
"""                   Заполняем список.
list_1 = [] 
for i in range(5):
    list_1.append(i)
    print(list_1)
"""

"""
Метод pop удаляет последний элемент из списка:

list_1 = [12, 7, -1, 21, 0] 
print(list_1.pop())# 0 
print(list_1)# [12, 7, -1, 21] 
print(list_1.pop())# 21 
print(list_1)# [12, 7, -1] 
print(list_1.pop())# -1 
print(list_1)# [12, 7]

"""

"""
Функция insert — указание индекса (позиции) и значения. 

list_1 = [12, 7, -1, 21, 0] 
print(list1.insert(2, 11)) 
print(list1)# [12, 7, 11, -1, 21, 0]

"""


"""
Срез списка Помните в конце первой лекции Вы прошли срезы строк? 
Также существует срез списка, давайте научимсяизменять наш список ● 
Отрицательное число в индексе — счёт с конца списка 


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(list_1[0]) # 1 
print(list_1[1]) # 2 
print(list_1[len(list_1)-1]) # 10 
print(list_1[-5]) # 6 
print(list_1[:]) # [1, 2, 3, 4,5, 6, 7, 8, 9, 10] 
print(list_1[:2]) # [1, 2] 
print(list_1[len(list_1)-2:]) #[9,10] 
print(list_1[2:9]) # [3, 4,5, 6, 7, 8, 9] 
print(list_1[6:-18]) # [] 
print(list_1[0:len(list_1):6]) # [1,7] 
print(list_1[::6]) # [1, 7]

"""

"""
dictionary = {}
dictionary = {'up' : '1', 'left' : '2'}
print(dictionary['up'])

"""



"""
Словари 💡 Словари—неупорядоченныеколлекциипроизвольныхобъектов с доступом по ключу. 
Вспискахвкачествеключаиспользуетсяиндексэлемента. 
Всловаредля определения элемента используется значение ключа (строка, число). 


dictionary = {} 
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓','right':'→'} 
print(dictionary['left']) # ← 
# типы ключей могут отличаться 
print(dictionary['up']) # ↑ 
# типы ключей могут отличаться 
dictionary['left'] = '⇐' 
print(dictionary['left'])# ⇐ 

 
for item in dictionary: # for (k,v) in dictionary.items(): 
    print('{}: {}'.format(item, dictionary[item])) # up: ↑ # down: ↓ # right: →


dictionary = {} 
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 

print (dictionary.items())
for (k,v) in dictionary.items():
    print(k,v)

"""
#Множества 💡 Множествасодержатвсебеуникальныеэлементы,необязательно упорядоченные. 
#Одномножествоможетсодержатьзначениялюбыхтипов.ЕслиуВасестьдва множества, 
#Выможете совершатьнаднимилюбые стандартныеоперации, например, объединение, пересечение и разность. 
#Давайте разберем их. 

#colors = {'red', 'green', 'blue'} 
#print(colors)# {'red', 'green', 'blue'} 
#colors.add('red') 
#print(colors) # {'red', 'green', 'blue'} 
#colors.add('gray') 
#print(colors) # {'red', 'green', 'blue','gray'} 
#colors.remove('red') 
#print(colors) # {'green', 'blue','gray'} 
#colors.remove('red')# KeyError: 'red' 
#colors.discard('red') # ok 
#print(colors)# {'green', 'blue','gray'} 
#colors.clear()# { } 
#print(colors)# set()


"""
Операции со множествами в Python 
a = {1, 2, 3, 5, 8} 
b = {2, 5, 8, 13, 21} 
c = a.copy() # c = {1, 2, 3, 5, 8} 
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 
i = a.intersection(b) # i = {8, 2, 5} 
dl = a.difference(b) # dl = {1, 3} 
dr = b.difference(a) # dr = {13, 21} 
q=a.union(b).difference(a.intersection(b))# {1, 21,3, 13}

"""

# генератор списка

# list_1 = [ (i,i) for i in range ( 1 , 101 ) if i % 2 == 0 ] #[(2,2),(4,4),..., (100, 100)]
# print(list_1)  