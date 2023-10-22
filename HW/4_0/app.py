"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
"""

def In_list(str):
    new_arr = []
    temp = ""
    for i in range(0, len(str)):
        if str[i] != " ":
            temp += str[i]
            if i == len(str) - 1:
                new_arr.append(temp)
        else:
            new_arr.append(temp)
            temp = ""
    return new_arr


var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
res = []
var2 = In_list(var2)
var3 = In_list(var3)

if int(var1[0]) > int(var1[2]):    
    for i in var3:
        if i != " ":
            for j in var2:
                if i == j:
                    res.append(i)
elif int(var1[0]) < int(var1[2]):
    for i in var2:
        if i != " ":
            for j in var3:
                if i == j:
                    res.append(i)
elif int(var1[0]) == int(var1[2]):
    for i in var2:
        if i != " ":
            for j in var3:
                if i == j:
                    res.append(i)

print(*res)
        
            






# print(" ".join(set(var2) & set(var3)))