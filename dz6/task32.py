# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input('Введите количество элементов в списке: '))
ls = [randint(1, 20) for i in range(n)]
dmin, dmax = input('Введите диапазон значений через пробел - минимальное и максимальное: ').split()
dmin = int(dmin)
dmax = int(dmax)
def fil_num(el):
    if(el >= dmin and el <= dmax):
        return el
result = list(filter(fil_num, ls))
print("Исходный список: ", ls)
print("Отфильтрованный список: ", result)

