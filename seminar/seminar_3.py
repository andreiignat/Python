
'''
Программа выводит количество одинаковых элементов 
'''
# list_1 = [1, 1, 1, 4, 5]
# k = 1
# count = 0

# for i in range(len(list_1)):
#     if k == list_1[i]:
#         count = count + 1

# print(count)

list_1 = [ (i,i) for i in range ( 1 , 101 ) if i % 2 == 0 ] #[(2,2),(4,4),..., (100, 100)]
print(list_1)