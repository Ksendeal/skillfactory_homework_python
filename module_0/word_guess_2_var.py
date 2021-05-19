import numpy as np


def game_core(num):  # функция для отгадывания за минимальное к-во попыток
    low = 1  # низший предел
    high = 100  # высший предел
    count = 0  # счетчик попыток
    guess = np.random.randint(1, 101)
    while guess != num:
        guess = (low + high) // 2  # находим среднюю точку между нижним и высшим пределами
        count += 1
        if guess > num:  # каждый раз делим число пополам и узнаем в меньшую или большую сторону двигаться
            high = guess
        elif guess < num:
            low = guess + 1
    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
