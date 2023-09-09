'''
Программа выводит количество одинаковых элементов 
'''
list_1 = [1, 1, 1, 4, 5]
k = 1
count = 0

for i in range(len(list_1)):
    if k == list_1[i]:
        count = count + 1

print(count)