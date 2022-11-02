'''
1. Fizz Buzz
Дано: Число, как целочисленное (int).
Задание:
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
Вы должны написать программу, которая принимает положительное целое число и возвращает сл. значения.
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.
Пример:
 x = 15, результат: "Fizz Buzz"
 x = 6, результат: "Fizz"
 x = 5, результат: "Buzz"
 x = 7, результат: "7"
'''


def fizz_buzz(num: int):
    res = ""

    if num % 3 == 0:
        res += "Fizz"

    if num % 5 == 0:
        res += "Buzz"

    if res:
        return res
    else:
        return str(num)

'''
2. Оценка числа
Дано: Число x.
Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
если x нечетное, то это "Плохо"
если x = [2, 5] и четное, то это "Неплохо"
если x = [6, 20] и четное, то это "Так себе"
если x > 20 и четное, то это "Отлично"
Пример:
 x = 15, результат: "Плохо"
 x = 4, результат: "Неплохо"
 x = 8, результат: "Так себе"
 x = 24, результат: "Отлично"
'''


def evaluate_number(num: int):
    BAD = "Плохо"
    NOT_BAD = "Неплохо"
    SO_SO = "Так себе"
    GREAT = "Отлично"

    if num % 2 == 1:
        return BAD
    elif 2 <= num <= 5:
        return NOT_BAD
    elif 6 <= num <= 20:
        return SO_SO
    elif num > 20:
        return GREAT

'''
3. Последовательность
Дано: Число N = [1-9].
Задание: нужно написать программу, которая выведет последовательность 123..N
Пример:
 N = 3, результат: 123
 N = 9, результат: 123456789
 x = 1, результат: 1
'''


def sequence(num: int):
    res = ""

    for i in range(1, num + 1):
        res += str(i)

    return res


'''
4. Секретное сообщение
"Где умный человек прячет лист? В лесу. Но что если леса нет? ... Он выращивает лес и прячет его там." -- Гилберт Кит Честертон
Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты? Вы можете использовать газету, 
чтобы рассказать кому-то свой секрет. 
Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора. 
Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы. 
Давайте найдем несколько таких секретных сообщений.
Дано: Дан кусок текста (str).
Задание: Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста. 
Подсказка: посмотрите внимательно на методы класса str.
Пример:
 текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
'''


def get_secret_message(msg: str):
    res = ""

    for i in range(0, len(msg)):
        if msg[i].isupper():
            res += msg[i]

    return res


'''
[Junior] 5. Три слова
Давайте научим наших роботов отличать слова от чисел.
Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв.
Дано: Строка со словами (str).
Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд.
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Примеры:
text = "Hello World hello", результат: True
text = "He is 123 man", результат: False
text = "1 2 3 4", результат: False
'''


def three_words_sequence(text: str):
    repition = 0
    arr = text.split()

    for i in arr:
        if i.isalpha():
            repition += 1
            if repition == 3:
                return True
        else:
            repition = 0

    return False


'''
[Junior+] 6. Мир захватили левши
На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей." Santrock, John W. (2008). 
Motor, Sensory, and Perceptual Development.
"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и 
неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"." Scientific American. 
www.scientificamerican.com
Один робот был занят простой задачей: объединить 
последовательность строк в одно выражение для создания инструкции по обходу корабля. 
Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
Дано: последовательность строк.
Задание: вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. 
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", 
даже если это часть другого слова. Все строки даны в нижнем регистре.
Примеры:
["left", "right", "left", "stop"], результат: "left,left,left,stop"
["bright aright", "ok"], результат: "bleft aleft,ok"
["enough", "jokes"], результат: "enough,jokes"
'''


def right_to_left(arr: list[str]):
    res = ""
    iter = 0

    for i in arr:
        res += i.replace("right", "left")
        if iter < len(arr) - 1:
            res += ","
        iter += 1

    return res


def main():
    print("FizzBuzz task:")
    print(fizz_buzz(6))
    print(fizz_buzz(45))
    print(fizz_buzz(10))
    print(fizz_buzz(4))
    print("---------------------------------")

    print("Evaluate number task:")
    print(evaluate_number(13))
    print(evaluate_number(2))
    print(evaluate_number(6))
    print(evaluate_number(22))
    print("---------------------------------")

    print("Sequence task:")
    print(sequence(1))
    print(sequence(4))
    print(sequence(9))
    print("---------------------------------")

    print("Secret message task:")
    print(get_secret_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    print("---------------------------------")

    print("Three words task:")
    print(three_words_sequence("Hello World hello"))
    print(three_words_sequence("He is 123 man"))
    print(three_words_sequence("1 2 3 4"))
    print("---------------------------------")

    print("Lefties have taken over the world task:")
    print(right_to_left(["left", "right", "left", "stop"]))
    print(right_to_left(["bright aright", "ok"]))
    print(right_to_left(["enough", "jokes"]))
    print("---------------------------------")

if __name__ == "__main__":
    main()
