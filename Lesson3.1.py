num_1 = int(input("Num1:"))
num_2 = int(input("Num2:"))
rou = int(input('Rounded to:'))
def div(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError as Err:
        print(Err)
    else:
        print(f'{num_1}/{num_2} = {result.__round__(rou)}')


div(num_1, num_2)
