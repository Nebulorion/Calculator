from Calculator import Calculator

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

buttons = [
    '7', '8', '9', 'C',
    '4', '5', '6', 'Exit',
    '1', '2', '3', 'π',
    '*', '0', '/', 'sin',
    'cos', '(', ')', 'x',
    '+', '-', '=', '.'
]


class Interface:
    def __init__(self):
        self.eq = ""
        self.calculator = Calculator()
        self.root = Tk()
        self.root.title("Calculator")
        self.setButtons(self.root)
        self.calc_entry = Entry(self.root, width=33)
        self.calc_entry.grid(row=0, column=0, columnspan=3)

        self.root.mainloop()

    def checkTypeOfEq(self, eq):

        if 'x' in eq:
            # Уравнение вида ax+b=0(пользователь не вводит 0)
            if '=' == eq[len(eq) - 1] or '=' not in eq:
                return 'eq0'
            # простое уравнение вида ax+b=c
            return 'eq'

        # Простое выражение
        if 'x' not in eq:
            return 'exp'

    @staticmethod
    def setNewSymbolToEq(self, i):
        if i not in buttons:
            messagebox.showerror("Error!", "Enter a number or a function")
            return

        if i == "C":
            self.eq = ""
            self.calc_entry.delete(0, END)
            return
        if i == "Exit":
            self.root.after(1, self.root.destroy)
            return
        if i == "xⁿ":
            self.eq += "**"
            self.calc_entry.insert(END, "**")
            return
        if i == "=":
            if i in self.calc_entry.get():
                messagebox.showerror("Error!", "'=' is already in your EQ")
                return
        if i == ".":
            if i == self.calc_entry.get()[len(self.calc_entry.get()) - 1]:
                messagebox.showerror("Error!", "You can't place '.' here")
                return
        self.eq += i
        print(self.eq)
        self.calc_entry.insert(END, i)

    @staticmethod
    def solveEq(self):
        expression = self.calc_entry.get()
        type = self.checkTypeOfEq(expression)

        if type == 'eq':
            left = (self.calc_entry.get()).split('=')[0]
            right = (self.calc_entry.get()).split('=')[1]
            result = self.calculator.solveEq(left, right)
        elif type == 'eq0':
            result = self.calculator.solveEqi(str(expression).replace('=', ""))
        elif type == 'exp':
            result = self.calculator.solveExp(str(expression).replace('=', ""))
        self.eq = ""
        self.calc_entry.delete(0, END)
        self.calc_entry.insert(END, "Ответ: x = " + str(result))
        print(result)

    def setButtons(self, root):
        r = 1
        c = 0
        for i in buttons:
            cmd = lambda x=i: self.setNewSymbolToEq(self, x)
            ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1
        ttk.Button(root, text='SOLVE IT', command=lambda: self.solveEq(self), width=10).grid(row=0, column=3)
