# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

poem = list(input('Введите считалку Винни через пробел:  ').split())
print(poem)

def find_rhythm(poem: list):
    #vowels_letters = ['у','е','ы','а','о','э','я','и','ю']
    vowels_letters = 'уеыаоэяию'
    count = 0
    sum_vowels_in_phrase = set()
    parity = True
    for phrase in poem:
        for letter in phrase:
            #if letter in vowels_letters:
            #    count += 1
            count += letter in vowels_letters
        sum_vowels_in_phrase.add(count)    
        # if count % 2 != 0:
        #     parity = False
        count = 0
    #return parity
    return len(sum_vowels_in_phrase) <= 1

if find_rhythm(poem):
    print('Парам пам-пам')
else:   
    print('Пам парам')



