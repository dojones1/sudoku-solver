from unittest import TestCase
from sudoku_solver.grid import Grid


class TestGrid(TestCase):
    def test_initial_state(self):
        nrows = 3
        ncols = 5
        grid = Grid(nrows, ncols)

        for row in range(nrows):
            for col in range(ncols):
                cell = grid.get_cell(row, col)
                self.assertFalse(cell.is_solved())
                self.assertEqual(len(cell.poss_values), 9)
                self.assertIsNone(cell.value)

    def test_set_cell(self):
        nrows = 3
        ncols = 3
        grid = Grid(ncols, nrows)
        grid.set_cell_value(1, 2, '2', False)
        grid.print()

        cell = grid.get_cell(1, 2)

        self.assertTrue(cell.is_solved())
        self.assertEqual(len(cell.poss_values), 1)
        self.assertEqual(cell.value, '2')

        # Check that get_cell_value works for location that value is set
        cell_value = grid.get_cell_value(1,2)
        self.assertEqual(cell_value, '2')

        # Make sure that value is not set for other location - x,y reversed
        cell_value = grid.get_cell_value(2,1)
        self.assertEqual(cell_value, '-')