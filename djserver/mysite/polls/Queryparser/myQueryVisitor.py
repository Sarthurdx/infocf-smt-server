


from ..CKBparser.Conditional import Conditional

from antlr4 import *
from .QUERYLexer import QUERYLexer
from .QUERYParser import QUERYParser
from .QUERYVisitor import QUERYVisitor



from z3 import *



class myQueryVisitor(QUERYVisitor):



    def visitQuery(self, ctx):
        return {i:self.visit(c) for i,c in enumerate(ctx.conditional(),start=1)}

    def visitStrongConditional(self, ctx):
        consequent = self.visit(ctx.consequent)
        antecedent = self.visit(ctx.antecedent)

        return Conditional(consequent, antecedent, ctx.getText(), weak=True)

    def visitOr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return Or(left, right)

    def visitAnd(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return And(left, right)

    def visitNegation(self, ctx):
        return Not(self.visit(ctx.formula()))


    def visitParen(self, ctx):
        return self.visit(ctx.formula())
        

    def visitVar(self, ctx):
        v = ctx.atom.text
        if v == 'Top':
            return True
        if v == 'Bottom':
            return False
        return Bool(v)


