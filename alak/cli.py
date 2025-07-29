"""
Developer: leetz-kowd
Project: alak
Date: 2025-07-21
Version: 1.0.0
"""

import sys
import os
from alak.interpreter import AlakInterpreter, alak_grammar
from lark import Lark

VERSION = "0.1.0"

def run_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    parser = Lark(alak_grammar, parser='lalr', transformer=AlakInterpreter())
    parser.parse(code)

def init_project():
    template_code = """
         tungga "Kamusta, ka tagay!";
    """
    filename = "hello.alak"
    if os.path.exists(filename):
        print(f"{filename} already exists.")
    else:
        with open(filename, "w") as f:
            f.write(template_code.strip())
        print(f"Created {filename} with starter code.")

def main():
    if len(sys.argv) == 1:
        print("Usage: alak [run|init|--version] <filename>")
        return

    command = sys.argv[1]

    if command == "run":
        if len(sys.argv) < 3:
            print("Usage: alak run <filename>")
        else:
            run_file(sys.argv[2])
    elif command == "init":
        init_project()
    elif command == "--version":
        print(f"alak version {VERSION}")
    else:
        print(f"Unknown command: {command}")
