class Interpreter:
    def __init__(self):
        self.env = {}

    def interpret(self, ast):
        for stmt in ast:
            self.execute(stmt)

    def execute(self, stmt):
        if stmt[0] == 'let':
            _, name, expr = stmt
            self.env[name] = self.evaluate(expr)

        elif stmt[0] == 'assign':
            _, name, expr = stmt
            if name not in self.env:
                raise RuntimeError(f"Undefined variable '{name}'")
            self.env[name] = self.evaluate(expr)


        elif stmt[0] == 'print':
            _, expr = stmt
            print(self.evaluate(expr))

        elif stmt[0] == 'if':
            _, cond, then_branch, else_branch = stmt
            if self.evaluate(cond):
                for s in then_branch:
                    self.execute(s)
            elif else_branch:
                for s in else_branch:
                    self.execute(s)

                        
    def evaluate(self, expr):
        kind = expr[0]
        if kind == 'number':
            return expr[1]
        elif kind == 'string':
            return expr[1]
        elif kind == 'var':
            return self.env.get(expr[1], None)
        elif kind == 'add':
            return self.evaluate(expr[1]) + self.evaluate(expr[2])
        elif kind == 'gt':
            return self.evaluate(expr[1]) > self.evaluate(expr[2])
        elif kind == 'lt':
            return self.evaluate(expr[1]) < self.evaluate(expr[2])
        elif kind == 'gte':
            return self.evaluate(expr[1]) >= self.evaluate(expr[2])
        elif kind == 'lte':
            return self.evaluate(expr[1]) <= self.evaluate(expr[2])
        elif kind == 'eq':
            return self.evaluate(expr[1]) == self.evaluate(expr[2])
        elif kind == 'neq':
            return self.evaluate(expr[1]) != self.evaluate(expr[2])
        elif kind == 'gt':
            return self.evaluate(expr[1]) > self.evaluate(expr[2])
        elif kind == 'lt':
            return self.evaluate(expr[1]) < self.evaluate(expr[2])
        elif kind == 'gte':
            return self.evaluate(expr[1]) >= self.evaluate(expr[2])
        elif kind == 'lte':
            return self.evaluate(expr[1]) <= self.evaluate(expr[2])
        elif kind == 'eq':
            return self.evaluate(expr[1]) == self.evaluate(expr[2])
        elif kind == 'neq':
            return self.evaluate(expr[1]) != self.evaluate(expr[2])


