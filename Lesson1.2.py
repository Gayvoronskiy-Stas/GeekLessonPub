int_sec = int(input("Введите время в секундах:"))
mm = (int_sec // 60)
ss = (int_sec % 60)
h = (mm // 60)
mm1 = (mm % 60)
mm = (mm + mm1)

print (f"{h}h {mm}mm {ss}ss или {h}:{mm}:{ss} ")





