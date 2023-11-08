
# nums = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []

# for i in nums:
#     if i % 2 == 0:
#         temp_tup = (i, i * i)
#         res.append((i, i ** 2))
    
# print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

nums = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, nums)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)