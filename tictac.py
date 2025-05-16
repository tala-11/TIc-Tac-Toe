import random

board=[' ' for _ in range(10)]

def insert_letter(letter,pos):
    board[pos]=letter

def is_space_free(pos):
    return board[pos]==' '

def print_board():
    for row in [[1,2,3],[4,5,6],[7,8,9]]:
        print('   |   |')
        print(' '+ ' | '.join(board[i] for i in row))
        print('   |   |')
        if row!=[7,8,9]:
            print('-----------')

def is_winner(bo,le):
    win_conditions=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    return any(all(bo[i]==le for i in line) for line in win_conditions)

def player_move():
    while True:
        move=input('Select a position (1-9) to place an "X": ')
        if move.isdigit():
            move=int(move)
            if 1<=move<=9:
                if is_space_free(move):
                    insert_letter('X',move)
                    break
                else:
                    print('That space is already occupied.')
            else:
                print('Number out of range. Choose 1-9.')
        else:
            print('Please enter a number.')

def select_random(lst):
    return random.choice(lst)

def comp_move():
    possible_moves=[i for i in range(1,10) if is_space_free(i)]
    for letter in ['O','X']:
        for move in possible_moves:
            copy=board[:]
            copy[move]=letter
            if is_winner(copy,letter):
                return move
    for group in ([1,3,7,9],[5],[2,4,6,8]):
        open_group=[i for i in group if i in possible_moves]
        if open_group:
            return select_random(open_group)
    return 0

def is_board_full():
    return board.count(' ')==1

def main():
    print('Welcome to Tic Tac Toe!')
    print_board()
    while not is_board_full():
        if not is_winner(board,'O'):
            player_move()
            print_board()
        else:
            print('O wins! Try again.')
            break
        if not is_winner(board,'X'):
            move=comp_move()
            if move==0:
                print('Tie Game!')
            else:
                insert_letter('O',move)
                print(f'Computer placed an "O" in position {move}:')
                print_board()
        else:
            print('X wins! Good job!')
            break
    if is_board_full() and not is_winner(board,'X') and not is_winner(board,'O'):
        print('Tie Game!')

while True:
    board=[' ' for _ in range(10)]
    main()
    play_again=input('Do you want to play again? (Y/N): ').strip().lower()
    if play_again not in ['y','yes']:
        break
