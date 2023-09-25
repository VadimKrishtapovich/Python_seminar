# #n = 'sdf\'df'
# #print(n )

# print(5)

# """
# print(5, 8)
# print(5)
# print(5, 9)
# """


# # print(5, 8)  Ctrl+K CTRL+ C
# # print(5)
# # print(5, 9)

def count_min_flips(coins):
    head_count = coins.count('H')
    tail_count = coins.count('T')
    return min(head_count, tail_count)

n = int(input("Введите количество монеток: "))
coins = [input() for i in range(n)]

print("Минимальное количество переворотов монеток:", count_min_flips(coins))