# We start creating the board, it will be a list of 9 positions. It starts with all blanks ' '.
board = [' ' for x in range(10)]


def insert_letter(letter, pos):  # Insert etter (X or O) in given position.
    board[pos] = letter


def pos_is_free(pos):  # Boolean function, return True if the position on the board is available.
    return board[pos] == ' '


def print_board(board):  # It just make the prints to reflect a ta-te-ti board.
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#  s_winner funct get a board and a letter and checks if horizontal lines (7,8 and 9) or
#  (4,5 and 6) or ( 1,2 and 3) has the same letter (X or O) or if verticals lines (1,4 and 7) or
#  (2, 5 and 8) or (3, 6 and 9) has the same letter. And, also for diagonals (1, 5 and 9) or (2, 5 and 7)


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():  # It tries to set the letter X (player) to desired board position.
    run = True
    while run:  # Until run equals to True, ask the user for the position.
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:  # It handle the right type input and the right range of the user input (1 to 9)
            move = int(move)
            if move > 0 and move < 10:
                if pos_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, pick an available place!')
            else:
                print('Please, type a number within the range!')
        except:
            print('Please type a number!')


def machine_move():  # It tries the machine move. As its request, this point is deeper explained at the README file.
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = pick_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = pick_random(edges_open)

    return move


def pick_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    from random import randrange
    print('Ta-Te-Ti')
    print_board(board)

    player_turn = randrange(2)

    while not (is_board_full(board)):
        if player_turn == 0:
            if not (is_winner(board, 'O')):
                player_move()
                print_board(board)
            else:
                print('Sorry, O\'s won this time!')
                break

        player_turn = 0

        if not (is_winner(board, 'X')):
            move = machine_move()
            if not move == 0:
            #     print('Tie Game!')
            # else:
                insert_letter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                print_board(board)
        else:
            if not (is_winner(board, 'X')) and not (is_board_full(board)):
                print('Tie Game!')
                break
            else:
                print('X\'s won this time! Good Job!')
                break

    # if is_board_full(board):
    #     print('Tie Game!')

if __name__ == '__main__':
    main()
