from test.SolverTestCase import SolverTestCase


class TestGrid(SolverTestCase):
    def hello(self):
        pass

    def test_initial_state(self):
        test_grid = ['1--------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        soln_grid = test_grid
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_1(self):
        test_grid = ['12345678-',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        soln_grid = ['123456789',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_2(self):
        test_grid = ['---------',
                     '987-65432',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        soln_grid = ['---------',
                     '987165432',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_horizontal_rule_3_only_loc(self):
        test_grid = ['987-54--1',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '------6--',
                     '---------',
                     '-------6-',
                     '---------']
        soln_grid = ['987654--1',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '------6--',
                     '---------',
                     '-------6-',
                     '---------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_1(self):
        test_grid = ['1--------',
                     '2--------',
                     '3--------',
                     '4--------',
                     '5--------',
                     '6--------',
                     '7--------',
                     '8--------',
                     '---------']
        soln_grid = ['1--------',
                     '2--------',
                     '3--------',
                     '4--------',
                     '5--------',
                     '6--------',
                     '7--------',
                     '8--------',
                     '9--------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_2(self):
        test_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '---------',
                     '-6-------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        soln_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '-1-------',
                     '-6-------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_vertical_rule_3_only_loc(self):
        test_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '----4----',
                     '------4--',
                     '---------',
                     '-3-------',
                     '-2-------',
                     '-1-------']
        soln_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '----4----',
                     '------4--',
                     '-4-------',
                     '-3-------',
                     '-2-------',
                     '-1-------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_box_rule_1(self):
        test_grid = ['123------',
                     '456------',
                     '78-------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        soln_grid = ['123------',
                     '456------',
                     '789------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------',
                     '---------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_box_rule_2_only_loc(self):
        test_grid = ['-2-------',
                     '4-6--1---',
                     '789------',
                     '---------',
                     '---------',
                     '--1------',
                     '---------',
                     '---------',
                     '---------']
        soln_grid = ['12-------',
                     '4-6--1---',
                     '789------',
                     '---------',
                     '---------',
                     '--1------',
                     '---------',
                     '---------',
                     '---------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_vert_then_hor(self):
        test_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '9--765432',
                     '-6-------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        soln_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '918765432',
                     '-6-------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_hor_then_vert(self):
        test_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '9-8765432',
                     '---------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        soln_grid = ['-9-------',
                     '-8-------',
                     '-7-------',
                     '918765432',
                     '-6-------',
                     '-5-------',
                     '-4-------',
                     '-3-------',
                     '-2-------']
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200704(self):
        test_grid = ['1539---82',
                     '---3--5--',
                     '-9---5-1-',
                     '-42-5-7--',
                     '---4-6---',
                     '--1-3-46-',
                     '-3-8---5-',
                     '--8--2---',
                     '51---3248']
        soln_grid = ['153974682',
                     '726381594',
                     '894625317',
                     '642158739',
                     '375496821',
                     '981237465',
                     '237849156',
                     '468512973',
                     '519763248']
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200711_i(self):
        test_grid = ['71---63--',
                     '-932---56',
                     '-----1-9-',
                     '4--5--8--',
                     '--5-9-7--',
                     '--7--8--3',
                     '-6-1-----',
                     '54---392-',
                     '--14---35']
        soln_grid = ['712956384',
                     '893247156',
                     '654831297',
                     '436572819',
                     '185394762',
                     '927618543',
                     '369125478',
                     '548763921',
                     '271489635']
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200730_sa_h(self):
        test_grid = ['--6-81---',
                     '---9-4---',
                     '2-9---3--',
                     '-4---2-83',
                     '1-------6',
                     '76-4---9-',
                     '--8---5-9',
                     '---3-5---',
                     '---86-2--']
        soln_grid = ['436281975',
                     '857934621',
                     '219576348',
                     '945612783',
                     '182793456',
                     '763458192',
                     '328147569',
                     '694325817',
                     '571869234']
        self.verify_solver_results(test_grid, soln_grid)

    def test_real_solution_20200730_sa_m(self):
        test_grid = ['-1-3--2-5',
                     '964------',
                     '-5-6-1--8',
                     '7-8-6-9--',
                     '---1-9---',
                     '--9-8-5-6',
                     '4--9-7-5-',
                     '------847',
                     '3-6--8-2-']
        soln_grid = ['817394265',
                     '964825371',
                     '253671498',
                     '728563914',
                     '635149782',
                     '149782536',
                     '482917653',
                     '591236847',
                     '376458129']
        self.verify_solver_results(test_grid, soln_grid)
