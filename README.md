# Tic-Tac-Toe AI

Tic-tac-toe against a computer opponent that plays perfectly using minimax: it searches every possible continuation of the game, so it always wins or draws. Pygame provides the board.

Demo video: https://youtu.be/QfEb0bBzi2k

This is my solution to the Tic-Tac-Toe project in Harvard's CS50 Introduction to AI with Python. The course provides the Pygame interface (`runner.py`) and the font. I wrote the game logic and the AI in `tictactoe.py`: whose turn it is, legal moves, applying a move, win and draw detection, and minimax (`minimax`, with mutually recursive `maxval` and `minval`).

## Run it

```bash
pip install pygame
python runner.py
```

Choose to play as X or O, click a square to move, and press "Play Again" when the game ends.
