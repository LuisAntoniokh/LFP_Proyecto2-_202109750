from Constantes.Letras import LETTERS, LIMITS, RESERVED_WORDS, NUMBERS
from Lexico.Token import Token, TokenType
from Lexico.ErrorLexico import LexicError

class DFA():
    def __init__(self, stringFlow: str):
        self.state = 0
        self.lexeme = ""
        self.stringFlow = stringFlow.strip()

        self.currentIndex = 0
        self.row = 1
        self.col = 1

        self.skipBlankSpaces = True
        self.skipLineBreaks = True
        self.skipLine = False
        self.skipToken = False

    def getNextToken(self):
        while self.currentIndex < len(self.stringFlow):
            token = None
            currentCharacter = self.stringFlow[self.currentIndex]

            if self.skipLine:
                self.currentIndex += 1
                self.col += 1
                if currentCharacter == '\n':
                    self.row += 1
                    self.col = 1
                    self.skipLine = False
                continue

            if self.skipLineBreaks and currentCharacter == '\n':
                token = self._evalAcceptanceState()
                self.row += 1
                self.col = 1
                self.currentIndex += 1

            if token == None:
                token = self._evalCharacter()

            if token == True:
                self.col += 1
                self.currentIndex += 1
                continue
            
            if isinstance(token, Token):
                if token.tokenType == TokenType.ONE_ROW_COMMENT:
                    self.skipLine = True
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if token.tokenType == TokenType.OPEN_MORE_ONE_ROW:
                    self.skipToken = True
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if token.tokenType == TokenType.CLOSE_MORE_ONE_ROW:
                    self.skipToken = False
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                if self.skipToken:
                    # self.col += 1
                    # self.currentIndex += 1
                    continue

                return token

            if isinstance(token, LexicError):
                return token

        if self.lexeme != '':
            return self._evalAcceptanceState()
        return None

    # True -> valid state/character
    # False -> invalid state/character
    # Token -> valid token/lexeme
    # LexicError -> invalid token/lexeme
    def _evalCharacter(self):
        currentCharacter = self.stringFlow[self.currentIndex]
        if currentCharacter == ' ':
            if self.skipBlankSpaces:
                token = self._evalAcceptanceState()
                self.col += 1
                self.currentIndex += 1
                return token
            else:
                self.lexeme += currentCharacter
                return True

        if self.state == 0:
            if currentCharacter in LETTERS:
                self.state = 1
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "=":
                self.state = 2
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "(":
                self.state = 3
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ")":
                self.state = 4
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ",":
                self.state = 5
                self.lexeme += currentCharacter
                return True
            if currentCharacter == ";":
                self.state = 6
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "\"":
                self.state = 7
                self.lexeme += currentCharacter
                return True
            if currentCharacter == '-':
                self.state = 9
                self.lexeme += currentCharacter
                return True
            if currentCharacter == "/":
                self.state = 14
                self.lexeme += currentCharacter
                return True
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 1:
            if currentCharacter in LETTERS or NUMBERS:
                self.state = 1
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in LIMITS:
                self.state = 0
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 2:
            if currentCharacter in LIMITS:
                self.state = 0
                return True
        
        if self.state == 3:
            if currentCharacter in LIMITS:
                self.state = 0
                return True
            
        if self.state == 4:
            if currentCharacter in LIMITS:
                self.state = 0
                return True
            
        if self.state == 5:
            if currentCharacter in LIMITS:
                self.state = 0
                return True
        
        if self.state == 6:
            if currentCharacter in LIMITS:
                self.state = 0
                return True

        if self.state == 7:
            if currentCharacter in LETTERS:
                self.state = 8
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in NUMBERS:
                self.state = 8
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == "{":
                self.state = 19
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 8:
            if currentCharacter in LETTERS:
                self.state = 8
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in NUMBERS:
                self.state = 8
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == "\"":
                self.state = 18
                self.lexeme += currentCharacter
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 18:
            if currentCharacter in LIMITS:
                self.state = 0
                return True
            
            if currentCharacter == ",":
                self.state = 0
                self.lexeme += currentCharacter
                return True

        if self.state == 19:
            if currentCharacter in LETTERS:
                self.state = 19
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in LIMITS:
                self.state = 19
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == "\"":
                self.state = 19
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == ":":
                self.state = 19
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == ",":
                self.state = 19
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == "}":
                self.state = 20
                self.lexeme += currentCharacter
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 20:
            if currentCharacter == "\"":
                self.state = 21
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == ",":
                self.state = 7
                self.lexeme += currentCharacter
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 21:
            if currentCharacter in LIMITS:
                self.state = 0
                return True

        if self.state == 9:
            if currentCharacter == '-':
                self.state = 10
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 10:
            if currentCharacter == '-':
                self.state = 11
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 11:
            if currentCharacter in LETTERS:
                self.state = 12
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in NUMBERS:
                self.state = 12
                self.lexeme += currentCharacter
                return True

            if currentCharacter == " ":
                self.state = 12
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 12:
            if currentCharacter == " ":
                self.state = 12
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter in LETTERS or NUMBERS:
                self.state = 12
                self.lexeme += currentCharacter
                return True

            if currentCharacter == "\n":
                self.state = 13
                self.lexeme += currentCharacter
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error
        
        if self.state == 13:
            if currentCharacter in LIMITS:
                self.state = 0
                return True

        if self.state == 14:
            if currentCharacter == "*":
                self.state = 15
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 15:
            if currentCharacter in LETTERS:
                self.state = 15
                self.lexeme += currentCharacter
                return True
            
            if currentCharacter == "*":
                self.state = 16
                self.lexeme += currentCharacter
                return True

            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 16:
            if currentCharacter == "/":
                self.state = 17
                self.lexeme += currentCharacter
                return True
            
            error = self._generateError("Invalid token")
            self._resetAutomaton()
            self.currentIndex += 1
            self.col += 1
            return error

        if self.state == 17:
            if currentCharacter in LIMITS:
                self.state = 0
                return True

        return self._evalAcceptanceState()

    def _resetAutomaton(self):
        self.state = 0
        self.lexeme = ""

    def _evalAcceptanceState(self):
        
        if self.state == 0:
            self.currentIndex -= 1
            return True
        if self.state == 1:
            token = self._generateToken(TokenType.ID)
            self._resetAutomaton()
            return token
        if self.state == 2:
            token = self._generateToken(TokenType.EQUALS)
            self._resetAutomaton()
            return token
        if self.state == 3:
            token = self._generateToken(TokenType.PARENTHESIS_OPENING)
            self._resetAutomaton()
            return token
        if self.state == 4:
            token = self._generateToken(TokenType.PARENTHESIS_CLOSING)
            self._resetAutomaton()
            return token
        if self.state == 5:
            token = self._generateToken(TokenType.COMMA)
            self._resetAutomaton()
            return token
        if self.state == 6:
            token = self._generateToken(TokenType.SEMICOLON)
            self._resetAutomaton()
            return token
        if self.state == 13:
            token = self._generateToken(TokenType.ONE_ROW_COMMENT)
            self._resetAutomaton()
            return token
        if self.state == 17:
            token = self._generateToken(TokenType.CLOSE_MORE_ONE_ROW)
            self._resetAutomaton()
            return token
        if self.state == 18:
            token = self._generateToken(TokenType.STRING)
            self._resetAutomaton()
            return token
        if self.state == 21:
            token = self._generateToken(TokenType.JSON)
            self._resetAutomaton()
            return token

        error = self._generateError("Lexema no reconocido")
        self._resetAutomaton()
        return error

    def _generateToken(self, tokenType):
        token = Token(tokenType, self.lexeme, self.row, self.col)
        return token

    def _generateError(self, msg) -> LexicError:
        currentCharacter = self.stringFlow[self.currentIndex]
        self.lexeme += currentCharacter
        return LexicError(self.lexeme, msg, self.row, self.col)
