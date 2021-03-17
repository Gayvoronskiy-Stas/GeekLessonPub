c = "срез строки проверка"
a = c.split()
a.append("аппэнд")
a.append(50)
a.append(45)
a.extend('qwe')
a.insert(1, 2334.34)
a.insert(2, 12)
a.insert(1, "12")
a.append(True)
print(a)
print(len(a),"-length")
while True:
    n = int(input("index?"))
    if n >= (-13) and n <=(12):
        print(type(a[n]))
    else:
        break
print('Stop')