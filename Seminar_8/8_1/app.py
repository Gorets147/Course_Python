numbers = '2 12 -4 77 -38 8'

# numbers = numbers.split(' ')
# numbers = list(map(int, numbers))
# result = []

# for i in numbers:
#     if (i >= 10 and i <= 99):
#         result.append(i)
#     elif (i >= -99 and i <= -10):
#         result.append(i)
    
# print(result)


print(list(filter(lambda x: (len(str(abs(x))) == 2), map(int, numbers.split(" ")))))