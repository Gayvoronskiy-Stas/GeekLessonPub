# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("text_5.txt", 'w', encoding='utf-8') as num_w:
    num_wr = num_w.write(input('Введите числа через пробел:'))

with open("text_5.txt", 'r', encoding='utf-8') as num_r:
    num_str = num_r.read()
    num_spl = num_str.split()
    num_int = [int(i) for i in num_spl]
    print('сумма чисел =', sum(num_int))


