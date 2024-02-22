import random

game_board= ['x'] + [i for i in range(1,9)]
random.shuffle(game_board)

x = game_board.index('x')

def row_move(n):
    num= game_board.index(n)
    x = game_board.index('x')
    game_board[x], game_board[num] = game_board[num], game_board[x]


def col_move(n):
    num= game_board.index(n)
    x = game_board.index('x')
    game_board[x], game_board[num] = game_board[num], game_board[x]

def win():
    return game_board == [1, 2, 3, 4, 5, 6, 7, 8, 'x'] or game_board == ['x', 1, 2, 3, 4, 5, 6, 7, 8]


def isIllegal(n):
    if n not in game_board:
        return True
    num = game_board.index(n)
    x = game_board.index('x')

    if x-num == 1 or num-x == 1 or num-x == 3 or x-num == 3:
        return False
    return True


def show_state():
    print(game_board[0], game_board[1], game_board[2])
    print(game_board[3], game_board[4], game_board[5])
    print(game_board[6], game_board[7], game_board[8])

def start():
    show_state()
    choice= int(input('which one you wanna move?'))
    if isIllegal(choice):
        print("you can't move that")
    else:
        choice_id= game_board.index(choice)
        if choice_id- x == 1 or x-choice_id==1:
            row_move(choice)
        else:
            col_move(choice)

while not win():
    start()
    if win():
        print('well done')
