'''
1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.


*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
import random

N = int(input("Введите количество элементов списка: "))

def randnum(n):
    numbers = [random.randrange(1, 10, 1) for _ in range(n)]
    return numbers

nums = randnum(N)
print(nums)
res = 0
index = 0

while index < len(nums):
    if index % 2 != 0:
        res += nums[index]
    index += 1

print(res)



s = [2, 3, 5, 9, 3]
print(sum(s[1::2]))