import random

num = [random.randint(1, 34) for _ in range(34)]

with open('numbers.txt', 'w') as fl:
    for i in num:
        print(i, file=fl)

