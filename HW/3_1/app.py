"""
Требуется найти в массиве list_1 самый близкий по 
величине элемент к заданному числу k и вывести его.
"""

list_1 = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
k = 3

list_1.sort()
closet_num = list_1[0]
for i in list_1:
    if abs(i - k) < abs(closet_num - k):
        closet_num = i
    if i > k:
        break

print(closet_num)