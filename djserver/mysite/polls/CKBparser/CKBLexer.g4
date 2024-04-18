lexer grammar CKBLexer;

SIGNATURE : 'signature';
CONDITIONALS : 'conditionals';
ID : [A-Za-z]([a-zA-Z0-9]|'_'|'-')*;
NEWLINE : '\r'? '\n' -> skip;
WS : [ \t\r\n]+ -> skip;
LPAR : '(';
RPAR : ')';
LBRA : '{';
RBRA : '}';
SEP : '|';
COMMA : ',';
NOT: '!';
OR: ';';
RL: '[';
LL: ']';




