# Generated from CKBParser.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4\35\n\4\f\4\16\4 \13\4\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\7\6*\n\6\f\6\16\6-\13\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\bG\n\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\7\bO\n\b\f\b\16\bR\13\b\3\b\2\3\16\t\2\4\6\b\n\f")
        buf.write("\16\2\2\2T\2\21\3\2\2\2\4\25\3\2\2\2\6\30\3\2\2\2\b!\3")
        buf.write("\2\2\2\n#\3\2\2\2\f<\3\2\2\2\16F\3\2\2\2\20\22\5\4\3\2")
        buf.write("\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\3\3\2\2\2\25\26\5\6\4\2\26\27\5\n\6\2\27\5\3\2\2")
        buf.write("\2\30\31\7\3\2\2\31\36\5\b\5\2\32\33\7\r\2\2\33\35\5\b")
        buf.write("\5\2\34\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\7\3\2\2\2 \36\3\2\2\2!\"\7\5\2\2\"\t\3\2\2\2#")
        buf.write("$\7\4\2\2$%\7\5\2\2%&\7\n\2\2&+\5\f\7\2\'(\7\r\2\2(*\5")
        buf.write("\f\7\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2")
        buf.write("\2\2-+\3\2\2\2./\7\13\2\2/\13\3\2\2\2\60\61\7\b\2\2\61")
        buf.write("\62\5\16\b\2\62\63\7\f\2\2\63\64\5\16\b\2\64\65\7\t\2")
        buf.write("\2\65=\3\2\2\2\66\67\7\21\2\2\678\5\16\b\289\7\f\2\29")
        buf.write(":\5\16\b\2:;\7\20\2\2;=\3\2\2\2<\60\3\2\2\2<\66\3\2\2")
        buf.write("\2=\r\3\2\2\2>?\b\b\1\2?@\7\16\2\2@G\5\16\b\7AB\7\b\2")
        buf.write("\2BC\5\16\b\2CD\7\t\2\2DG\3\2\2\2EG\7\5\2\2F>\3\2\2\2")
        buf.write("FA\3\2\2\2FE\3\2\2\2GP\3\2\2\2HI\f\6\2\2IJ\7\r\2\2JO\5")
        buf.write("\16\b\7KL\f\5\2\2LM\7\17\2\2MO\5\16\b\6NH\3\2\2\2NK\3")
        buf.write("\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\17\3\2\2\2RP\3\2")
        buf.write("\2\2\t\23\36+<FNP")
        return buf.getvalue()


