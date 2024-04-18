# Generated from QUERY.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QUERYParser import QUERYParser
else:
    from QUERYParser import QUERYParser

# This class defines a complete listener for a parse tree produced by QUERYParser.
class QUERYListener(ParseTreeListener):

    # Enter a parse tree produced by QUERYParser#query.
    def enterQuery(self, ctx:QUERYParser.QueryContext):
        pass

    # Exit a parse tree produced by QUERYParser#query.
    def exitQuery(self, ctx:QUERYParser.QueryContext):
        pass


    # Enter a parse tree produced by QUERYParser#StrongConditional.
    def enterStrongConditional(self, ctx:QUERYParser.StrongConditionalContext):
        pass

    # Exit a parse tree produced by QUERYParser#StrongConditional.
    def exitStrongConditional(self, ctx:QUERYParser.StrongConditionalContext):
        pass


    # Enter a parse tree produced by QUERYParser#Or.
    def enterOr(self, ctx:QUERYParser.OrContext):
        pass

    # Exit a parse tree produced by QUERYParser#Or.
    def exitOr(self, ctx:QUERYParser.OrContext):
        pass


    # Enter a parse tree produced by QUERYParser#Negation.
    def enterNegation(self, ctx:QUERYParser.NegationContext):
        pass

    # Exit a parse tree produced by QUERYParser#Negation.
    def exitNegation(self, ctx:QUERYParser.NegationContext):
        pass


    # Enter a parse tree produced by QUERYParser#Var.
    def enterVar(self, ctx:QUERYParser.VarContext):
        pass

    # Exit a parse tree produced by QUERYParser#Var.
    def exitVar(self, ctx:QUERYParser.VarContext):
        pass


    # Enter a parse tree produced by QUERYParser#And.
    def enterAnd(self, ctx:QUERYParser.AndContext):
        pass

    # Exit a parse tree produced by QUERYParser#And.
    def exitAnd(self, ctx:QUERYParser.AndContext):
        pass


    # Enter a parse tree produced by QUERYParser#Paren.
    def enterParen(self, ctx:QUERYParser.ParenContext):
        pass

    # Exit a parse tree produced by QUERYParser#Paren.
    def exitParen(self, ctx:QUERYParser.ParenContext):
        pass



del QUERYParser