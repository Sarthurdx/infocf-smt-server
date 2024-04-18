// Generated from CKBLexer.g4 by ANTLR 4.9
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CKBLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SIGNATURE=1, CONDITIONALS=2, TOP=3, BOTTOM=4, ID=5, NEWLINE=6, WS=7, LPAR=8, 
		RPAR=9, LBRA=10, RBRA=11, SEP=12, COMMA=13, NOT=14, OR=15, RL=16, LL=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SIGNATURE", "CONDITIONALS", "TOP", "BOTTOM", "ID", "NEWLINE", "WS", 
			"LPAR", "RPAR", "LBRA", "RBRA", "SEP", "COMMA", "NOT", "OR", "RL", "LL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'signature'", "'conditionals'", "'Top'", "'Bottom'", null, null, 
			null, "'('", "')'", "'{'", "'}'", "'|'", "','", "'!'", "';'", "'['", 
			"']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SIGNATURE", "CONDITIONALS", "TOP", "BOTTOM", "ID", "NEWLINE", 
			"WS", "LPAR", "RPAR", "LBRA", "RBRA", "SEP", "COMMA", "NOT", "OR", "RL", 
			"LL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CKBLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CKBLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23p\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6"+
		"\3\6\7\6J\n\6\f\6\16\6M\13\6\3\7\5\7P\n\7\3\7\3\7\3\7\3\7\3\b\6\bW\n\b"+
		"\r\b\16\bX\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16"+
		"\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r"+
		"\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2"+
		"c|\7\2//\62;C\\aac|\5\2\13\f\17\17\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5/\3\2\2\2\7"+
		"<\3\2\2\2\t@\3\2\2\2\13G\3\2\2\2\rO\3\2\2\2\17V\3\2\2\2\21\\\3\2\2\2\23"+
		"^\3\2\2\2\25`\3\2\2\2\27b\3\2\2\2\31d\3\2\2\2\33f\3\2\2\2\35h\3\2\2\2"+
		"\37j\3\2\2\2!l\3\2\2\2#n\3\2\2\2%&\7u\2\2&\'\7k\2\2\'(\7i\2\2()\7p\2\2"+
		")*\7c\2\2*+\7v\2\2+,\7w\2\2,-\7t\2\2-.\7g\2\2.\4\3\2\2\2/\60\7e\2\2\60"+
		"\61\7q\2\2\61\62\7p\2\2\62\63\7f\2\2\63\64\7k\2\2\64\65\7v\2\2\65\66\7"+
		"k\2\2\66\67\7q\2\2\678\7p\2\289\7c\2\29:\7n\2\2:;\7u\2\2;\6\3\2\2\2<="+
		"\7V\2\2=>\7q\2\2>?\7r\2\2?\b\3\2\2\2@A\7D\2\2AB\7q\2\2BC\7v\2\2CD\7v\2"+
		"\2DE\7q\2\2EF\7o\2\2F\n\3\2\2\2GK\t\2\2\2HJ\t\3\2\2IH\3\2\2\2JM\3\2\2"+
		"\2KI\3\2\2\2KL\3\2\2\2L\f\3\2\2\2MK\3\2\2\2NP\7\17\2\2ON\3\2\2\2OP\3\2"+
		"\2\2PQ\3\2\2\2QR\7\f\2\2RS\3\2\2\2ST\b\7\2\2T\16\3\2\2\2UW\t\4\2\2VU\3"+
		"\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\b\2\2[\20\3\2\2\2\\"+
		"]\7*\2\2]\22\3\2\2\2^_\7+\2\2_\24\3\2\2\2`a\7}\2\2a\26\3\2\2\2bc\7\177"+
		"\2\2c\30\3\2\2\2de\7~\2\2e\32\3\2\2\2fg\7.\2\2g\34\3\2\2\2hi\7#\2\2i\36"+
		"\3\2\2\2jk\7=\2\2k \3\2\2\2lm\7]\2\2m\"\3\2\2\2no\7_\2\2o$\3\2\2\2\7\2"+
		"IKOX\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}