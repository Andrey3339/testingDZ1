# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве 
# внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за
# один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

N, d1, d2 = input('введите количество кустов и диапазон возможного количества ягод на каждом кусте через пробел: ').split()
n = [randint(int(d1), int(d2)) for _ in range(int(N))]
print('Кусты с ягодами: ', end =' ')
print(n)
total = subtotal = sum(n[:3])  
ind = 1
for i in range(len(n)):
    if i == (len(n) - 2):
        subtotal = sum(n[-2:]) + n[0]
        if subtotal > total:
          total = subtotal
          ind = len(n) - 1
    if i == (len(n) - 1):
        subtotal = n[-1] + sum(n[:2])
        if subtotal > total:
          total = subtotal
          ind = 1
    if (i != (len(n) - 2)) and (i != (len(n) - 1)):
        subtotal = sum(n[i : i + 3])
        if subtotal > total:
            total = subtotal
            ind = i + 1
print(f'Максимальное количество ягод {total} будет перед {ind + 1} кустом, на котором {n[ind]} ягод')
