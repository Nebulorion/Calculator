from interface import *
from Calculator import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.ui = Interface()
        self.calc = Calculator()

    # Проверка типа уравнения
    def test_CheckTypeOfEq_Interface(self):
        # пользователь не ввёл "="
        self.assertEqual(self.ui.checkTypeOfEq("4*x-2"), 'eq0')
        # пользователь ввёл "="
        self.assertEqual(self.ui.checkTypeOfEq("4*x-2=10"), 'eq')
        # пользователь ввёл простое выражение
        self.assertEqual(self.ui.checkTypeOfEq("4*2-10"), 'exp')

    def test_setNewSymbolToEq_Interface(self):
        self.ui.setNewSymbolToEq('1')
        self.assertEqual(self.ui.eq, '1')

        self.ui.setNewSymbolToEq('+')
        self.ui.setNewSymbolToEq('2')
        self.assertEqual(self.ui.eq, '1+2')

    def test_solveEq_Interface(self):
        self.ui.calc_entry.insert(END, '2*x+10')
        self.assertEqual(self.ui.solveEq(), [-5])

        self.ui.calc_entry.delete(0, END)
        self.ui.calc_entry.insert(END, '2*x+10=10')
        self.assertEqual(self.ui.solveEq(), [0])

        self.ui.calc_entry.delete(0, END)
        self.ui.calc_entry.insert(END, 'x**2+17*x-18=0')
        self.assertEqual(self.ui.solveEq(), [-18, 1])

    def test_solveEq_calc(self):
        self.assertEqual(self.calc.solveEq("2*x", "6"), [3])
        self.assertEqual(self.calc.solveEq("x**2+17*x-18", "0"), [-18, 1])

    def test_solveEqi_calc(self):
        self.assertEqual(self.calc.solveEqi("2*x"), [0])
        self.assertEqual(self.calc.solveEqi("x**2+17*x-18"), [-18, 1])

    def test_solveExp_calc(self):
        self.assertEqual(self.calc.solveExp("2+1"), 3)
        self.assertEqual(self.calc.solveExp("44-3*2"), 38)


if __name__ == '__main__':
    unittest.main()
