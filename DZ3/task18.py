
# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X

#*Пример:*
#5
#    7 -2 3 5 1
#    6
#    -> 7

def task18():
    from random import randint
    N, d1, d2 = input('введите количество элементов в массиве и диапазон от и до через пробел: ').split()
    if int(d1) < int(d2):
        mas = [randint(int(d1), int(d2)) for _ in range(int(N))]
    else:
        mas = [randint(int(d2), int(d1)) for _ in range(int(N))]
    print(*mas)
    n  = int(input('Введите число, чтобы узнать ближайшее к нему в массиве: '))
    print(n)
    min = abs(n - max(mas))
    el = max(mas)
    # for i in range(len(mas)):
    #     if abs(n - mas[i]) < min:
    #         min = abs(n - mas[i])
    #         el = mas[i]
    for e in mas:
        if abs(n - e) < min:
            min = abs(n - e)
            el = e
    print(f'-> {el}')

task18()





