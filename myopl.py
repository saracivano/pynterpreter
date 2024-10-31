
INT = "INT"
FLOAT = "FLOAT"
PLUS = "PLUS"
MINUS = "MINUS"
MUL = "MUL"
DIV = "DIV"
MOD = "MOD"
LPAREN = "LPAREN"
RPAREN = "RPAREN"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        result = self.type
        if self.value: result += str(self.value)
        return result

class Lexer:
    def __init__(self, text):
        self.text = text
        self.index = -1
        self.char: str = None
        self.advance()
    
    def advance(self):
        self.index += 1
        self.char = self.text[self.index] if self.index < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.char != None:
            if self.char == "+":
                tokens.append(Token(PLUS))
                self.advance()
            elif self.char == "-":
                tokens.append(Token(MINUS))
                self.advance()
            elif self.char == "*":
                tokens.append(Token(MUL))
                self.advance()
            elif self.char == "/":
                tokens.append(Token(DIV))
                self.advance()
            elif self.char == "%":
                tokens.append(Token(MOD))
                self.advance()
            elif self.char == "(":
                tokens.append(Token(LPAREN))
                self.advance()
            elif self.char == ")":
                tokens.append(Token(RPAREN))
                self.advance()
            elif self.char.isdigit():
                tokens.append(self.make_number())

    def make_number(self):
        result = 
                

def run():
    return None, None

while True:
    text = input(">>>")
    result, error = run(text)
    
    if error: print(error)
    else: print(result)