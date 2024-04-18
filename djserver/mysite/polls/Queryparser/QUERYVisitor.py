# Generated from QUERY.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QUERYParser import QUERYParser
else:
    from QUERYParser import QUERYParser

# This class defines a complete generic visitor for a parse tree produced by QUERYParser.

class QUERYVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QUERYParser#query.
    def visitQuery(self, ctx:QUERYParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#StrongConditional.
    def visitStrongConditional(self, ctx:QUERYParser.StrongConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#Or.
    def visitOr(self, ctx:QUERYParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#Negation.
    def visitNegation(self, ctx:QUERYParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#Var.
    def visitVar(self, ctx:QUERYParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#And.
    def visitAnd(self, ctx:QUERYParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QUERYParser#Paren.
    def visitParen(self, ctx:QUERYParser.ParenContext):
        return self.visitChildren(ctx)



del QUERYParser