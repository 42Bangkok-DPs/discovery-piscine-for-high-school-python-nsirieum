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

    king_row, king_col = king_position

    # Check for threats from pawns
    if (king_row > 0 and king_col > 0 and board[king_row - 1][king_col - 1] == 'p'):
        return True
    if (king_row > 0 and king_col < 7 and board[king_row - 1][king_col + 1] == 'p'):
        return True

    # Check for threats from rooks and queens
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
        for step in range(1, 8):
            new_row = king_row + direction[0] * step
            new_col = king_col + direction[1] * step
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board[new_row][new_col]
                if piece in enemy_pieces:
                    if piece == 'q' or (piece == 'r' and (direction[0] == 0 or direction[1] == 0)):
                        return True
                    break
                if piece != '.':
                    break
    # Check for threats from bishops and queens
    for i in range(1, 8):
        if king_row - i >= 0 and king_col - i >= 0:
            if board[king_row - i][king_col - i] in ['b', 'q']:
                return True
            if board[king_row - i][king_col - i] != '.':
                break
    for i in range(1, 8):
        if king_row - i >= 0 and king_col + i < 8:
            if board[king_row - i][king_col + i] in ['b', 'q']:
                return True
            if board[king_row - i][king_col + i] != '.':
                break
    for i in range(1, 8):
        if king_row + i < 8 and king_col - i >= 0:
            if board[king_row + i][king_col - i] in ['b', 'q']:
                return True
            if board[king_row + i][king_col - i] != '.':
                break
    for i in range(1, 8):
        if king_row + i < 8 and king_col + i < 8:
            if board[king_row + i][king_col + i] in ['b', 'q']:
                return True
            if board[king_row + i][king_col + i] != '.':
                break

    # Check for threats from knights
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    for distance_r, distance_c in knight_moves:
        r, c = king_row + distance_r, king_col + distance_c
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == 'n':
            return True

    return False

def main():
    if len(checkmate) < 2:
        print("No files provided.")
        return
    

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
