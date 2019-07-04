%token IF THEN ELSE ID NUM
%right '='
%left '+' '-'
%left '*' '/'

%%
S : '(' E ')'{lab1();} ELSE E ';'{lab2();} THEN E ';'{lab3();}
E : V '='{push();} E{codegen_assign();}
| E '+' {push();} E{codegen();}
| E '-' {push();} E{codegen();}
| E '*' {push();} E{codegen();}
| E '/' {push();} E{codegen();}
|'(' E ')'
|V
| NUM{push();}
;
V : ID{push();}
;
%%

#include "lex.yy.c"
#include<ctype.h>

char st[100][100];
int top=0;
char i_[2]="0";
char temp[2]="t";
int label[20];
int lnum=0;
int ltop=0;

main()
{
	printf("Enter your expression : ");
	yyparse();
}


push()
{
	strcpy(st[top],yytext);
}

codegen()
{
	lnum++;
	strcpy(temp,"t");
	strcat(temp,i_);
	printf("%s = %s %s %s \n",temp,st[top-2],st[top-1],st[top]);
	top-=2;
	strcpy(st[top],temp);
	i_[0]++;

}

codegen_assign()
{
	printf("%s = %s \n",st[top-2],st[top]);
	top-=2;
}

lab1()
{
	lnum++;
	strcpy(temp,"t");
	strcat(temp,i_);
	printf("%s not %s \n",temp,st[top]);
	printf("if %s goto L%d",temp,lnum);
	i_[0]++;
	label[++ltop]=lnum;
}


lab2()
{
	lnum++;
	int x;
	x=label[ltop--];
	printf("goto L%d \n",lnum);
	printf("L%d\n",x);
	i_[0]++;
	label[++ltop]=lnum;
}

lab3()
{
	int y;
	y=label[ltop--];
	printf("L%d\n",y);

}

int yyerror()
{

}

int yywrap()
{
	return 1;
}