from lark import Lark, Transformer

alak_grammar = """
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
func_def: "inom" CNAME "tagay" statement+ "bitaw"
func_call: CNAME "()" ";"

condition: expr comp_op expr

?expr: expr "+" term   -> add
     | expr "-" term   -> sub
     | term

?term: term "*" factor -> mul
     | term "/" factor -> div
     | factor

?factor: NUMBER        -> number
       | STRING        -> string
       | CNAME         -> var
       | "(" expr ")"

comp_op: "==" | "!=" | ">" | "<"

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING -> STRING
%import common.WS
%ignore WS
"""

class AlakInterpreter(Transformer):
    def __init__(self):
        self.vars = {}
        self.funcs = {}

    def start(self, items):
        for stmt in items:
            if callable(stmt):
                stmt()

    def statement(self, items):
        return items[0]

    def print_stmt(self, items):
        return lambda: print(items[0]())

    def assign_stmt(self, items):
        var_name = str(items[0])
        expr_fn = items[1]
        return lambda: self.vars.__setitem__(var_name, expr_fn())

    def var(self, name):
        return lambda: self.vars.get(str(name[0]), 0)

    def number(self, n):
        return lambda: float(n[0])

    def string(self, s):
        return lambda: s[0][1:-1]

    def add(self, items):
        return lambda: items[0]() + items[1]()

    def sub(self, items):
        return lambda: items[0]() - items[1]()

    def mul(self, items):
        return lambda: items[0]() * items[1]()

    def div(self, items):
        return lambda: items[0]() / items[1]()

    def comp_op(self, tokens):
        if not tokens:
            print(f"comp_op received no tokens {tokens}")
            return None
        return tokens[0].value


    def condition(self, items):
        left, op, right = items
        return lambda: (
            left() == right() if op == "==" else
            left() != right() if op == "!=" else
            left() > right() if op == ">" else
            left() < right()
        )

    def if_stmt(self, items):
        condition_fn = items[0]
        body = items[1:]
        return lambda: [stmt() for stmt in body] if condition_fn() else None

    def while_stmt(self, items):
        condition_fn = items[0]
        body = items[1:]
        def loop():
            while condition_fn():
                for stmt in body:
                    stmt()
        return loop

    def func_def(self, items):
        name = str(items[0])
        body = items[1:]
        self.funcs[name] = body
        return lambda: None

    def func_call(self, items):
        name = str(items[0])
        body = self.funcs.get(name, [])
        return lambda: [stmt() for stmt in body]
