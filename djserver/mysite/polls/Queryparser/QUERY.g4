grammar QUERY;
query: (conditional ',')* conditional;

conditional: '(' consequent=formula '|' antecedent=formula ')'		#StrongConditional
	   ;

formula: '!' formula    			#Negation
	| left=formula ','  right=formula      	#And
	| left=formula ';' right=formula       	#Or
	| '(' formula ')'	   		#Paren
	| atom=ID				#Var
	; 

ID: ([A-Z]|[a-z])([0-9]|[a-z]|[A-Z]|'_')* ;
WS: (' '|'\t') -> skip;
COMMENT: '//' ~( '\r' | '\n' )* -> skip;

NEWLINE: '\r' '\n' | '\n' | '\r' ;
