#  Alak

**Alak** is a fun, Tagalog-inspired esolang designed for learning and laughs. It uses Filipino "inuman" terms as syntax.

---

## Project Structure
```bash
alak-lang/
├── alak/
│   ├── __init__.py
│   ├── cli.py             # Entry CLI file
│   ├── interpreter.py     # Transformer and runtime evaluator for executing AlakLang code
│   └── alak_grammar.py    # Contains the Alak language grammar defined in EBNF syntax as a Python string
├── setup.py               # Installer
└── requirements.txt       # Dependencies
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


## New Keywords (Under development)
* May hangover pa ako, pero gagawin ko pa ito pare!!!

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

4. Randomness with ```lagok()```

```
alak shot = lagok(1, 5); // Random between 1 to 5
alak inumin = ["GSM", "Empe", "SanMig"];
alak randomInom = lagok(inumin);
tungga "Tinagay ay {randomInom}, dami: {shot}";
```

5. Error Handling with ```sukaException```

```
try tagay
    alak x = 5 / 0;
bitaw sukaException
    tungga "Sumuka si tropa. Walang division by sero, pare!";
bitaw
```

6. Tagay-style For Loop: ```hangOver```

```
hangOver alak i = 0; i < 3; i = i + 1 tagay
    tungga "Shot #{i}";
bitaw
```

7. Input from User with ```ambag()```

```
tungga "Tagay para sa nag ambag na {name}!";
```

8. Exit Program with ```patayNa()```


```
tungga "Lasing na, uwian na!";
patayNa();
```
9. Call Functions with ```kalabit```

```
inom paShot() tagay
    tungga "Kampay!";
bitaw

kalabit paShot;
```

### License
MIT License. Feel free to use and modify.
