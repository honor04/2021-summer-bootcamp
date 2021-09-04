"""
Q1. We use a 2d list to represent a lake. The island is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).
Determine the perimeter of the island.

Input: [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]

Output: 16
explain:
    first row has 3 because the 1 at lake[0][1] has three faces connected to water and 1 face connect with lake[1][1].
    second row has 6 because both lake[1][0] and lake[1][2] has 3 faces connected to water and lake[1][1] doesn't connect to water.
    third row has 2 because lake[2][1] has 2 sides connected to water.
    last row has 5 because lake[3][0] has 3 sides and lake[3][1] has 2 sides connected to water.
"""

"""
Q2. Determine if a 9 x 9 Sudoku board is valid. 

Input: board = 
[
 ["8","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
Output: false

Explain:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""


