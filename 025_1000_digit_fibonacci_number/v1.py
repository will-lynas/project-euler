a = 0
b = 1

for i in range(9999):
    if len(str(a)) >= 1000:
        print(i)
        break
    a, b = b, a+b
