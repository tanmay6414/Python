%{
	#include<stdlib.h>
	#define YYSTYPE double
	#include "y.tab.h"
%}
digit [0-9]
integer {digit}+
real {integer}("."{integer})?
%%
{real} {yylval=atof(yytext); return NUMBER;}
"<=" return LE;
">=" return GE;
"==" return EQ;
"!=" return NE;
[\n] return 0;
[\t];
. return yytext[0];
%%