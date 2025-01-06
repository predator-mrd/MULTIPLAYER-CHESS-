'''import pygame
import numpy as np
from typing import List, Tuple, Optional

# Define the Piece class
class Piece:
    def __init__(self, piece_type: str, color: str):
        self.type = piece_type
        self.color = color
        self.has_moved = False

    def get_valid_moves(self, board, current_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = current_pos
        moves = []

        # Pawn logic
        if self.type == 'P':  
            direction = 1 if self.color == 'black' else -1

            # Forward move
            if 0 <= row + direction < 8 and board[row + direction][col] == 0:
                moves.append((row + direction, col))
                if not self.has_moved and 0 <= row + 2 * direction < 8 and board[row + 2 * direction][col] == 0:
                    moves.append((row + 2 * direction, col))

            # Diagonal captures
            for c in [-1, 1]:
                if 0 <= row + direction < 8 and 0 <= col + c < 8:
                    target = board[row + direction][col + c]
                    if target != 0 and target.color != self.color:
                        moves.append((row + direction, col + c))

        # Other pieces logic (Rook, Bishop, Knight, King, Queen)
        elif self.type in ['R', 'Q']:  
            # Horizontal and vertical moves
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + direction[0], col + direction[1]
                while 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board[new_row][new_col]
                    if target == 0:
                        moves.append((new_row, new_col))
                    elif target.color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                    new_row += direction[0]
                    new_col += direction[1]

        if self.type in ['B', 'Q']:  
            # Diagonal moves
            for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_row, new_col = row + direction[0], col + direction[1]
                while 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board[new_row][new_col]
                    if target == 0:
                        moves.append((new_row, new_col))
                    elif target.color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                    new_row += direction[0]
                    new_col += direction[1]

        elif self.type == 'N':  
            # Knight moves
            knight_moves = [
                (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1)
            ]
            for move in knight_moves:
                new_row, new_col = row + move[0], col + move[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board[new_row][new_col]
                    if target == 0 or target.color != self.color:
                        moves.append((new_row, new_col))

        elif self.type == 'K':  
            # King moves
            king_moves = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)
            ]
            for move in king_moves:
                new_row, new_col = row + move[0], col + move[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board[new_row][new_col]
                    if target == 0 or target.color != self.color:
                        moves.append((new_row, new_col))

        return moves

# Define the ChessBoard class
class ChessBoard:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=object)
        self.selected_piece = None
        self.selected_pos = None
        self.current_player = 'white'
        self.valid_moves = []

    def initialize_board(self):
        piece_order = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            self.board[1][i] = Piece('P', 'black')
            self.board[6][i] = Piece('P', 'white')
            self.board[0][i] = Piece(piece_order[i], 'black')
            self.board[7][i] = Piece(piece_order[i], 'white')

# Define the Game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Python Chess")
        self.clock = pygame.time.Clock()
        self.board = ChessBoard()
        self.board.initialize_board()
        self.load_pieces()

    def load_pieces(self):
        self.piece_symbols = {
            ('P', 'white'): '♙', ('R', 'white'): '♖',
            ('N', 'white'): '♘', ('B', 'white'): '♗',
            ('Q', 'white'): '♕', ('K', 'white'): '♔',
            ('P', 'black'): '♟', ('R', 'black'): '♜',
            ('N', 'black'): '♞', ('B', 'black'): '♝',
            ('Q', 'black'): '♛', ('K', 'black'): '♚'
        }

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = (255, 206, 158) if (row + col) % 2 == 0 else (209, 139, 71)
                pygame.draw.rect(self.screen, color, (col * 100, row * 100, 100, 100))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_board()
            pygame.display.flip()
            self.clock.tick(30)

# Main game loop
if __name__ == "__main__":
    game = Game()
    game.run()'''






