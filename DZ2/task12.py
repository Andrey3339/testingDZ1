# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


SP = input('Введите сумму и произведение (не более 1 млн) 2х чисел через пробел: ').split()
S = int(SP[0])
P = int(SP[1])
for i in range(S + 1):
    if i * (S - i) == P:
        print(f'Задуманные числа {i} и {S - i}')
    


