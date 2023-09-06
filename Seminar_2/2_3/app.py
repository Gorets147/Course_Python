'''
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
'''
import random

n = input("Введите количество арбузов: ")

def watermelon(n):
    melon = [random.randrange(1, 10, 1) for _ in range(n)]
    return melon

if n.isdigit() == True and int(n) > 1:
    n = int(n)
    melon = watermelon(n)
    maks = melon[0]
    min = melon[0]
    print(melon)
    for i in range(0, len(melon)):
        if melon[i] > maks:
            maks = melon[i]
        else:
            if melon[i] < min:
                min = melon[i]

print(f"min = {min}, max = {maks}")
            




