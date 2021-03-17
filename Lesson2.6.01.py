n = 0
z = list()
while True:
    qwe = input("Добавить данные[Д/Н]?")
    if qwe == ("Д") or qwe == ('д'):
        d = dict()
        x = list()
        d.update({'Наименование:': (input("Наименование:"))})
        d.update({"Цена": float(input("Цена:"))})
        d.update({'Количество': int(input('Количество:'))})
        d.update({'Ед': input('Ед:')})
        n += 1
        x.insert(0, n)
        x.append(d)
        z.append(x)
    else:
        break
print(x)
print(z)