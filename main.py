# Simple Compiler Design Toolkit

# -------- LEXICAL ANALYZER --------
def lexical_analyzer():
    with open("input/source_code.txt") as f:
        code = f.read()
    tokens = code.split()
    with open("output/tokens.txt", "w") as f:
        for t in tokens:
            f.write(t + "\n")
    print("Lexical Analysis Done → tokens.txt")


# -------- REGEX TO DFA (Dummy) --------
def regex_to_dfa():
    with open("input/regex.txt") as f:
        regex = f.read()
    with open("output/dfa.txt", "w") as f:
        f.write("DFA constructed for regex: " + regex)
    print("Regex → DFA Done → dfa.txt")


# -------- FIRST FOLLOW (Dummy) --------
def parsing_table():
    with open("input/grammar.txt") as f:
        grammar = f.read()
    with open("output/parsing_table.txt", "w") as f:
        f.write("Parsing table generated for grammar:\n" + grammar)
    print("Parsing Table Generated → parsing_table.txt")


# -------- MAIN --------
if __name__ == "__main__":
    lexical_analyzer()
    regex_to_dfa()
    parsing_table()
    print("Compiler Toolkit Executed Successfully")