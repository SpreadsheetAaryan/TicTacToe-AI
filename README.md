# Tic Tac Toe AI Game

This project implements a Tic Tac Toe game with an unbeatable AI opponent using the minimax algorithm. The AI player is designed to never lose, ensuring a challenging experience for users.

## Project Demo: https://youtu.be/QfEb0bBzi2k?si=Jao60LeBNOxes531

## Features

- **Gameplay**: Play against the computer AI or another player.
- **AI Opponent**: Implements a minimax algorithm to make optimal moves.
- **Winning Detection**: Detects and displays the winner or if the game ends in a tie.
- **Restart**: Allows players to restart the game after a win, loss, or tie.

## Process of Building

The game was developed in Python using the Pygame library for the graphical user interface. Key steps in the development process include:

1. **Initial Setup**: Defined constants for players (X and O) and an empty board state.
2. **Game Logic**: Implemented functions to determine the current player, possible moves, and updating the game board based on player actions.
3. **Winning Conditions**: Created functions to check for winning conditions across rows, columns, and diagonals.
4. **Minimax Algorithm**: Integrated the minimax algorithm to determine the optimal move for the AI player, ensuring it never loses.
5. **User Interface**: Developed a simple graphical interface using Pygame to display the game board, player turns, and game outcome.
6. **Game Loop**: Implemented a game loop to continuously update the display and handle user input until the game is over or restarted.

## How It Never Loses

The minimax algorithm is a recursive function that evaluates all possible future game states, assuming both players play optimally. It assigns scores to each possible move and chooses the move that maximizes its chances of winning or minimizing the opponent's chances of winning. This ensures that the AI player can either win or force a tie, never allowing the opponent to win.

## Usage

To play the game:

1. Run the Python script using a suitable environment with Pygame installed.
2. Choose whether to play as X or O.
3. Make your moves by clicking on the desired tile.
4. Watch the AI make its moves strategically.
5. The game declares the winner or if it's a tie.
6. Click "Play Again" to restart the game.
