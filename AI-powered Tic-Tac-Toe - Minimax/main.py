import sys
import pygame
from game import Game
from setup import SQUARE_SIZE


def main():
    # GAME OBJECT
    game = Game()
    board = game.board
    ai = game.algorithm

    # MAIN LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # G - change game mode
                if event.key == pygame.K_g:
                    game.change_game_mode()
                # R - rest
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.algorithm
                # 0 - random AI
                if event.key == pygame.K_0:
                    ai.level = 0
                # 1 - minimax AI
                if event.key == pygame.K_1:
                    ai.level = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE

                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.is_over():
                        game.running = False

        if game.game_mode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()
            # AI METHOD
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.is_over():
                game.running = False

        pygame.display.update()

main()

'''
https://www.youtube.com/watch?v=Bk9hlNZc6sE 
59:40
'''