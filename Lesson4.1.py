from sys import argv


def script_1(a, b, c):
    ZP = (a * b) + c
    print('Заработная плата сотрудника составляет:', ZP, 'коп.')


try:
    Ch1, num1, num2, num3 = argv
except ValueError:
    num1 = num2 = num3 = 0

script_1(int(num1), int(num2), int(num3))
