'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

num = int(input("Введите десятичное число: "))
res = ""

while num > 1:
    temp = 0
    temp = num % 2
    if temp != 0:
        temp = "1"
    else:
        temp = "0"
    res = res + temp
    num //= 2
    if num == 1:
        res = res + "1"

print(res[::-1])