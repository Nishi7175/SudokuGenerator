import pygame

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):

        # Constructor for the SudokuGenerator class.

        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]

    def get_board(self):

        # Returns a 2D python list of numbers, which represents the board

        return self.board

    def print_board(self):

        # Displays the board to the console.

        for i in range(self.row_length):
            for j in range(self.row_length):
                print(self.board[i][j], end=" ")
            print()  # New line after each row

    def valid_in_row(self, row, num):

        # Returns a Boolean value & determines if num is contained in the given row of the board.

        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_col(self, col, num):

        # Returns a Boolean value & determines if num is contained in the given column of the board.

        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):

        # Returns a Boolean value & determines if num is contained in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2).

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):

        # Returns if it's valid to enter num at (row, col) in the board.
        # Get the starting row and column for the 3x3 box

        box_row = row - (row % 3)
        box_col = col - (col % 3)

        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(box_row, box_col, num))

    def fill_box(self, row_start, col_start):

        # Randomly fills in values in the 3x3 box from (row_start, col_start) to (row_start+2, col_start+2).

        import random
        numbers = list(range(1, 10))
        random.shuffle(numbers)

        index = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = numbers[index]
                index += 1

    def fill_diagonal(self):

        # Fills the three boxes along the main diagonal of the board.

        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_remaining(self):

        # Fills the remaining squares in the board.

        pass

    def fill_values(self):

        pass

    def remove_cells(self):

        import random
        cells_removed = 0
        while cells_removed < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_removed += 1


def generate_sudoku(size, removed):

    generator = SudokuGenerator(size, removed)
    generator.fill_values()  # This would call fill_diagonal and fill_remaining
    generator.remove_cells()
    return generator.get_board()