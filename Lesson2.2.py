b = "срез строки проверка"
a = b.split()
print(a)
print(a)
while True:
    qwe = input("Добавить данные?")
    if qwe == ("Y") or qwe == ('y'):
        a.insert(int(input('index?')), input('data str?'))
        print(a)
    else:
        break
print(a, '- Origin')
le = len(a)
i=0
i1=1
while i1 < le:
    a[i], a[i1] = a[i1], a[i]
    i = i + 2
    i1 = i1 + 2
print(a,'- Revers')