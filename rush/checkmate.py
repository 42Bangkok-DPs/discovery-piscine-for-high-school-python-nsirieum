#!/usr/bin/env python3
import sys 

# Define the chess pieces
WHITE_KING = 'K'
enemy_piece = ['q', 'r', 'b', 'n', 'p']  # Queen, Rook, Bishop, Knight, Pawn


#in check for WHITE_KING
def is_in_check(board, king_position):
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),   # Vertical and horizontal
        (-1, -1), (-1, 1), (1, -1), (1, 1)   # Diagonal
    ]
    
    for distance_x, distance_y in directions:
        x, y = king_position
        while 0 <= x < 8 and 0 <= y < 8:
            x += distance_x
            y += distance_y
            if 0 <= x < 8 and 0 <= y < 8:
                piece = board[y][x]
                if piece == 'K':
                    return True
                elif piece != '.':
                    break
    
    # Check for knights
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    for distance_x, distance_y in knight_moves:
        x, y = king_position[0] + distance_x, king_position[1] + distance_y
        if 0 <= x < 8 and 0 <= y < 8:
            if board[y][x] == 'n':
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

