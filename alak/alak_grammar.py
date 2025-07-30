grammar = r"""
start: statement+

statement: print_stmt
         | assign_stmt
         | if_stmt
         | while_stmt
         | func_def
         | func_call

print_stmt: "tungga" expr ";"
assign_stmt: "alak" CNAME "=" expr ";"
if_stmt: "kung" "(" condition ")" "tagay" statement+ "bitaw"
while_stmt: "ikot" "(" condition ")" "tagay" statement+ "bitaw"

func_def: "inom" CNAME "(" [params] ")" "tagay" statement+ "bitaw"
params: CNAME ("," CNAME)*

func_call: CNAME "(" [args] ")" ";"
args: expr ("," expr)*

condition: expr comp_op expr

?expr: expr "+" term   -> add
     | expr "-" term   -> sub
     | term

?term: term "*" factor -> mul
     | term "/" factor -> div
     | factor

?factor: list_literal
       | index_access
       | NUMBER        -> number
       | STRING        -> string
       | "walangTama"  -> false
       | "myTama"      -> true
       | CNAME         -> var
       | "(" expr ")"

list_literal: "[" [expr_list] "]"
expr_list: expr ("," expr)*

index_access: CNAME "[" expr "]"

comp_op: "==" | "!=" | ">" | "<"

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS

SL_COMMENT: /\/\/[^\r\n]*/
%ignore SL_COMMENT
"""