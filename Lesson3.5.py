while True:
    a = input('Введите строку чисел через продбел:')
    b = a.split()
    try:
        result = [int(i) for i in b]
    except Exception:
        print('вы ввели не число!')
        b.pop(-1)
        result = [int(i) for i in b]
        print(sum(result))
        break
    else:
        print(sum(result))
        print('Для выхода введите любое строковое значение(кроме int)!')
