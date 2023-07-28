# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint


def get_interval(lst, mini, maxi):
    res = [i for i, k in enumerate(lst) if mini <= k <= maxi]
    return res

k = [randint(-10, 20) for i in range(randint(5, 20))]
j = randint(-9, 5)
l = randint(5, 20)
print(k, j, l, sep="\n")
print(get_interval(k, j, l))
