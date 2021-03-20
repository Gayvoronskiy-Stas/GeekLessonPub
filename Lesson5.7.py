# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
dev_dict1 = {}  # Словарь с прибыльными компаниями
dev_dict0 = {}  # Словарь с убыточными компаниями
dev_dict3 = {}  # Словарь со значением средней прибыли
dev_list = []
with open("text_7.txt", 'r', encoding='utf-8') as txt7:
    for line in txt7:
        line = line.split()
        int_line = [int(i) for (i) in line[2:]]
        diff_line = int_line[0] - int_line[1]
        if diff_line > 0:
            dev_dict1[' '.join(line[:2])] = diff_line
        else:
            dev_dict0[' '.join(line[:2])] = diff_line
    dev_list.append(dev_dict1)
    dev_list.append(dev_dict0)
    dev_dict3['average_profit'] = sum(dev_dict1.values()) / dev_dict1.__len__()
    dev_list.append(dev_dict3)
    print(dev_list)
import json

with open('text7my.json', 'w', encoding='utf-8') as txt_json:
    json.dump(dev_list, txt_json)
