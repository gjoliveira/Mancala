# Mancala
Mancala game implementation using Minimax and Alpha Beta pruning



In this repository, you will have access to 2 Python files, the "main" file with the game implementation, and the "heuristics" file containing the 3 types of heuristics tested in the project.

The work requires the importation of the Python libraries "time," "random," and "sys."

////Compilation Instructions:

This is a Python script and does not need to be compiled. It can be executed directly.

////Execution Instructions:

	Save the code in a file with the ".py" extension.
	Open the terminal in the directory where the .py file was saved.
	Type "python filename.py" (without quotes) and press enter.

////Usage Instructions:

When running the program, the user will be prompted to choose one of 3 game modes through terminal input:

	(1) Player 1 vs Player 2
	(2) Player 1 vs AI
	(3) AI vs AI (with the option to choose the depths of the algorithms for both AI bots)
	(4) Exit
After choosing the game mode, various difficulty levels will appear, selected in the same way:

	a) Player 1 vs Player 2:
		(1) Easy (no stealing)
		(2) Hard (stealing)

	b) Player 1 vs AI:
		(1) Easy (no stealing)
		(2) Hard (stealing and medium Minimax depth limit)
		(3) Hardcore (stealing and high Minimax depth limit)

NOTES: For the Player 1 vs AI mode, a function has been added that asks Player 1 if they want a hint when losing by more than five points. In each game, the player has only 2 hints to use (function get_hint()).

The game is initiated, and the board is displayed on the screen. To make a move, type the number corresponding to the pit you want to move the stones from.
