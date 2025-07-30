#  Alak

**Alak** is a fun, Tagalog-inspired esolang designed for learning and laughs. It uses Filipino "inuman" terms as syntax.

---

## Project Structure
```bash
alak-lang/
├── alak/
│   ├── __init__.py
│   ├── cli.py           # Entry CLI file
│   └── interpreter.py   # Transformer logic
├── example.alak         # Example program
├── setup.py             # Setup config
└── requirements.txt     # Dependencies
```

---

## Getting Started

### 1. How to install
Make sure you have Python 3.x installed.

```bash
git clone git@github.com:jinolacson/alak-lang.git
python3 -m venv env && source env/bin/activate && pip install -e .
```

### Usage
```bash
alak init # Creates hello.alak
alak repl # Launches interactive REPL shell
alak run hello.alak # Runs the program
alak --version # Outputs: alak version 0.1.0
```

### Supported Features in AlakLang
🔹 Variable Declaration
Use alak to declare and initialize a variable:
```
alak x = 5;
alak y = 10;
```

You can also use Boolean values:

```
alak sanMigApple = walangTama; // false
alak alfonsoBrandy = myTama;   // true
```

* Use tungga to print expressions or strings (with variable interpolation):
```
tungga x;
tungga "Total ay {x}";
```

🔹 Comments
Alak supports c-style comment:

```
// Ito ay comment pare!
```

🔹 If Statement
Use ```kung```, ```tagay```, and ```bitaw``` for conditional logic:

```
kung (x < y) tagay
    tungga "{x} pesos ay kaunti sa ambag na {y}";
bitaw
```

🔹 While Loop
Use ```ikot```, ```tagay```, and ```bitaw``` for looping:

```
ikot (x < 10) tagay
    tungga x;
    alak x = x + 1;
bitaw
```

🔹 Function Definition & Calling
Use ```inom``` to define a function and call it like normal:

```
inom ginebra(a, b) tagay
    alak sum = a + b;
    tungga "Total ng tinagay ng tropa ay {sum}";
bitaw

ginebra(3, 5);
```

🔹 Arrays & Indexing
Declare arrays using square brackets ```[]``` and access elements using indices:

```
alak tropa = ["Mark", "Leetz", "Leo"];
tungga tropa[0];
tungga tropa[1];
```


### REPL Example
You can test single lines of Alak code interactively using the REPL:

```bash
alak repl
```

output:
```bash
alak> alak a = 3;
alak> alak b = 5;
alak> tungga a + b;
8.0
alak> exit
```

### Implemented features
* ```alak``` for variable assignment
* ```tungga``` for print
* ```kung```, ```ikot``` for control flow (if, while)
* ```inom``` for function definition
* ```ginebra(...)``` for function calls
* ```"{var}"``` String interpolation
* Boolean literals: ```myTama``` (true), ```walangTama``` (false)
* C-style comments: ```\\ Ito ay comment pare!```
* Array ```["Mark", "Leetz", "Leo"]```

### New Keywords (Under development)

1. ```balikTagay``` Return Statements
```bash
inom add(a, b) tagay
    balikTagay a + b;
bitaw

alak nahilo = add(3, 5);
tungga nahilo;

```

2. Built-in Functions
```bash
haba("alak")        // 4
tropa.nahilo(x)    // push x to tropa array
bilang(tropa)       // Get length
nahilo.PataAs()    // first Uppercase letter
```
4. (Optional) Math library & Better Error Reporting

### License
MIT License. Feel free to use and modify.
