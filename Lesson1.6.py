a = int(input("Кол - во км. в 1ый день: "))
b = int(input("Цель пробежать, км: "))
while True:
    a = a * 1.1
    if a >= b:
        break
print("Через", int(a), "дней цель будет достигнута.")



