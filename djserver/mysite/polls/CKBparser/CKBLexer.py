# Generated from CKBLexer.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\7\4;\n\4\f\4\16\4>\13\4\3\5\5\5A\n")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\6\6H\n\6\r\6\16\6I\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21\3\2\5\4\2C\\c|\7\2//\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5+\3")
        buf.write("\2\2\2\78\3\2\2\2\t@\3\2\2\2\13G\3\2\2\2\rM\3\2\2\2\17")
        buf.write("O\3\2\2\2\21Q\3\2\2\2\23S\3\2\2\2\25U\3\2\2\2\27W\3\2")
        buf.write("\2\2\31Y\3\2\2\2\33[\3\2\2\2\35]\3\2\2\2\37_\3\2\2\2!")
        buf.write("\"\7u\2\2\"#\7k\2\2#$\7i\2\2$%\7p\2\2%&\7c\2\2&\'\7v\2")
        buf.write("\2\'(\7w\2\2()\7t\2\2)*\7g\2\2*\4\3\2\2\2+,\7e\2\2,-\7")
        buf.write("q\2\2-.\7p\2\2./\7f\2\2/\60\7k\2\2\60\61\7v\2\2\61\62")
        buf.write("\7k\2\2\62\63\7q\2\2\63\64\7p\2\2\64\65\7c\2\2\65\66\7")
        buf.write("n\2\2\66\67\7u\2\2\67\6\3\2\2\28<\t\2\2\29;\t\3\2\2:9")
        buf.write("\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\b\3\2\2\2><\3")
        buf.write("\2\2\2?A\7\17\2\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\7\f")
        buf.write("\2\2CD\3\2\2\2DE\b\5\2\2E\n\3\2\2\2FH\t\4\2\2GF\3\2\2")
        buf.write("\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\b\6\2\2L")
        buf.write("\f\3\2\2\2MN\7*\2\2N\16\3\2\2\2OP\7+\2\2P\20\3\2\2\2Q")
        buf.write("R\7}\2\2R\22\3\2\2\2ST\7\177\2\2T\24\3\2\2\2UV\7~\2\2")
        buf.write("V\26\3\2\2\2WX\7.\2\2X\30\3\2\2\2YZ\7#\2\2Z\32\3\2\2\2")
        buf.write("[\\\7=\2\2\\\34\3\2\2\2]^\7]\2\2^\36\3\2\2\2_`\7_\2\2")
        buf.write("` \3\2\2\2\7\2:<@I\3\b\2\2")
        return buf.getvalue()


class CKBLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SIGNATURE = 1
    CONDITIONALS = 2
    ID = 3
    NEWLINE = 4
    WS = 5
    LPAR = 6
    RPAR = 7
    LBRA = 8
    RBRA = 9
    SEP = 10
    COMMA = 11
    NOT = 12
    OR = 13
    RL = 14
    LL = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'signature'", "'conditionals'", "'('", "')'", "'{'", "'}'", 
            "'|'", "','", "'!'", "';'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "SIGNATURE", "CONDITIONALS", "ID", "NEWLINE", "WS", "LPAR", 
            "RPAR", "LBRA", "RBRA", "SEP", "COMMA", "NOT", "OR", "RL", "LL" ]

    ruleNames = [ "SIGNATURE", "CONDITIONALS", "ID", "NEWLINE", "WS", "LPAR", 
                  "RPAR", "LBRA", "RBRA", "SEP", "COMMA", "NOT", "OR", "RL", 
                  "LL" ]

    grammarFileName = "CKBLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


