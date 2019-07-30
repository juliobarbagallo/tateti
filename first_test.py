#def test_answer():
#    assert func(3) == 5
import unittest

board = [' ' for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter

def pos_is_free(pos):
    return board[pos] == ' '


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
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


class TestFunctions(unittest.TestCase):

    def test_insert_letter(self):
        #self.assert(insert_letter('X', 1), )
        self.assertIn('X', insert_letter('X', 2))

    def test_pos_is_free(self):
        self.assertTrue(pos_is_free(2))

    def test_is_winner(self):
        self.assertTrue(is_winner([' ', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O'], 'X'))



    # def test_player_move(self):
    #     #assert player_move()
    #     self.as
    #
    # def machine_move():
    #     possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    #     move = 0
    #
    #     for let in ['O', 'X']:
    #         for i in possible_moves:
    #             board_copy = board[:]
    #             board_copy[i] = let
    #             if is_winner(board_copy, let):
    #                 move = i
    #                 return move
    #
    #     corners_open = []
    #     for i in possible_moves:
    #         if i in [1, 3, 7, 9]:
    #             corners_open.append(i)
    #
    #     if len(corners_open) > 0:
    #         move = pick_random(corners_open)
    #         return move
    #
    #     if 5 in possible_moves:
    #         move = 5
    #         return move
    #
    #     edges_open = []
    #     for i in possible_moves:
    #         if i in [2, 4, 6, 8]:
    #             edges_open.append(i)
    #
    #     if len(edges_open) > 0:
    #         move = pick_random(edges_open)
    #
    #     return move
    #
    # def test_machine_move():
    #     assert machine_move()



    def test_pick_random(self):
        list_test = pick_random([1, 3])
        self.assertIn(list_test, 2)



    def test_is_board_full(self):
        self.assertTrue(is_board_full([' ', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O']))


if __name__ == "__main__":
    unittest.main()