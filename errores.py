
sets = {}
for i in range(1, 6):
    if i <= 2:
        sets[1] = i-1

c = {e: e-1 for e in range(1, 6)if e <= 2}

print(c)


try:
    f = 0
    print(10/0)
except ZeroDivisionError as error:
    print(error)
