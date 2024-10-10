#!/usr/bin/env python3
import sys 

# Define the chess pieces
WHITE_KING = 'K'
enemy_piece = ['q', 'r', 'b', 'n', 'p']  # Queen, Rook, Bishop, Knight, Pawn


#in check for WHITE_KING
def load_board(filename):
    with open(filename, 'r') as file:
        board = [list(line.strip()) for line in file.readlines()]
    return board

def find_king(board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == WHITE_KING:
                return (row, col)
    return None

def is_in_check(board, king_position):
    king_row, king_col = king_position
    
        # Check for threats from rooks and queens
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
        for step in range(1, 8):
            new_row = king_row + direction[0] * step
            new_col = king_col + direction[1] * step
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board[new_row][new_col]
                if piece in enemy_piece:
                    if piece == 'q' or (piece == 'r' and (direction[0] == 0 or direction[1] == 0)):
                        return True
                    break
                if piece != '.':
                    break

    # Check for threats from bishops and queens
    for direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # diagonals
        for step in range(1, 8):
            new_row = king_row + direction[0] * step
            new_col = king_col + direction[1] * step
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board[new_row][new_col]
                if piece in enemy_piece:
                    if piece == 'q' or (piece == 'b' and (direction[0] != 0 and direction[1] != 0)):
                        return True
                    break
                if piece != '.':
                    break

    # Check for threats from knights
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for move in knight_moves:
        new_row = king_row + move[0]
        new_col = king_col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == 'n':
                return True

    # Check for threats from pawns
    pawn_attacks = [(-1, -1), (-1, 1)]
    for attack in pawn_attacks:
        new_row = king_row + attack[0]
        new_col = king_col + attack[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == 'p':
                return True

    return False

def read_board(file_path):
    with open(file_path, 'r') as file:
        board = [list(line.strip()) for line in file.readlines()]
    return board

def find_king(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == 'K':
                return (x, y)
    return None

def main(file_path):
    board = read_board(file_path)
    king_position = find_king(board)
    
    if king_position is None:
        print("No King found on the board.")
        return

    if is_in_check(board, king_position):
        print("The King is in check.")
    else:
        print("The King is not in check.")

def main():
    board = """\
........
........
........
........
........
........
........
........\
"""

if __name__ == "__main__":
    import checkmate
    if len(sys.argv) != 2:
        print("Usage: python check_king.py <board_file>")
    else:
        main(sys.argv[1])

