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
        insert_letter('X', 2)
        insert_letter('X', 4)
        self.assertIn('X', board)
        self.assertIn('X', board)

    def test_pos_is_free(self):
        self.assertTrue(pos_is_free(2))
        self.assertTrue(pos_is_free(4))

    def test_is_winner(self):
        self.assertTrue(is_winner([' ', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O'], 'X'))

    def test_pick_random(self):
        result = pick_random([1, 3])
        self.assertIn(result, [1, 2, 3])

    def test_is_board_full(self):
        self.assertTrue(is_board_full([' ', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O']))
        #self.assertTrue(is_board_full(['X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O']))
        self.assertFalse(is_board_full(['X', 'X', 'O', 'O', 'X', 'O', 'O', 'X', 'O']))


if __name__ == "__main__":
    unittest.main()
