# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('введите число N: '))
for i in range(N+1):
    if 2 ** i <= N:
        print(2 ** i, end=' ')


