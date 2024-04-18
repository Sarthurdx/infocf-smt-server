# Generated from CKB.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CKBParser import CKBParser
else:
    from CKBParser import CKBParser

# This class defines a complete listener for a parse tree produced by CKBParser.
class CKBListener(ParseTreeListener):

    # Enter a parse tree produced by CKBParser#ckbs.
    def enterCkbs(self, ctx:CKBParser.CkbsContext):
        pass

    # Exit a parse tree produced by CKBParser#ckbs.
    def exitCkbs(self, ctx:CKBParser.CkbsContext):
        pass


    # Enter a parse tree produced by CKBParser#ckb.
    def enterCkb(self, ctx:CKBParser.CkbContext):
        pass

    # Exit a parse tree produced by CKBParser#ckb.
    def exitCkb(self, ctx:CKBParser.CkbContext):
        pass


    # Enter a parse tree produced by CKBParser#signature.
    def enterSignature(self, ctx:CKBParser.SignatureContext):
        pass

    # Exit a parse tree produced by CKBParser#signature.
    def exitSignature(self, ctx:CKBParser.SignatureContext):
        pass


    # Enter a parse tree produced by CKBParser#myid.
    def enterMyid(self, ctx:CKBParser.MyidContext):
        pass

    # Exit a parse tree produced by CKBParser#myid.
    def exitMyid(self, ctx:CKBParser.MyidContext):
        pass


    # Enter a parse tree produced by CKBParser#conditionals.
    def enterConditionals(self, ctx:CKBParser.ConditionalsContext):
        pass

    # Exit a parse tree produced by CKBParser#conditionals.
    def exitConditionals(self, ctx:CKBParser.ConditionalsContext):
        pass


    # Enter a parse tree produced by CKBParser#StrongConditional.
    def enterStrongConditional(self, ctx:CKBParser.StrongConditionalContext):
        pass

    # Exit a parse tree produced by CKBParser#StrongConditional.
    def exitStrongConditional(self, ctx:CKBParser.StrongConditionalContext):
        pass


    # Enter a parse tree produced by CKBParser#WeakConditional.
    def enterWeakConditional(self, ctx:CKBParser.WeakConditionalContext):
        pass

    # Exit a parse tree produced by CKBParser#WeakConditional.
    def exitWeakConditional(self, ctx:CKBParser.WeakConditionalContext):
        pass


    # Enter a parse tree produced by CKBParser#Or.
    def enterOr(self, ctx:CKBParser.OrContext):
        pass

    # Exit a parse tree produced by CKBParser#Or.
    def exitOr(self, ctx:CKBParser.OrContext):
        pass


    # Enter a parse tree produced by CKBParser#Negation.
    def enterNegation(self, ctx:CKBParser.NegationContext):
        pass

    # Exit a parse tree produced by CKBParser#Negation.
    def exitNegation(self, ctx:CKBParser.NegationContext):
        pass


    # Enter a parse tree produced by CKBParser#Var.
    def enterVar(self, ctx:CKBParser.VarContext):
        pass

    # Exit a parse tree produced by CKBParser#Var.
    def exitVar(self, ctx:CKBParser.VarContext):
        pass


    # Enter a parse tree produced by CKBParser#And.
    def enterAnd(self, ctx:CKBParser.AndContext):
        pass

    # Exit a parse tree produced by CKBParser#And.
    def exitAnd(self, ctx:CKBParser.AndContext):
        pass


    # Enter a parse tree produced by CKBParser#Paren.
    def enterParen(self, ctx:CKBParser.ParenContext):
        pass

    # Exit a parse tree produced by CKBParser#Paren.
    def exitParen(self, ctx:CKBParser.ParenContext):
        pass



del CKBParser