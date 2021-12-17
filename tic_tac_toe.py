# -*- coding: utf-8 -*-
import random

board = [[' ', '1', '2', '3'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-'],
         ['3', '-', '-', '-']]

for i in board:
    print(*i)

while True:

    while True:
        playerChoice = input("\nвведте поле через пробел (рядб столбец): ")
        playerWay = list(map(int, playerChoice.split(' ')))
        if board[playerWay[0]][playerWay[1]] == '-':
            board[playerWay[0]][playerWay[1]] = 'X'
            break
        else:
            print("\nПоле занято, попробуй еще раз.")

# ROWS
    if (board[1][1] == board[1][2] == 'O' and board[1][3] == '-') or (board[1][1] == board[1][2] == 'X' and board[1][3] == '-'):
        board[1][3] = 'O'
    elif (board[1][2] == board[1][3] == 'O' and board[1][1] == '-') or (board[1][2] == board[1][3] == 'X' and board[1][1] == '-'):
        board[1][1] = 'O'
    elif (board[1][1] == board[1][3] == 'O' and board[1][2] == '-') or (board[1][1] == board[1][3] == 'X' and board[1][2] == '-'):
        board[1][2] = 'O'

    elif (board[2][1] == board[2][2] == 'O' and board[2][3] == '-') or (board[2][1] == board[2][2] == 'X' and board[2][3] == '-'):
        board[2][3] = 'O'
    elif (board[2][2] == board[2][3] == 'O' and board[2][1] == '-') or (board[2][2] == board[2][3] == 'X' and board[2][1] == '-'):
        board[2][1] = 'O'
    elif (board[2][1] == board[2][3] == 'O' and board[2][2] == '-') or (board[2][1] == board[2][3] == 'X' and board[2][2] == '-'):
        board[2][2] = 'O'

    elif (board[3][1] == board[3][2] == 'O' and board[3][3] == '-') or (board[3][1] == board[3][2] == 'X' and board[3][3] == '-'):
        board[3][3] = 'O'
    elif (board[3][2] == board[3][3] == 'O' and board[3][1] == '-') or (board[3][2] == board[3][3] == 'X' and board[3][1] == '-'):
        board[3][1] = 'O'
    elif (board[3][1] == board[3][3] == 'O' and board[3][2] == '-') or (board[3][1] == board[3][3] == 'X' and board[3][2] == '-'):
        board[3][2] = 'O'

# COLUMNS
    elif (board[2][1] == board[3][1] == 'O' and board[1][1] == '-') or (board[2][1] == board[3][1] == 'X' and board[1][1] == '-'):
        board[1][1] = 'O'
    elif (board[1][1] == board[3][1] == 'O' and board[2][1] == '-') or (board[1][1] == board[3][1] == 'X' and board[2][1] == '-'):
        board[2][1] = 'O'
    elif (board[2][1] == board[1][1] == 'O' and board[3][1] == '-') or (board[2][1] == board[1][1] == 'X' and board[3][1] == '-'):
        board[3][1] = 'O'

    elif (board[2][2] == board[3][2] == 'O' and board[1][2] == '-') or (board[2][2] == board[3][2] == 'X' and board[1][2] == '-'):
        board[1][2] = 'O'
    elif (board[1][2] == board[3][2] == 'O' and board[2][2] == '-') or (board[1][2] == board[3][2] == 'X' and board[2][2] == '-'):
        board[2][2] = 'O'
    elif (board[2][2] == board[1][2] == 'O' and board[3][2] == '-') or (board[2][2] == board[1][2] == 'X' and board[3][2] == '-'):
        board[3][2] = 'O'

    elif (board[2][3] == board[3][3] == 'O' and board[1][3] == '-') or (board[2][3] == board[3][3] == 'X' and board[1][3] == '-'):
        board[1][3] = 'O'
    elif (board[1][3] == board[3][3] == 'O' and board[2][3] == '-') or (board[1][3] == board[3][3] == 'X' and board[2][3] == '-'):
        board[2][3] = 'O'
    elif (board[2][3] == board[1][3] == 'O' and board[3][3] == '-') or (board[2][3] == board[1][3] == 'X' and board[3][3] == '-'):
        board[3][3] = 'O'

# DIAGONALS
    elif (board[1][1] == board[2][2] == 'O' and board[3][3] == '-') or (board[1][1] == board[2][2] == 'X' and board[3][3] == '-'):
        board[3][3] = 'O'
    elif (board[2][2] == board[3][3] == 'O' and board[1][1] == '-') or (board[2][2] == board[3][3] == 'X' and board[1][1] == '-'):
        board[1][1] = 'O'
    elif (board[1][1] == board[3][3] == 'O' and board[2][2] == '-' or (board[1][1] == board[3][3] == 'X' and board[2][2] == '-')):
        board[2][2] = 'O'

    elif (board[1][3] == board[2][2] == 'O' and board[3][1] == '-') or (board[1][3] == board[2][2] == 'X' and board[3][1] == '-'):
        board[3][1] = 'O'
    elif (board[1][3] == board[3][1] == 'O' and board[2][2] == '-') or (board[1][3] == board[3][1] == 'X' and board[2][2] == '-'):
        board[2][2] = 'O'
    elif (board[2][2] == board[3][1] == 'O' and board[1][3] == '-') or (board[2][2] == board[3][1] == 'X' and board[1][3] == '-'):
        board[1][3] = 'O'

    else:
        a = 0
        for i in range(1, 4):
            for j in range(1, 4):
                if board[i][j] == '-':
                    a += 1
        if a == 0:
            print("Ничья")
            break

        while True:
            opprow = random.choice([1, 2, 3])
            oppcolumn = random.choice([1, 2, 3])
            if board[opprow][oppcolumn] == '-':
                board[opprow][oppcolumn] = 'O'
                break

    for i in board:
        print(*i)

# WINS
    if board[1][1] == board[1][2] == board[1][3] == 'X' or board[1][1] == board[1][2] == board[1][3] == 'O':
        print(board[1][1], " Победил")
        break
    elif board[2][1] == board[2][2] == board[2][3] == 'X' or board[2][1] == board[2][2] == board[2][3] == 'O':
        print(board[2][1], " Победил")
        break
    elif board[3][1] == board[3][2] == board[3][3] == 'X' or board[3][1] == board[3][2] == board[3][3] == 'O':
        print(board[3][1], " Победил")
        break

    elif board[1][1] == board[2][1] == board[3][1] == 'X' or board[1][1] == board[2][1] == board[3][1] == 'O':
        print(board[3][1], " Победил")
        break
    elif board[1][2] == board[2][2] == board[3][2] == 'X' or board[1][2] == board[2][2] == board[3][2] == 'O':
        print(board[3][2], " Победил")
        break
    elif board[1][3] == board[2][3] == board[3][3] == 'X' or board[1][3] == board[2][3] == board[3][3] == 'O':
        print(board[3][3], " Победил")
        break

    elif board[1][1] == board[2][2] == board[3][3] == 'X' or board[1][1] == board[2][2] == board[3][3] == 'O':
        print(board[3][3], " Победил")
        break

    elif board[1][3] == board[2][2] == board[3][1] == 'X' or board[1][3] == board[2][2] == board[3][1] == 'O':
        print(board[3][1], " Победил")
        break
