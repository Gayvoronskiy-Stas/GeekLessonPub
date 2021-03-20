# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
with open ("num.txt", "r", encoding="UTF-8") as num_r:
    cont = num_r.read()
    print(cont)
    list_cont = cont.split()
    print(list_cont)
    list_cont.remove('One')
    list_cont.remove('Two')
    list_cont.remove('Three')
    list_cont.remove('Four')
    print(list_cont)
    list_cont.insert(0, 'Один')
    list_cont.insert(3, 'Два')
    list_cont.insert(6, 'Три')
    list_cont.insert(9, 'Четыре')
    print(list_cont)
    cont_ru = ' '.join(list_cont)
    print(cont_ru)
    with open("numRU.txt", "w", encoding="UTF-8") as num_wRU:
        num_wRU.write(cont_ru)


