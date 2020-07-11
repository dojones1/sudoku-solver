from test.SolverTestCase import SolverTestCase


class TestGrid(SolverTestCase):
    def hello(self):
        pass

    def test_initial_state(self):
        test_grid = [['1','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = test_grid
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_1(self):
        test_grid = [['1','2','3','4','5','6','7','8','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['1','2','3','4','5','6','7','8','9'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_2(self):
        test_grid = [['-','-','-','-','-','-','-','-','-'],
                     ['9','8','7','-','6','5','4','3','2'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['-','-','-','-','-','-','-','-','-'],
                     ['9','8','7','1','6','5','4','3','2'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_3_only_loc(self):
        test_grid = [['9','8','7','-','5','4','-','-','1'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','6','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','6','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['9','8','7','6','5','4','-','-','1'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','6','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','6','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_1(self):
        test_grid = [['1','-','-','-','-','-','-','-','-'],
                     ['2','-','-','-','-','-','-','-','-'],
                     ['3','-','-','-','-','-','-','-','-'],
                     ['4','-','-','-','-','-','-','-','-'],
                     ['5','-','-','-','-','-','-','-','-'],
                     ['6','-','-','-','-','-','-','-','-'],
                     ['7','-','-','-','-','-','-','-','-'],
                     ['8','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['1','-','-','-','-','-','-','-','-'],
                     ['2','-','-','-','-','-','-','-','-'],
                     ['3','-','-','-','-','-','-','-','-'],
                     ['4','-','-','-','-','-','-','-','-'],
                     ['5','-','-','-','-','-','-','-','-'],
                     ['6','-','-','-','-','-','-','-','-'],
                     ['7','-','-','-','-','-','-','-','-'],
                     ['8','-','-','-','-','-','-','-','-'],
                     ['9','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_2(self):
        test_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','6','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        soln_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['-','1','-','-','-','-','-','-','-'],
                     ['-','6','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_3_only_loc(self):
        test_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['-','-','-','-','4','-','-','-','-'],
                     ['-','-','-','-','-','-','4','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-'],
                     ['-','1','-','-','-','-','-','-','-']]
        soln_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['-','-','-','-','4','-','-','-','-'],
                     ['-','-','-','-','-','-','4','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-'],
                     ['-','1','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_box_rule_1(self):
        test_grid = [['1','2','3','-','-','-','-','-','-'],
                     ['4','5','6','-','-','-','-','-','-'],
                     ['7','8','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['1','2','3','-','-','-','-','-','-'],
                     ['4','5','6','-','-','-','-','-','-'],
                     ['7','8','9','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_box_rule_2_only_loc(self):
        test_grid = [['-','2','-','-','-','-','-','-','-'],
                     ['4','-','6','-','-','1','-','-','-'],
                     ['7','8','9','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','1','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        soln_grid = [['1','2','-','-','-','-','-','-','-'],
                     ['4','-','6','-','-','1','-','-','-'],
                     ['7','8','9','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','1','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','-','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_vert_then_hor(self):
        test_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['9','-','-','7','6','5','4','3','2'],
                     ['-','6','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        soln_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['9','1','8','7','6','5','4','3','2'],
                     ['-','6','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_hor_then_vert(self):
        test_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['9','-','8','7','6','5','4','3','2'],
                     ['-','-','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        soln_grid = [['-','9','-','-','-','-','-','-','-'],
                     ['-','8','-','-','-','-','-','-','-'],
                     ['-','7','-','-','-','-','-','-','-'],
                     ['9','1','8','7','6','5','4','3','2'],
                     ['-','6','-','-','-','-','-','-','-'],
                     ['-','5','-','-','-','-','-','-','-'],
                     ['-','4','-','-','-','-','-','-','-'],
                     ['-','3','-','-','-','-','-','-','-'],
                     ['-','2','-','-','-','-','-','-','-']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200704(self):
        test_grid = [['1','5','3','9','-','-','-','8','2'],
                     ['-','-','-','3','-','-','5','-','-'],
                     ['-','9','-','-','-','5','-','1','-'],
                     ['-','4','2','-','5','-','7','-','-'],
                     ['-','-','-','4','-','6','-','-','-'],
                     ['-','-','1','-','3','-','4','6','-'],
                     ['-','3','-','8','-','-','-','5','-'],
                     ['-','-','8','-','-','2','-','-','-'],
                     ['5','1','-','-','-','3','2','4','8']]
        soln_grid = [['1','5','3','9','7','4','6','8','2'],
                     ['7','2','6','3','8','1','5','9','4'],
                     ['8','9','4','6','2','5','3','1','7'],
                     ['6','4','2','1','5','8','7','3','9'],
                     ['3','7','5','4','9','6','8','2','1'],
                     ['9','8','1','2','3','7','4','6','5'],
                     ['2','3','7','8','4','9','1','5','6'],
                     ['4','6','8','5','1','2','9','7','3'],
                     ['5','1','9','7','6','3','2','4','8']]
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200711_i(self):
        test_grid = [['7','1','-','-','-','6','3','-','-'],
                     ['-','9','3','2','-','-','-','5','6'],
                     ['-','-','-','-','-','1','-','9','-'],
                     ['4','-','-','5','-','-','8','-','-'],
                     ['-','-','5','-','9','-','7','-','-'],
                     ['-','-','7','-','-','8','-','-','3'],
                     ['-','6','-','1','-','-','-','-','-'],
                     ['5','4','-','-','-','3','9','2','-'],
                     ['-','-','1','4','-','-','-','3','5']]
        soln_grid = [['7','1','2','9','5','6','3','8','4'],
                     ['8','9','3','2','4','7','1','5','6'],
                     ['6','5','4','8','3','1','2','9','7'],
                     ['4','3','6','5','7','2','8','1','9'],
                     ['1','8','5','3','9','4','7','6','2'],
                     ['9','2','7','6','1','8','5','4','3'],
                     ['3','6','9','1','2','5','4','7','8'],
                     ['5','4','8','7','6','3','9','2','1'],
                     ['2','7','1','4','8','9','6','3','5']]
        self.verify_solver_results(test_grid, soln_grid)