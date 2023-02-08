# SIMPLE SUDOKU 5X5
#### Name: Luong An Khang; Country: Vietnam; City: Ho Chi Minh city;
#### Video Demo:  <https://youtu.be/ooFSAHVBuv0>
#### Note: Use pip install to install all dependencies
#### Description:
The project is created to create, solve and let user play a simplified version of 5x5 sudoku,
with the normal restriction on rows and columns only:
- Each row/ column must have all numbers from 1 to 5, with each number appears once only.

The project contains 15 functions:

1. greeting(): Display the greeting screen and ask users for mode.
2. mode_input(): Ask user for inputs, validate and return the validated inputs.
3. user_input(grid): Receive user input while playing, validate if empty, and return the co-ordinate as tuple.
4. check_correct(grid): Check if all the entered input is correct.
5. play(grid): Continuously ask the user input for the missing number until the entire grid is filled, and return whether the user has solved the sudoku.
6. congrat(): Print a dinosaur saying CONGRATULATIONS
7. initialize(grid): Initialize a grid of Sudoku answer. For this project, the function will start with a prefilled grid (position [i, j] is filled with value (i + j + 1) MOD 5 + 1), then randomly swaps rows and columns to ensure the rules are always obeyed.
8. swap_row(grid, a, b): Swap the row a and b in the grid.
9. swap_column(grid, a, b): Swap the column a and b in the grid.
10. check_none(grid): Return True if all of the elements are NOT empty set/ None.
11. main(): Displays the Sudoku grid filled with numbers at the end.
12. creator(): Removes certain cells from the grid's initialization, and ensures that the puzzle is solvable with 1 solution only.
13. checker(): Check all possible values that a cell could contain.
14. unique(): Locate the cell with a unique possible value linked to it.
15. solver(): Use checker() and unique() to find the cell with a unique solution, and try to solve the puzzle.