# Generated from QUERY.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\5\b%\n\b\3\b\7\b(\n\b")
        buf.write("\f\b\16\b+\13\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n\65")
        buf.write("\n\n\f\n\16\n8\13\n\3\n\3\n\3\13\3\13\3\13\5\13?\n\13")
        buf.write("\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3")
        buf.write("\2\6\4\2C\\c|\6\2\62;C\\aac|\4\2\13\13\"\"\4\2\f\f\17")
        buf.write("\17\2B\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33")
        buf.write("\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2\2\r!\3\2\2\2\17$\3\2")
        buf.write("\2\2\21,\3\2\2\2\23\60\3\2\2\2\25>\3\2\2\2\27\30\7.\2")
        buf.write("\2\30\4\3\2\2\2\31\32\7*\2\2\32\6\3\2\2\2\33\34\7~\2\2")
        buf.write("\34\b\3\2\2\2\35\36\7+\2\2\36\n\3\2\2\2\37 \7#\2\2 \f")
        buf.write("\3\2\2\2!\"\7=\2\2\"\16\3\2\2\2#%\t\2\2\2$#\3\2\2\2%)")
        buf.write("\3\2\2\2&(\t\3\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3")
        buf.write("\2\2\2*\20\3\2\2\2+)\3\2\2\2,-\t\4\2\2-.\3\2\2\2./\b\t")
        buf.write("\2\2/\22\3\2\2\2\60\61\7\61\2\2\61\62\7\61\2\2\62\66\3")
        buf.write("\2\2\2\63\65\n\5\2\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29:\b\n\2\2")
        buf.write(":\24\3\2\2\2;<\7\17\2\2<?\7\f\2\2=?\t\5\2\2>;\3\2\2\2")
        buf.write(">=\3\2\2\2?\26\3\2\2\2\b\2$\')\66>\3\b\2\2")
        return buf.getvalue()


class QUERYLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ID = 7
    WS = 8
    COMMENT = 9
    NEWLINE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'('", "'|'", "')'", "'!'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "COMMENT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ID", 
                  "WS", "COMMENT", "NEWLINE" ]

    grammarFileName = "QUERY.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


