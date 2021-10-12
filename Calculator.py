from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import sin, cos


class Calculator:

    # метод решения уравнений

    def solveEq(self, eq_left, eq_right):
        a, b, y, x = symbols('a b y x')
        left = parse_expr(eq_left)
        right = parse_expr(eq_right)
        return solve(Eq(left, right), x)

    def solveEqi(self, eq):
        a, b, y, x = symbols('a b y x')
        expr = parse_expr(eq)
        return solve(expr, x)

    def solveExp(self, exp):
        return parse_expr(exp)

    def separateEq(self, eq):
        return str(eq).split('=')
