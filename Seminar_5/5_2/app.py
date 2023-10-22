"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""

z = int(input("Введите число: "))

def easy(z, x = 2):
    if z == 2 or x * x > z:
        return True
    elif z % x == 0:
        return False
    return easy(z, x + 1)

print(easy(z))



