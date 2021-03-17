a = [4, 8, 6, 2, 9, 3, 1]
print(a)
while True:
    qwe = input("Добавить данные[Y/N]?")
    if qwe == ("Y") or qwe == ('y'):
        a.append(int(input("введите целое натуральное число:")))
        a.sort(reverse=True)
        print(a)
    else:
        break