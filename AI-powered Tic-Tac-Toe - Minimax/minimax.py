import copy
import random

class Minimax:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    # ---RANDOM---
    @staticmethod
    def random(board):
        empty_squares = board.get_empty_sqrs()
        random_position = random.randrange(0, len(empty_squares))

        return empty_squares[random_position]

    # ---MINIMAX---
    def minimax(self, board, maximizing):
        case = board.final_state()      # TERMINAL CASES
        if case == 1:       # PLAYER 1 WINS
            return 1, None
        if case == 2:       # PLAYER 2 WINS
            return -1, None
        elif board.is_full():        # DRAW
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                evaluation = self.minimax(temp_board, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_evaluation = 100
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                evaluation = self.minimax(temp_board, True)[0]
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    best_move = (row, col)

            return min_evaluation, best_move

    # ---MAIN EVALUATION---
    def eval(self, main_board):
        if self.level == 0:
            # RANDOM CHOICE
            evaluation = 'random'
            move = self.random(main_board)
        else:
            # MINIMAX ALGO CHOICE
            evaluation, move = self.minimax(main_board, False)
        print(f'AI has chosen to mark the square in position {move} with an evaluation of: {eval}')
        return move
