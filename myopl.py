
INT = "INT"
FLOAT = "FLOAT"
PLUS = "PLUS"
MINUS = "MINUS"
MUL = "MUL"
DIV = "DIV"
MOD = "MOD"
LPAREN = "LPAREN"
RPAREN = "RPAREN"

DIGITS = "0123456789"

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        result = self.type
        if self.value != None: result += f":{self.value}"
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
            elif self.char in DIGITS:
                result, error = self.make_number()
                if error: return [], error
                tokens.append(result)
            else:
                return None, None # error
        
        return tokens, None

    def make_number(self):
        result = ""
        decimals = 0

        while self.char != None and self.char in DIGITS + ".":
            if self.char == ".":
                if decimals > 0: return None, None # error
                decimals += 1
            
            result += self.char
            self.advance()
        
        if decimals == 0: return Token(INT, int(result)), None
        return Token(FLOAT, float(result)), None

class NumberNode:
    def __init__(self, token):
        self.token = token
    
    def __repr__(self):
        return str(self.token)

class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"

class UnaryOpNode:
    def __init__(self, op, token):
        self.op = op
        self.token = token
    
    def __repr__(self):
        return f"({self.op} {self.token})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = -1
        self.tok = None
        self.advance()
    
    def advance(self):
        self.index += 1
        self.tok = self.tokens[self.index] if self.index < len(self.tokens) else None
    
    def parse(self):
        pass
    
    def expr(self):
        left, error = self.term()
        if error: return None, error


    def term(self):
        pass
    
    def factor(self):
        pass


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error

while True:
    text = input(">>>")
    result, error = run(text)
    
    if error: print(error)
    else: print(result)