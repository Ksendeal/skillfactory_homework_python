import numpy as np


def game_core(num):  # функция для отгадывания за минимальное к-во попыток
    low = 1  # низший предел
    high = 100  # высший предел
    count = 0  # счетчик попыток
    guess = np.random.randint(1, 101)
    while guess != num:
        guess = (low + high) // 2  # находим среднюю точку между нижним и высшим пределами
        count += 1
        print('Может это...', guess)
        if guess > num:  # каждый раз делим число пополам и узнаем в меньшую или большую сторону двигаться
            high = guess
        elif guess < num:
            low = guess + 1
    print('Ого! Это - ', guess, '!',  'И мы отгадали число за', count, 'попытки(попыток).')


def game_launch():
    num = np.random.randint(1, 101)  # генирируем случайно число
    game_core(num)


game_launch() # запускаем нашу игру
