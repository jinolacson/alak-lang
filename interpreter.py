class Interpreter:
    def __init__(self):
        self.env = {}

    def interpret(self, ast):
        for stmt in ast:
            if stmt[0] == 'let':
                _, name, expr = stmt
                self.env[name] = self.evaluate(expr)
            elif stmt[0] == 'print':
                _, expr = stmt
                print(self.evaluate(expr))

    def evaluate(self, expr):
        kind = expr[0]
        if kind == 'number':
            return expr[1]
        elif kind == 'var':
            return self.env.get(expr[1], None)
        elif kind == 'add':
            return self.evaluate(expr[1]) + self.evaluate(expr[2])
