from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class Calculator:

    # метод решения уравнений
    def solveEq(self, eq_left, eq_right):
        a, b, y, x = symbols('a b y x')
        left = parse_expr(eq_left)
        right = parse_expr(eq_right)
        return solve(Eq(left, right), x)

    @staticmethod
    def separateEq(eq):
        return str(eq).split('=')
