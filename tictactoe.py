board= ['-']*9

def ending():
    WIN_CONDITIONS= [board[0]==board[1]==board[2]!='-',
                 board[3]==board[4]==board[5]!='-',
                 board[6]==board[7]==board[8]!='-',
                 board[0]==board[3]==board[6]!='-',
                 board[1]==board[4]==board[7]!='-',
                 board[2]==board[5]==board[8]!='-',
                 board[0]==board[4]==board[8]!='-',
                 board[2]==board[4]==board[6]!='-']
    for i in WIN_CONDITIONS:
        if i:
            return 'winner'
        elif board.count('-')==0:
            return 'draw'
    return False

def turn():
    if board.count('-')%2 ==  1:
        return 'x'
    else:
        return 'o'

def choice(n):
    if n<1 or n>9:
        print("it's not valid")
    elif turn() == 'x':
        board[n-1]= 'x'
    elif turn() == 'o':
        board[n-1]= 'o'

def show_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    
show_board()
while ending() != 'winner' or ending() != 'draw':
    if ending() == 'winner':
        if board.count('x') > board.count('o'):
            print('x wins')
            break
        else:
            print('o wins')
            break
    elif ending() == 'draw':
        print('this was a draw')
        break
    else:
        user_choice= int(input('please choose the place'))
        choice(user_choice)
        show_board()

