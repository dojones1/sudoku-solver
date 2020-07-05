from unittest import TestCase
from sudoku_solver.solver import SudokuSolver


class SolverTestCase(TestCase):

    solver = None

    def setUp(self):
        self.solver = SudokuSolver()

    def verify_solver_results(self, test_grid, exp_grid):
        print()
        print("Test Case")
        self.solver.setup(test_grid)  # Initialise the grid with test configuration
        solver_grid = self.solver.get_grid()
        print("-- Initial grid:")
        solver_grid.print_known()
        self.solver.apply_rules()     # Run the various rules

        solver_grid = self.solver.get_grid()
        print("-- Test Results:")
        solver_grid.print_known()
        solver_grid.print_poss_values()

        print("-- Discrepancies")
        # Confirm that the solved grid matches the expected value
        valid = True
        row_idx = 0
        for row in range(self.solver.nrows):
            for col in range(self.solver.ncols):
                exp_value = exp_grid[row][col]
                act_value = solver_grid.get_cell_value(row, col)


                if exp_value != act_value:
                    print("    {},{}: {} != {}".format(row, col, exp_value, act_value))
                    valid = False

        self.assertTrue(valid)
