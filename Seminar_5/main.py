# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# 0 1 2 3 4 5 6  7  8  9
# 0 1 1 2 3 5 8 13 21 34
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)

# n = int(input("Введите число: "))
# print(fib(n))


# """
#                         5
#             4                      3
#         3       2 -> 1          2->1   1->1
#     2->1      1  -> 1 

    
# """


# -------------------------------------------------------------------------------------------
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки
# на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


# n = int(input('Сколько оценок:  '))
# list1 = []
# for i in range(n):
#     x = int(input('x = '))
#     list1.append(x)

# maxx = max(list1)
# minn =  min(list1)

# for i in range(len(list1)):
#     if list1[i] == maxx:
#         list1[i] = minn
# print(list1)


# list1 = [int(input('x = ')) for i in range(int(input('Сколько оценок:  ')))]
# maxx = max(list1)
# minn =  min(list1)
# list1 = [minn if i == maxx else i for i in list1]
# print(list1)

# -----------------------------------------------------------------------------------------------------------------------------
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# Output: yes


# def prime(n):
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# n = int(input("Введите число: "))
# print(prime(n))

# ----------------------------------------------------------------------------------------------------------------------
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3
# 5 -> 1 2 3 4 5
# 5 4 3 2 1

# def f(n):
#     if n == 0:
#         return ''
#     x = int(input("x = "))
#     return f(n - 1) + str(x) + ' '


# n = int(input("Введите число: "))
# print(f(n))

# f(4)
# f(3) + 1
# f(2) + 2
# f(1) + 3
# f(0) + 4