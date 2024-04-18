
import z3

class Conditional:
    def __init__(self,consequence, antecedence, textRepresentation, weak):
        self.antecedence=antecedence
        self.consequence=consequence
        self.weak=weak
        self.textRepresentation = textRepresentation
        self.literals = self.setLiterals()

    def make_A_then_B(self):
        return z3.And(self.antecedence, self.consequence)

    def setLiterals(self):
        table = str.maketrans({a:" "for a in "(),;!|"})
        literals = str.translate(self.textRepresentation, table)
        self.literals = list(set(literals.split()))
        self.literals = [l for l in self.literals if l not in ['Top', 'Bottom']]
        return self.literals


    def make_A_then_not_B(self):
        return z3.And(self.antecedence, z3.Not(self.consequence))

    def make_B(self):
        return self.consequence

    def __str__(self):
        return self.textRepresentation

    def __repr__(self):
        return self.textRepresentation

