# comment

"""
comment
comment
"""

# ctrl + /
# ctrl + k -> ctrl -> c
# ctrl + k -> ctrl -> u

# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной 
# инструкцией if и циклами.

# Input:
# n = 700
# m = 750

# Output:
# 2

# n = 700
# m = 1400
# -> 2

# n = int(input('Введите число: '))
# m = int(input('Введите число: '))
# print(m // n + int(m % n > 0))


# 7 / 5 = 1,4
# 7 // 5 = 1 (ост 2) -> 1
# 7 % 5 = 1 (ост 2) -> 2

# -----------------------------------------------
# В некоторой школе решили набрать три новых 
# математических класса и оборудовать 
# кабинеты для них новыми партами. За каждой партой 
# может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт,
# которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32 (10 + 11 + 11)

# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# c = int(input('Введите число: '))

# print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)


# -----------------------------------------------------
# Вагоны в электричке пронумерованы натуральными числами,
#  начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, 
# а иногда – с «хвоста»; 
#  это зависит от того, в какую сторону едет электричка).
#  В каждом вагоне написан 
# его номер. Витя сел в i-й вагон от головы поезда и 
# обнаружил, что его вагон имеет 
# номер j. Он хочет определить, сколько всего вагонов 
# в электричке. Напишите программу, 
# которая будет это делать или сообщать, что без 
# дополнительной информации это сделать невозможно.

# Input: 3 4(ввод на разных строках)
# Output: 6


#  i = 3 ; j =  5
# -> 7
#  1  2  3  4  5  6  7 = i = 3
# -- -- -- -- -- -- --
#  7  6  5  4  3  2  1 = j = 5

# 4 4 !!!
# i = int(input('Введите число: '))
# j = int(input('Введите число: '))

# if i == j:
#     print('без дополнительной информации это решить 
# невозможно')
# else:
#     print(i + j - 1)

# ----------------------------------------------------
#  Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе 
# выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если
#  он кратен 400.

# Input: 2016
# Output: YES

# 2001 -> NO


# n = int(input('Введите число: '))
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('y')
# else:
#     print('n')

# n = input("Введите номер билета: ") # Пользователь вводит номер билета
# # left_sum = int(n[0]) + int(n[1]) + int(n[2]) # Считаем сумму первых трех цифр номера
# # right_sum = int(n[3]) + int(n[4]) + int(n[5]) # Считаем сумму последних трех цифр номера
# # if left_sum == right_sum: # Проверяем условие счастливости билета
# #     print("yes")
# # else:
# #     print("no")


