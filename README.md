Multiplayer Chess Game (Pygame)
Description
This is an interactive chess game built using Pygame that allows players to play chess on a virtual 8x8 board. The game supports:

Piece movement with proper validation based on chess rules.
Turn-based gameplay with alternating moves between players.
Highlighting of valid moves and selected pieces.
An intuitive graphical user interface (GUI) for easy interaction.
Features
Valid Move Calculation: Automatically highlights valid moves for each piece based on chess rules.
Turn-based Gameplay: Alternates between two players (white and black) with checks for valid moves.
Piece Highlighting: Allows users to select a piece and see its valid moves visually.
Basic Chess Logic: The game follows standard chess rules for piece movement, including pawns' initial two-square move and special moves like castling (not yet implemented, can be added).
Installation
To run the project locally, follow these steps:

Clone the repository:

git clone https://github.com/predator-mrd/MULTIPLAYER-CHESS-.git
Navigate into the project folder:

cd MULTIPLAYER-CHESS-
Install Pygame:

If you don't have Pygame installed, install it using pip:

pip install pygame
Run the game:

python chess_game.py
The game window will open, and you can start playing by clicking on the pieces to move them.

Usage
The game allows you to select a piece by clicking on it.
Valid moves will be highlighted in light blue.
After selecting a piece, click on one of the highlighted squares to move the piece.
The turn will alternate between white and black players.
If you click on a piece from the opposite side, the game will ignore the action.
Contributing
Feel free to fork the repository and make contributions. If you'd like to add new features or fix bugs, open a pull request.

To Do:
Add Castling, En Passant, and Pawn Promotion features.
Implement AI for playing against the computer.
Improve UI/UX with animations for piece movement and better visuals.
