import sys
from lark import Lark
from alak.interpreter import AlakInterpreter, alak_grammar

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print("Usage: alak run filename.alak")
        return

    with open(sys.argv[2], "r") as file:
        code = file.read()

    parser = Lark(alak_grammar, parser="lalr", transformer=AlakInterpreter(), debug=True)
    parser.parse(code)

if __name__ == "__main__":
    main()