'''import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# Load piece images
PIECE_IMAGES = {}
PIECES = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
COLORS = ['w', 'b']  # w for white, b for black

for color in COLORS:
    for piece in PIECES:
        PIECE_IMAGES[f"{color}_{piece}"] = pygame.image.load(f"assets/{color}_{piece}.png")
        PIECE_IMAGES[f"{color}_{piece}"] = pygame.transform.scale(
            PIECE_IMAGES[f"{color}_{piece}"], (SQUARE_SIZE, SQUARE_SIZE)
        )

# Function to draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to set up pieces
def setup_pieces():
    board = [[None] * COLS for _ in range(ROWS)]

    # Pawns
    for col in range(COLS):
        board[1][col] = "b_pawn"
        board[6][col] = "w_pawn"

    # Rooks
    board[0][0] = board[0][7] = "b_rook"
    board[7][0] = board[7][7] = "w_rook"

    # Knights
    board[0][1] = board[0][6] = "b_knight"
    board[7][1] = board[7][6] = "w_knight"

    # Bishops
    board[0][2] = board[0][5] = "b_bishop"
    board[7][2] = board[7][5] = "w_bishop"

    # Queens
    board[0][3] = "b_queen"
    board[7][3] = "w_queen"

    # Kings
    board[0][4] = "b_king"
    board[7][4] = "w_king"

    return board

# Function to draw pieces
def draw_pieces(board):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                screen.blit(PIECE_IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()
    board = setup_pieces()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()
        draw_pieces(board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()'''













'''import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FONT_SIZE = SQUARE_SIZE // 2

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 215, 0)  # Gold for highlighting

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Chess")

# Font for text
font = pygame.font.Font(None, FONT_SIZE)

# Initial board setup
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Selected piece and its position
selected_piece = None
selected_pos = None


# Function to draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = GREEN if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # Highlight selected square
            if selected_pos == (row, col):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)


# Function to draw pieces
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                text_color = WHITE
                text = font.render(piece.upper(), True, text_color)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)


# Function to handle piece movement
def move_piece(start_pos, end_pos):
    global board
    piece = board[start_pos[0]][start_pos[1]]
    board[start_pos[0]][start_pos[1]] = None  # Remove piece from start
    board[end_pos[0]][end_pos[1]] = piece  # Place piece at destination


# Function to get board position from mouse click
def get_board_position(mouse_pos):
    x, y = mouse_pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = get_board_position(pygame.mouse.get_pos())
            if selected_piece:
                # Move piece to new position
                move_piece(selected_pos, pos)
                selected_piece = None
                selected_pos = None
            else:
                # Select a piece
                selected_pos = pos
                selected_piece = board[pos[0]][pos[1]]

    # Draw everything
    draw_board()
    draw_pieces()

    pygame.display.flip()

pygame.quit()
sys.exit()'''
























import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FONT_SIZE = SQUARE_SIZE // 2

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 215, 0)  # Gold for highlighting
VALID_MOVE_COLOR = (173, 216, 230)  # Light blue for valid moves

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Chess")

# Font for text
font = pygame.font.Font(None, FONT_SIZE)

# Initial board setup
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Game state variables
selected_piece = None
selected_pos = None
current_turn = 'white'  # Track whose turn it is
valid_moves = []  # Store valid moves for selected piece

def is_white_piece(piece):
    """Check if the piece is white (lowercase)"""
    return piece and piece.islower()

def is_black_piece(piece):
    """Check if the piece is black (uppercase)"""
    return piece and piece.isupper()

def get_piece_color(piece):
    """Get the color of a piece"""
    if piece is None:
        return None
    return 'white' if is_white_piece(piece) else 'black'

def is_valid_position(row, col):
    """Check if position is within board boundaries"""
    return 0 <= row < ROWS and 0 <= col < COLS

