# Generated from QUERY.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\7\4)\n\4\f\4\16\4,\13\4\3\4\2\3\6\5\2\4\6\2\2\2/\2\r")
        buf.write("\3\2\2\2\4\22\3\2\2\2\6 \3\2\2\2\b\t\5\4\3\2\t\n\7\3\2")
        buf.write("\2\n\f\3\2\2\2\13\b\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2")
        buf.write("\r\16\3\2\2\2\16\20\3\2\2\2\17\r\3\2\2\2\20\21\5\4\3\2")
        buf.write("\21\3\3\2\2\2\22\23\7\4\2\2\23\24\5\6\4\2\24\25\7\5\2")
        buf.write("\2\25\26\5\6\4\2\26\27\7\6\2\2\27\5\3\2\2\2\30\31\b\4")
        buf.write("\1\2\31\32\7\7\2\2\32!\5\6\4\7\33\34\7\4\2\2\34\35\5\6")
        buf.write("\4\2\35\36\7\6\2\2\36!\3\2\2\2\37!\7\t\2\2 \30\3\2\2\2")
        buf.write(" \33\3\2\2\2 \37\3\2\2\2!*\3\2\2\2\"#\f\6\2\2#$\7\3\2")
        buf.write("\2$)\5\6\4\7%&\f\5\2\2&\'\7\b\2\2\')\5\6\4\6(\"\3\2\2")
        buf.write("\2(%\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\7\3\2\2\2")
        buf.write(",*\3\2\2\2\6\r (*")
        return buf.getvalue()


class QUERYParser ( Parser ):

    grammarFileName = "QUERY.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "'|'", "')'", "'!'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS", 
                      "COMMENT", "NEWLINE" ]

    RULE_query = 0
    RULE_conditional = 1
    RULE_formula = 2

    ruleNames =  [ "query", "conditional", "formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    WS=8
    COMMENT=9
    NEWLINE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.ConditionalContext)
            else:
                return self.getTypedRuleContext(QUERYParser.ConditionalContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = QUERYParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 6
                    self.conditional()
                    self.state = 7
                    self.match(QUERYParser.T__0) 
                self.state = 13
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 14
            self.conditional()
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
            return QUERYParser.RULE_conditional

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrongConditionalContext(ConditionalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.ConditionalContext
            super().__init__(parser)
            self.consequent = None # FormulaContext
            self.antecedent = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.FormulaContext)
            else:
                return self.getTypedRuleContext(QUERYParser.FormulaContext,i)


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



    def conditional(self):

        localctx = QUERYParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_conditional)
        try:
            localctx = QUERYParser.StrongConditionalContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(QUERYParser.T__1)
            self.state = 17
            localctx.consequent = self.formula(0)
            self.state = 18
            self.match(QUERYParser.T__2)
            self.state = 19
            localctx.antecedent = self.formula(0)
            self.state = 20
            self.match(QUERYParser.T__3)
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
            return QUERYParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.FormulaContext)
            else:
                return self.getTypedRuleContext(QUERYParser.FormulaContext,i)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(QUERYParser.FormulaContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.FormulaContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(QUERYParser.ID, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.FormulaContext)
            else:
                return self.getTypedRuleContext(QUERYParser.FormulaContext,i)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QUERYParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(QUERYParser.FormulaContext,0)


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
        localctx = QUERYParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QUERYParser.T__4]:
                localctx = QUERYParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(QUERYParser.T__4)
                self.state = 24
                self.formula(5)
                pass
            elif token in [QUERYParser.T__1]:
                localctx = QUERYParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(QUERYParser.T__1)
                self.state = 26
                self.formula(0)
                self.state = 27
                self.match(QUERYParser.T__3)
                pass
            elif token in [QUERYParser.ID]:
                localctx = QUERYParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                localctx.atom = self.match(QUERYParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = QUERYParser.AndContext(self, QUERYParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        self.match(QUERYParser.T__0)
                        self.state = 34
                        localctx.right = self.formula(5)
                        pass

                    elif la_ == 2:
                        localctx = QUERYParser.OrContext(self, QUERYParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        self.match(QUERYParser.T__5)
                        self.state = 37
                        localctx.right = self.formula(4)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[2] = self.formula_sempred
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
         




