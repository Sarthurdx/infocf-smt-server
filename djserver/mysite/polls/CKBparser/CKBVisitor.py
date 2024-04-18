# Generated from CKB.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CKBParser import CKBParser
else:
    from CKBParser import CKBParser

# This class defines a complete generic visitor for a parse tree produced by CKBParser.

class CKBVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CKBParser#ckbs.
    def visitCkbs(self, ctx:CKBParser.CkbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#ckb.
    def visitCkb(self, ctx:CKBParser.CkbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#signature.
    def visitSignature(self, ctx:CKBParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#myid.
    def visitMyid(self, ctx:CKBParser.MyidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#conditionals.
    def visitConditionals(self, ctx:CKBParser.ConditionalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#StrongConditional.
    def visitStrongConditional(self, ctx:CKBParser.StrongConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#WeakConditional.
    def visitWeakConditional(self, ctx:CKBParser.WeakConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#Or.
    def visitOr(self, ctx:CKBParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#Negation.
    def visitNegation(self, ctx:CKBParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#Var.
    def visitVar(self, ctx:CKBParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#And.
    def visitAnd(self, ctx:CKBParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CKBParser#Paren.
    def visitParen(self, ctx:CKBParser.ParenContext):
        return self.visitChildren(ctx)



del CKBParser