with open("ch1text.txt", "w", encoding="UTF-8") as ch1:
    ch1.write('one two three\nfour five')
with open("ch1text.txt", "r", encoding="UTF-8") as ch2:
    n = 1
    while True:
        content = ch2.readline()
        print(content)
        cont_list = content.split()
        print(len(cont_list), 'слов(а) в строке №', n)
        n += 1
        if len(cont_list) == 0 :
            break

    # content2 = ch2.readline()
    # print(content2)
    # coun2 = content2.split()
    # print(coun2)
    # print(len(coun2))
    # content3 = ch2.readline()
    # print(content3)
    # coun3 = content3.split()
    # print(coun3)
    # print(len(coun3))
    # content4 = ch2.readline()
    # print(content4)
    # coun4 = content4.split()
    # print(coun4)
    # print(len(coun4))
