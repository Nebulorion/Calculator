from Calculator import Calculator

from tkinter import *
from tkinter import ttk

buttons = [
    '7', '8', '9', '+', '*',
    '4', '5', '6', '-', '/',
    '1', '2', '3', '=', 'xⁿ',
    '0', '.', '±','C',
    'Exit', 'π', 'sin', 'cos',
    '(', ')', 'n!', '√2', 'x', 'y']


class Interface:
    def __init__(self):
        self.eq = ""
        self.calculator = Calculator()
        self.root = Tk()
        self.root.title("Calculator")
        self.setButtons(self.root)
        self.calc_entry = Entry(self.root, width=33)
        self.calc_entry.grid(row=0, column=0, columnspan=5)

        self.root.mainloop()

    @staticmethod
    def setNewSymbolToEq(self, i):
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
        self.eq += i
        print(self.eq)
        self.calc_entry.insert(END, i)

    @staticmethod
    def solveEq(self):

        left = self.eq.split('=')[0]
        right = self.eq.split('=')[1]
        result = self.calculator.solveEq(left, right)
        self.eq=""
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
            if c > 4:
                c = 0
                r += 1
        ttk.Button(root, text='SOLVE IT', command=lambda: self.solveEq(self), width=25).grid(row=1, column=c+1)

