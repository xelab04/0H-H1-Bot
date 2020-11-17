# 0H-H1-Bot
Program to solve binary sudoku puzzles from the mobile game 0H H1

The game has a grid of size 4x4, 8x8, 10x10 and 12x12.
Each grid square has 3 states, red, blue, blank. The objective is to fill the grid and eliminate all the blank squares.

The rules are as follows:
  
  -There must not me 3 squares of the same colour next to each other, vertically or horizontally.
  
  -There must be the same number of red squares as blue squares in the columns and rows.
  
  -No 2 columns can be the same. The same applies to rows as well.
  
  
So, the bot will read from a text file and attempt to solve the grid using the logic above.
