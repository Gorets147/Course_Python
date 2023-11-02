#Проверка на палиндром рекурсией

s = "123321"

def polindrom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return polindrom(s[1:-1])

print(polindrom(s))