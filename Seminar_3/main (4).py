# list1 = []
# list1 = list()
# print(list1)
# list1.append(5)
# list1.append(4)
# list1.append(12)
# print(list1)
# for i in list1:
#     print(i)



# tuple1 = tuple()
# tuple1 = (1, 2, 3)
# print(tuple1)
# print(type(tuple1))



# set1 = set()
# set1 = {1, 5, 2, 3}
# print(set1)
# set1.add(4)
# print(set1)
# set1.add(5)
# print(set1)


# dict1 = {}
# dict1 = dict()
# dict1 = {'a': 'A', 'b': 'B', 'c': 'C'}
# print(dict1)
# # # print(dict1['b'])
# # dict1['e'] = 'E'
# # print(dict1)
# # dict1['a'] = 'M'
# # print(dict1)
# print(dict1.values())



# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# list1 =  [1, 1, 2, 0, -1, 3, 4, 4]

# 1
# n = int(input('Сколько эл-тов нужно ввести:  '))
# list1 = []
# for i in range(n):
#     x = int(input('x = '))
#     list1.append(x)
# print(list1)

# 2
# list1 = []
# for i in range(int(input('Сколько эл-тов нужно ввести:  '))):
#     list1.append(int(input('x = ')))
# print(list1)

# list1 =  [1, 1, 2, 0, -1, 3, 4, 4]
# print(list1)
# # print(len(set(list1)))
# list2 = []
# count = 0
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#         count += 1
# print(count)

# ----------------------------------------------------------------------------------------------------------------------
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# [1, 2, 3, 4, 5, 6]
# k = 3
# 4 5 6 1 2 3

# # Примечание: Пользователь может вводить значения списка или список задан изначально.
# list1 = [1, 2, 3, 4, 5]
# k = int(input('k = '))
# print(list1)

# k = k % len(list1)
# for i in range(k):
#     list1.insert(0, list1.pop(-1))
# print(list1)

# -------------------------------------------------------------------------------------------------------------------------------
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)

# Input: [5, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# list = [5, -1, 5, 2, 3]
# count = 0

# for i in range(1, len(list)):
#     if list[i] > list[i - 1]:
#         count += 1

# print(count)

# ------------------------------------------------------------------------------------------------------------------------
# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. Пользователь его не вводит

# list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# set1 = set()

# for d in list1:
#     for v in d.values():
#         set1.add(v)
# print(set1)

def find_indices_in_range(lst, min_number, max_number):
    indices = []
    for i, num in enumerate(lst):
        if min_number <= num <= max_number:
            indices.append(i)
    return indices

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

result = find_indices_in_range(list_1, min_number, max_number)
for index in result:
    print(index)




