from random import randint

list_1 = []


def gen_list(num1, num2, num3):
    n = 0
    while n < num1:
        list_1.append(randint(num2, num3))
        n += 1


gen_list(int(input("num gen:")), int(input("num 2:")), int(input("num 3:")))
list_2 = [el for i, el in zip(list_1, list_1[1:]) if el > i]
print(list_1)
print(list_2)
