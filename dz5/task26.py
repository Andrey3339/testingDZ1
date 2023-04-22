# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8 

def pw(a, b):
    if b == 1:
        return a
    return pw(a, b - 1) * a

a, b = input('введите число и степень числа: ').split()

print(f'A = {a}, B = {b} -> {pw(int(a), int(b))}')