# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    guess = int(input("Введите число: "))

    if i < 9:
        if guess == num:
            print("Вы угадали!")
            break
        elif guess < num:
            print("Загаданное число больше, попыток осталось:", 9-i)
        else:
            print("Загаданное число меньше, попыток осталось:", 9-i)
    else:
        print("Не угадали, загаданное число: ", num)
