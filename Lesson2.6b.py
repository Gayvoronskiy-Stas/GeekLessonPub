n = 0
b = list()
z = list()
while True:
    n +=1
    m = str(n)
    a = "c" + m
    a = list()
    a.append(input("str"))
    a.insert(0, n)
    a2 = tuple(a)
    z.append(a2)
    if n == 4:
        break
print(z)
print(z.index[1])