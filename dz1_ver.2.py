# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Старое решение

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# for i in range(0, len(list)):
#     if (i % 2 != 0):
#         sum += list[i]
# print(f'Сумма нечетных элементов = {sum}')




# Новое решение

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = list(filter(lambda i: i % 2, list1))
print(sum(list1))