class CKBParser ( Parser ):

    grammarFileName = "CKBParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'signature'", "'conditionals'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'|'", "','", "'!'", "';'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "SIGNATURE", "CONDITIONALS", "ID", "NEWLINE", 
                      "WS", "LPAR", "RPAR", "LBRA", "RBRA", "SEP", "COMMA", 
                      "NOT", "OR", "RL", "LL" ]

    RULE_ckbs = 0
    RULE_ckb = 1
    RULE_signature = 2
    RULE_myid = 3
    RULE_conditionals = 4
    RULE_conditional = 5
    RULE_formula = 6

    ruleNames =  [ "ckbs", "ckb", "signature", "myid", "conditionals", "conditional", 
                   "formula" ]

    EOF = Token.EOF
    SIGNATURE=1
    CONDITIONALS=2
    ID=3
    NEWLINE=4
    WS=5
    LPAR=6
    RPAR=7
    LBRA=8
    RBRA=9
    SEP=10
    COMMA=11
    NOT=12
    OR=13
    RL=14
    LL=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CkbsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ckb(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.CkbContext)
            else:
                return self.getTypedRuleContext(CKBParser.CkbContext,i)


        def getRuleIndex(self):
            return CKBParser.RULE_ckbs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCkbs" ):
                listener.enterCkbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCkbs" ):
                listener.exitCkbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCkbs" ):
                return visitor.visitCkbs(self)
            else:
                return visitor.visitChildren(self)




    def ckbs(self):

        localctx = CKBParser.CkbsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ckbs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.ckb()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CKBParser.SIGNATURE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CkbContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signature(self):
            return self.getTypedRuleContext(CKBParser.SignatureContext,0)


        def conditionals(self):
            return self.getTypedRuleContext(CKBParser.ConditionalsContext,0)


        def getRuleIndex(self):
            return CKBParser.RULE_ckb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCkb" ):
                listener.enterCkb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCkb" ):
                listener.exitCkb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCkb" ):
                return visitor.visitCkb(self)
            else:
                return visitor.visitChildren(self)




    def ckb(self):

        localctx = CKBParser.CkbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ckb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.signature()
            self.state = 20
            self.conditionals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNATURE(self):
            return self.getToken(CKBParser.SIGNATURE, 0)

        def myid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.MyidContext)
            else:
                return self.getTypedRuleContext(CKBParser.MyidContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CKBParser.COMMA)
            else:
                return self.getToken(CKBParser.COMMA, i)

        def getRuleIndex(self):
            return CKBParser.RULE_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignature" ):
                listener.enterSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignature" ):
                listener.exitSignature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignature" ):
                return visitor.visitSignature(self)
            else:
                return visitor.visitChildren(self)




    def signature(self):

        localctx = CKBParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_signature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(CKBParser.SIGNATURE)
            self.state = 23
            self.myid()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CKBParser.COMMA:
                self.state = 24
                self.match(CKBParser.COMMA)
                self.state = 25
                self.myid()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MyidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.num = None # Token

        def ID(self):
            return self.getToken(CKBParser.ID, 0)

        def getRuleIndex(self):
            return CKBParser.RULE_myid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMyid" ):
                listener.enterMyid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMyid" ):
                listener.exitMyid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMyid" ):
                return visitor.visitMyid(self)
            else:
                return visitor.visitChildren(self)




    def myid(self):

        localctx = CKBParser.MyidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_myid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            localctx.num = self.match(CKBParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def CONDITIONALS(self):
            return self.getToken(CKBParser.CONDITIONALS, 0)

        def LBRA(self):
            return self.getToken(CKBParser.LBRA, 0)

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(CKBParser.ConditionalContext,i)


        def RBRA(self):
            return self.getToken(CKBParser.RBRA, 0)

        def ID(self):
            return self.getToken(CKBParser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CKBParser.COMMA)
            else:
                return self.getToken(CKBParser.COMMA, i)

        def getRuleIndex(self):
            return CKBParser.RULE_conditionals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionals" ):
                listener.enterConditionals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionals" ):
                listener.exitConditionals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionals" ):
                return visitor.visitConditionals(self)
            else:
                return visitor.visitChildren(self)




    def conditionals(self):

        localctx = CKBParser.ConditionalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(CKBParser.CONDITIONALS)
            self.state = 34
            localctx.name = self.match(CKBParser.ID)
            self.state = 35
            self.match(CKBParser.LBRA)
            self.state = 36
            self.conditional()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CKBParser.COMMA:
                self.state = 37
                self.match(CKBParser.COMMA)
                self.state = 38
                self.conditional()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(CKBParser.RBRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CKBParser.RULE_conditional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrongConditionalContext(ConditionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.ConditionalContext
            super().__init__(parser)
            self.consequent = None # FormulaContext
            self.antecedent = None # FormulaContext
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(CKBParser.LPAR, 0)
        def SEP(self):
            return self.getToken(CKBParser.SEP, 0)
        def RPAR(self):
            return self.getToken(CKBParser.RPAR, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.FormulaContext)
            else:
                return self.getTypedRuleContext(CKBParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrongConditional" ):
                listener.enterStrongConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrongConditional" ):
                listener.exitStrongConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrongConditional" ):
                return visitor.visitStrongConditional(self)
            else:
                return visitor.visitChildren(self)


    class WeakConditionalContext(ConditionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.ConditionalContext
            super().__init__(parser)
            self.consequent = None # FormulaContext
            self.antecedent = None # FormulaContext
            self.copyFrom(ctx)

        def LL(self):
            return self.getToken(CKBParser.LL, 0)
        def SEP(self):
            return self.getToken(CKBParser.SEP, 0)
        def RL(self):
            return self.getToken(CKBParser.RL, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.FormulaContext)
            else:
                return self.getTypedRuleContext(CKBParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeakConditional" ):
                listener.enterWeakConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeakConditional" ):
                listener.exitWeakConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeakConditional" ):
                return visitor.visitWeakConditional(self)
            else:
                return visitor.visitChildren(self)



    def conditional(self):

        localctx = CKBParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditional)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CKBParser.LPAR]:
                localctx = CKBParser.StrongConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(CKBParser.LPAR)
                self.state = 47
                localctx.consequent = self.formula(0)
                self.state = 48
                self.match(CKBParser.SEP)
                self.state = 49
                localctx.antecedent = self.formula(0)
                self.state = 50
                self.match(CKBParser.RPAR)
                pass
            elif token in [CKBParser.LL]:
                localctx = CKBParser.WeakConditionalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(CKBParser.LL)
                self.state = 53
                localctx.consequent = self.formula(0)
                self.state = 54
                self.match(CKBParser.SEP)
                self.state = 55
                localctx.antecedent = self.formula(0)
                self.state = 56
                self.match(CKBParser.RL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CKBParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(CKBParser.OR, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.FormulaContext)
            else:
                return self.getTypedRuleContext(CKBParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CKBParser.NOT, 0)
        def formula(self):
            return self.getTypedRuleContext(CKBParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.FormulaContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CKBParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def COMMA(self):
            return self.getToken(CKBParser.COMMA, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CKBParser.FormulaContext)
            else:
                return self.getTypedRuleContext(CKBParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CKBParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(CKBParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(CKBParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(CKBParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CKBParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CKBParser.NOT]:
                localctx = CKBParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 61
                self.match(CKBParser.NOT)
                self.state = 62
                self.formula(5)
                pass
            elif token in [CKBParser.LPAR]:
                localctx = CKBParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(CKBParser.LPAR)
                self.state = 64
                self.formula(0)
                self.state = 65
                self.match(CKBParser.RPAR)
                pass
            elif token in [CKBParser.ID]:
                localctx = CKBParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                localctx.atom = self.match(CKBParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CKBParser.AndContext(self, CKBParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 70
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 71
                        self.match(CKBParser.COMMA)
                        self.state = 72
                        localctx.right = self.formula(5)
                        pass

                    elif la_ == 2:
                        localctx = CKBParser.OrContext(self, CKBParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 73
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 74
                        self.match(CKBParser.OR)
                        self.state = 75
                        localctx.right = self.formula(4)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




