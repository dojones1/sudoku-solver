from .cell import Cell
from pprint import pprint


class Grid:
    nrows = 0
    ncols = 0
    bento_size = 3
    grid = []

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.grid = [[Cell() for _ in range(self.ncols)] for _ in range(self.nrows)]

    def get_cell(self, row, col):
        assert row < self.nrows
        assert col < self.ncols
        return self.grid[row][col]

    def get_cell_value(self, row, col):
        assert row < self.nrows
        assert col < self.ncols
        return self.grid[row][col].get_value()

    def get_grid(self):
        return self.grid

    def clean_up_cells(self, row, col, value):
        change_made = False

        if True:
            # remove value from possible options in the same row
            for test_col in range(self.ncols):
                cell = self.grid[row][test_col]
                if cell.value is None:
                    change_made |= self.remove_poss_cell_value(row, test_col, value)

            # remove value from possible options in the same column
            for test_row in range(self.nrows):
                if self.grid[test_row][col].value is None:
                    change_made |= self.remove_poss_cell_value(test_row, col, value)

            # remove value from possible options in the same bento
            bento_row = int(row / self.bento_size)
            bento_col = int(col / self.bento_size)
            for b_col in range(self.bento_size):
                for b_row in range(self.bento_size):
                    test_col = bento_col * self.bento_size + b_col
                    test_row = bento_row * self.bento_size + b_row
                    cell = self.grid[test_row][test_col]
                    try:
                        if cell.value is None:
                            change_made |= self.remove_poss_cell_value(test_row, test_col, value)
                    except TypeError:
                        pass
        return change_made

    def set_cell_value(self, row, col, value, calculated):
        assert row < self.nrows
        assert col < self.ncols
        self.grid[row][col].set(value, calculated)
        changed = self.clean_up_cells(row, col, value)
        return changed

    def remove_poss_cell_value(self, row, col, value):
        assert row < self.nrows
        assert col < self.ncols
        change_made = self.grid[row][col].remove_poss_value(value)
        if change_made:
            new_value = self.grid[row][col].get_value()
            print("     {} {} : {} ".format(row, col, new_value))
            self.clean_up_cells(row, col, new_value)
        return change_made

    def print_detail(self):
        pprint(self.grid)

    def print_known(self):
        print("     Known values")
        for row in range(self.nrows):
            print(end='     ')
            for col in range(self.ncols):
                print(self.grid[row][col].get_value(), end=" ")
            print()

    def print_poss_values(self):
        print("     Possible Values")
        for row in range(self.nrows):
            print(end='     ')
            for col in range(self.ncols):
                print(self.grid[row][col].get_poss_values(), end=" ")
            print()

    def print(self):
        self.print_known()
        self.print_poss_values()
