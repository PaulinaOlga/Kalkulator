def board_print(board):
    print('\n'*100)
    pos = ['A','B','C']
    print('  1|2|3')
    for i in range(0,3):
        print(pos[i],end='|')
        for j in range(0,2):
            print(f'{board[j+i*3]}',end='|')
        print(f'{board[2+i*3]}')

def pos_decode(post):
    dec = 'WRONG'
    if len(post) == 2:
        if post[0] == 'B':
            dec = 3
        elif post[0] == 'C':
            dec = 6
        elif post[0] == 'A':
            dec = 0
        else:
            return "WRONG"
        if post[1].isdigit() and int(post[1]) in range(1,4):
            dec += int(post[1]) -1
        else:
            dec="WRONG"
    return dec


def user_move_decode(current_user):
    pos = 'WRONG'
    while not type(pos) == int:
        post = input(f'Please enter the postion you would like to put {current_user} on:')
        pos = pos_decode(post)
    return pos

def user_move(board,current_user):
    correct_move = False
    while not correct_move:
        pos = user_move_decode(current_user)
        if board[pos] == ' ':
            board[pos] = current_user
            correct_move = True
    return board

def board_check(board,range_to_check,i=0):
    return not board[range_to_check[0]+i] == ' ' and board[range_to_check[0]+i] == board[range_to_check[1]+i] and board[range_to_check[0]+i] == board[range_to_check[2]+i]


def check_end(board):
    range_h = range(0,4)
    range_v = range(0,9,3)
    range_a1 = [0,4,8]
    range_a2 = [2,4,6]
    for i in range(0,3):
        if board_check(board,range_h,i) or board_check(board,range_v,i): return True
    return  board_check(board,range_a1) or board_check(board,range_a2)


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
current_user = 'Y'
game = True
moves = 0

while game:
    if current_user == 'X':
        current_user = 'Y'
    else:
        current_user = 'X'
    board_print(board)
    board = user_move(board, current_user)
    game = not check_end(board)
    moves += 1
    if(moves == 9):
        break

if not game:
    board_print(board)
    print(f'User {current_user} Won!!!!!\n In {moves} moves')
else:
    print("No More moves")