def get_valid_moves(pos, piece):
    """Get all valid moves for a piece"""
    row, col = pos
    moves = []
    piece_type = piece.lower()
    is_white = is_white_piece(piece)

    # Pawn movement
    if piece_type == 'p':
        direction = -1 if is_white else 1
        # Forward move
        if is_valid_position(row + direction, col) and board[row + direction][col] is None:
            moves.append((row + direction, col))
            # Initial two-square move
            if ((is_white and row == 6) or (not is_white and row == 1)) and \
               board[row + 2*direction][col] is None:
                moves.append((row + 2*direction, col))
        
        # Diagonal captures
        for c in [-1, 1]:
            if is_valid_position(row + direction, col + c):
                target = board[row + direction][col + c]
                if target and get_piece_color(target) != get_piece_color(piece):
                    moves.append((row + direction, col + c))

    # Rook movement
    elif piece_type == 'r':
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not is_valid_position(new_row, new_col):
                    break
                target = board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                elif get_piece_color(target) != get_piece_color(piece):
                    moves.append((new_row, new_col))
                    break
                else:
                    break

    # Knight movement
    elif piece_type == 'n':
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if is_valid_position(new_row, new_col):
                target = board[new_row][new_col]
                if target is None or get_piece_color(target) != get_piece_color(piece):
                    moves.append((new_row, new_col))

    # Bishop movement
    elif piece_type == 'b':
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not is_valid_position(new_row, new_col):
                    break
                target = board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                elif get_piece_color(target) != get_piece_color(piece):
                    moves.append((new_row, new_col))
                    break
                else:
                    break

    # Queen movement (combination of rook and bishop)
    elif piece_type == 'q':
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + dr*i, col + dc*i
                if not is_valid_position(new_row, new_col):
                    break
                target = board[new_row][new_col]
                if target is None:
                    moves.append((new_row, new_col))
                elif get_piece_color(target) != get_piece_color(piece):
                    moves.append((new_row, new_col))
                    break
                else:
                    break

    # King movement
    elif piece_type == 'k':
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_position(new_row, new_col):
                target = board[new_row][new_col]
                if target is None or get_piece_color(target) != get_piece_color(piece):
                    moves.append((new_row, new_col))

    return moves

def draw_board():
    """Draw the chess board"""
    for row in range(ROWS):
        for col in range(COLS):
            color = GREEN if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            # Highlight selected square
            if selected_pos == (row, col):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, 
                               (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
            
            # Highlight valid moves
            if (row, col) in valid_moves:
                pygame.draw.circle(screen, VALID_MOVE_COLOR, 
                                 (col * SQUARE_SIZE + SQUARE_SIZE//2, 
                                  row * SQUARE_SIZE + SQUARE_SIZE//2), 
                                 SQUARE_SIZE//4)

def draw_pieces():
    """Draw all pieces on the board"""
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                text_color = WHITE
                text = font.render(piece.upper(), True, text_color)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE//2, 
                                                row * SQUARE_SIZE + SQUARE_SIZE//2))
                screen.blit(text, text_rect)

def move_piece(start_pos, end_pos):
    """Move a piece if the move is valid"""
    global board, current_turn
    
    piece = board[start_pos[0]][start_pos[1]]
    
    # Check if it's the correct player's turn
    is_white_turn = current_turn == 'white'
    if (is_white_turn and not is_white_piece(piece)) or \
       (not is_white_turn and not is_black_piece(piece)):
        return False

    # Check if the move is valid
    if end_pos in valid_moves:
        board[start_pos[0]][start_pos[1]] = None
        board[end_pos[0]][end_pos[1]] = piece
        current_turn = 'black' if current_turn == 'white' else 'white'
        return True
    return False

def get_board_position(mouse_pos):
    """Convert mouse position to board coordinates"""
    x, y = mouse_pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = get_board_position(pygame.mouse.get_pos())
            
            if selected_piece:
                # Attempt to move piece
                if move_piece(selected_pos, pos):
                    selected_piece = None
                    selected_pos = None
                    valid_moves = []
                elif pos == selected_pos:
                    # Deselect if clicking the same piece
                    selected_piece = None
                    selected_pos = None
                    valid_moves = []
                else:
                    # Select new piece if it's the current player's piece
                    piece = board[pos[0]][pos[1]]
                    if piece:
                        if (current_turn == 'white' and is_white_piece(piece)) or \
                           (current_turn == 'black' and is_black_piece(piece)):
                            selected_pos = pos
                            selected_piece = piece
                            valid_moves = get_valid_moves(pos, piece)
            else:
                # Select piece
                piece = board[pos[0]][pos[1]]
                if piece:
                    if (current_turn == 'white' and is_white_piece(piece)) or \
                       (current_turn == 'black' and is_black_piece(piece)):
                        selected_pos = pos
                        selected_piece = piece
                        valid_moves = get_valid_moves(pos, piece)

    # Draw everything
    draw_board()
    draw_pieces()
    pygame.display.flip()

pygame.quit()
sys.exit() 