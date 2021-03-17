def my_func(x, y):
    exp_num = x ** y
    print(exp_num)


my_func(8, -1)


def my_func2(x, y):
    exp2 = 1
    for i in range(abs(y)):
        exp2 *=x
    if y>=0:
        return exp2
    else:
        return 1/exp2


print(my_func2(8, -1))
