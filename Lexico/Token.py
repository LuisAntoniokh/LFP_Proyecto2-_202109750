from enum import Enum, auto

class TokenType(Enum):
    ID = auto()
    EQUALS = auto()
    PARENTHESIS_OPENING = auto()
    PARENTHESIS_CLOSING = auto()
    COMMA = auto()
    SEMICOLON = auto()
    STRING = auto()
    ONE_ROW_COMMENT = auto()
    OPEN_MORE_ONE_ROW = auto()
    CLOSE_MORE_ONE_ROW = auto()
    JSON = auto()
    
class Token():
    def __init__(self, tokenType: TokenType, lexeme: str = None, row: int = None, col: int = None):
        self.tokenType = tokenType
        self.lexeme = lexeme
        self.row = row
        self.col = col

        # hidden optional attributes
        self.posibleLexemes = None
        self.idType = None
