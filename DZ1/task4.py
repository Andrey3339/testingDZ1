# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

N = int(input('Введите сколько журавликов сделали Петя, Катя и Сережа вместе: '))
arrPSK = [0, 5, 6, 7, 8, 9]
sPS = "журавлика"
sK = "журавлика"
sN = "журавлика"
if N % 6 != 0:
    if N == 1 or N % 10 == 1:
        sN = "журавлик"
    if N >= 5 and N <= 20 or N % 10 in arrPSK or N in range(12, 100000012, 100) or N == 111:
        sN = "журавликов"
    print(f'По условию задачи дети не могли сделать {N} {sN}.')
else:
    nPS = N // 6
    nK = 4 * N // 6
    if nPS == 1 or nPS % 10 == 1:
        sPS = "журавлик"
    if nPS >= 5 and nPS <= 20 or nPS % 10 in arrPSK or nPS in range(12, 100000012, 100) or nPS == 111:
        sPS = "журавликов"
    if nK % 10 == 1:
        sK = "журавлик"
    if nK >= 5 and nK <= 20 or nK % 10 in arrPSK or nK in range(12, 100000012, 100) or nK == 111:
        sK = "журавликов"
    print(f'Петя сделал {nPS} {sPS}, Катя сделала {nK} {sK}, Сережа сделал {nPS} {sPS}.')

