'''
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
'''

import os
os.system('cls')

flag = False
count = 0
i = 1
res = 0

N = input("Введите натуральное положительное число: ")

if N.isdigit() == True and int(N) > 1:
    N = int(N)
    while res <= N:
        res += i
        i = res - i
        count += 1
        if i != N != res:
            flag = False
        else:
            flag = True
    if flag == True:
        print(f"Натуральное число {N} является числом фибоначи по счёту: {count}")
    else:
        print(f"Натуральное число {N} не является числом Фибоначчи")
else:
    print("Ошибка ввода данных: введите натуральное число положительное число >1.")




def fibonachi(num):
    a, b, i = 0, 1, 0
    while a <= num:
        if num == a:
            return i
        a = b
        b = a + b
        i += 1
    else:
        return (-1)

