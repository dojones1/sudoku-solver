from .grid import Grid


class SudokuSolver:
    grid = None
    nrows = 9
    ncols = 9
    nbentos = 3
    bento_size = 3

    def __init__(self):
        self.grid = Grid(self.nrows, self.ncols)

    def setup(self, grid):
        # Confirm grid matches dimensions of the solution
        assert len(grid) == self.nrows
        for row in grid:
            assert len(row) == self.ncols

        for row_idx in range(self.nrows):
            for col_idx in range(self.ncols):
                value = grid[col_idx][row_idx]
                if value != '-':
                    self.grid.set_cell_value(col_idx, row_idx, value, False)
                col_idx += 1
            row_idx += 1
        print("---- Setup complete")

    def print(self):
        self.grid.print()

    def get_grid(self):
        return self.grid

    def is_grid_solved(self):
        grid = self.get_grid()
        for row_idx in range(self.nrows):
            for col_idx in range(self.ncols):
                value = grid.get_cell_value(row_idx, col_idx)
                if value == '-':
                    return False
        return True

    def apply_rules(self):
        print("-- Applying Rules:")
        num_no_change_runs = 0
        continue_loop = True
        while continue_loop:
            change_made = False
            # Rules to prevent repetition of visible numbers
            change_made |= self.apply_horizontal_rules()
            change_made |= self.apply_vertical_rules()
            change_made |= self.apply_bento_rules()

            # If the grid is solved then stop
            if self.is_grid_solved():
                continue_loop = False

            # If no further changes are being made, then the grid has stabilised - test case?
            if not change_made:
                num_no_change_runs += 1
            else:
                num_no_change_runs = 0

            if num_no_change_runs > 0:
                continue_loop = False

        pass


    def apply_horizontal_rules(self):
        print("---- Applying horizontal rule")
        # If a value has been observed in the row,
        # then it cannot be a possible value for other cells in that row

        change_made = False
        for row in range(self.nrows):
            change_made |= self.horizontal_rule_only_one_loc(row)
        return change_made

    def horizontal_rule_only_one_loc(self, row):
        # Check to see if there is only one location where a number could be.
        # Scan the row and count how many times each poss value has been observed
        opt_observations = {}
        opt_locations = {}
        change_made = False

        #self.grid.print_poss_values()
        # scan row to count observations made
        for col in range(self.ncols):
            cell = self.grid.get_cell(row,col)
            if cell.value == None:
                for opt in cell.poss_values:
                    if opt in opt_observations:
                        opt_observations[opt] += 1
                    else:
                        opt_observations[opt] = 1
                        opt_locations[opt] = (row, col)

        # Review observations to see if any have been observed only once
        for opt in opt_observations:
            if opt_observations[opt] == 1:
                (opt_row, opt_col) = opt_locations[opt]
                # This has only been seen once, so it must go in the recorded location
                self.grid.set_cell_value(opt_row, opt_col, opt, True)
                change_made |= True
                print("     {} {}: {} - Horizontal Rule - Only one loc".format(opt_row,
                                                                               opt_col,
                                                                               self.grid.get_cell_value(opt_row, opt_col)))

        return change_made


    def apply_vertical_rules(self):
        # If a value has been observed in that column,
        # then it cannot be a possible value for other cells in that column

        print("---- Applying vertical rules")
        change_made = False
        for col in range(self.ncols):
            change_made |= self.vertical_rule_only_one_loc(col)
        return change_made

    def vertical_rule_only_one_loc(self, col):
        # Check to see if there is only one location where a number could be.
        # Scan the column and count how many times each poss value has been observed
        opt_observations = {}
        opt_locations = {}
        change_made = False

        # scan column to count observations made
        for row in range(self.nrows):
            cell = self.grid.get_cell(row,col)
            if cell.value == None:
                for opt in cell.poss_values:
                    if opt in opt_observations:
                        opt_observations[opt] += 1
                    else:
                        opt_observations[opt] = 1
                        opt_locations[opt] = (row, col)

        # Review observations to see if any have been observed only once
        for opt in opt_observations:
            if opt_observations[opt] == 1:
                (opt_row, opt_col) = opt_locations[opt]
                # This has only been seen once, so it must go in the recorded location
                self.grid.set_cell_value(opt_row, opt_col, opt, True)
                change_made |= True
                print("     {} {}: {} - Vertical Rule - Only one loc".format(opt_row,
                                                                               opt_col,
                                                                               self.grid.get_cell_value(opt_row, opt_col)))

        return change_made

    def apply_bento_rules(self):
        print("---- Applying bento rules")
        # If a value has been seen in that box, then it cannot be a possible value for blanks in that box
        change_made = False
        for bento_row in range(self.nbentos):
            for bento_col in range(self.nbentos):
                change_made |= self.bento_rule_only_one_loc(bento_row, bento_col)
        return change_made
        pass

    def bento_rule_only_one_loc(self, bento_row, bento_col):
        # Check to see if there is only one location where a number could be.
        # Scan the column and count how many times each poss value has been observed
        opt_observations = {}
        opt_locations = {}
        change_made = False

        # Scan bento to count observations made
        for b_row in range(self.bento_size):
            for b_col in range(self.bento_size):
                row = bento_row * self.bento_size + b_row
                col = bento_col * self.bento_size + b_col
                cell = self.grid.get_cell(row, col)

                if cell.value == None:
                    for opt in cell.poss_values:
                        if opt in opt_observations:
                            opt_observations[opt] += 1
                        else:
                            opt_observations[opt] = 1
                            opt_locations[opt] = (row, col)

        # Review observations to see if any have been observed only once
        for opt in opt_observations:
            if opt_observations[opt] == 1:
                (opt_row, opt_col) = opt_locations[opt]
                # This has only been seen once, so it must go in the recorded location
                self.grid.set_cell_value(opt_row, opt_col, opt, True)
                change_made |= True
                print("     {} {}: {} Bento Rule - Only one loc".format(opt_row,
                                                                        opt_col,
                                                                        opt))

        return change_made