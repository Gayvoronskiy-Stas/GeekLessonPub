from itertools import count, cycle

for el in count(5, 2):
    if el > 100:
        break
    print(el)

n = 0
for i in cycle('QWERTY'):
    n += 1
    print(i)
    if n == 10:
        break
