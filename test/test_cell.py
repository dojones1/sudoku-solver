import random
from unittest import TestCase
from sudoku_solver.cell import Cell


class TestCell(TestCase):
    def test_init_state(self):
        cell = Cell()
        self.assertFalse(cell.is_solved())
        self.assertEqual(len(cell.poss_values), 9)
        self.assertEqual(cell.get_value(), '-')

    def test_cell_set_value(self):
        cell = Cell()
        cell.set('2', False)

        self.assertTrue(cell.is_solved())
        self.assertEqual(len(cell.poss_values), 1)
        self.assertEqual(cell.get_value(), '2')
        self.assertFalse(cell.get_calculated())

    def test_cell_remove_value(self):
        cell = Cell()
        cell.remove_poss_value('3')
        self.assertFalse(cell.is_solved())
        self.assertEqual(len(cell.poss_values), 8)
        self.assertEqual(cell.get_value(), '-')

    def test_cell_remove_all_cells(self):
        cell = Cell()
        values_to_remove = ['1', '2', '3', '4', '5', '6', '7', '8']
        random.shuffle(values_to_remove)

        poss_value_length = 9
        resolved = False

        while len(values_to_remove):
            self.assertFalse(resolved)
            self.assertFalse(cell.is_solved())
            self.assertEqual(len(cell.poss_values), poss_value_length)
            value_to_remove = values_to_remove[0]
            values_to_remove.remove(value_to_remove)
            poss_value_length -= 1
            resolved = cell.remove_poss_value(value_to_remove)

        self.assertTrue(resolved)
        self.assertTrue(cell.is_solved())
        self.assertEqual(len(cell.poss_values), 1)
        self.assertEqual(cell.get_value(), '9')
        self.assertTrue(cell.get_calculated())
