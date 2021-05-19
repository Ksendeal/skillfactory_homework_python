board = list(range(1, 10))

win_combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------------')


def make_choice(symbol):
    while True:
        value = input('Куда ставим' + symbol + '?')
        if not (value in '123456789'):
            print('Вы ввели неподходящее число, попробуйте еще раз!')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Ой,а эта клетка уже занята!')
            continue
        board[value - 1] = symbol
        break


def winner_check():
    for each in win_combos:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[1] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            make_choice('X')
        else:
            make_choice('O')
        if counter > 3:
            winner = winner_check()
            if winner:
                draw_board()
                print('Поздравляю! Сегодня победили', winner)
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ого! Сегодня у нас ничья!')
            break


game()
