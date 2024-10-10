#!/usr/bin/env python3

import checkmate

enemy_pieces = ['q', 'r', 'b', 'n', 'p']

def is_in_check(board):

    # Find the position of the king
    king_position = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'K':
                king_position = (r, c)
                break
        if king_position:
            break

    if not king_position:
        return False  # No king found, cannot be in check


def is_king_in_check(king_pos, enemy_pieces):
    """
    Check if the King is in check.

    Parameters:
    king_pos (tuple): The position of the King (row, col).
    enemy_pieces (list): A list of tuples representing the positions of enemy pieces.

    Returns:
    None: Prints "Success" if the King is in check, otherwise "Fail".
    """
    
    king_row, king_col = king_pos
    
    # Possible moves that can attack the King (for simplicity)
    attacking_moves = [
        (king_row - 1, king_col),     # Up
        (king_row + 1, king_col),     # Down
        (king_row, king_col - 1),     # Left
        (king_row, king_col + 1),     # Right
        (king_row - 1, king_col - 1), # Up-Left
        (king_row - 1, king_col + 1), # Up-Right
        (king_row + 1, king_col - 1), # Down-Left
        (king_row + 1, king_col + 1)  # Down-Right
    ]
    

    for enemy in enemy_pieces:
        if enemy in attacking_moves:
            print("Success")
            return

    print("Fail")

def main():
    board = """\
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .\
"""
