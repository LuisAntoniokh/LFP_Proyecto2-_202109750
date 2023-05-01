from Lexico.LexPar import Lexer

class Core():
    def __init__(self):
        Core.SymbolTable = []
        Core.runTimeErrors = []

        if len(self.getErrors()) != 0:
            return

        self.createSymbolTable()
        self.applyProperties()

    @classmethod
    def getElement(cls, targetId: str):
        for element in cls.SymbolTable:
            if element.id == targetId:
                return element

        return None

    def getErrors(self):

        errors = []

        for lexicError in Lexer.lexicErrors:
            errors.append({
                'type': 'Lexico',
                'row': str(lexicError.row),
                'column': str(lexicError.col),
                'lexema': lexicError.lexeme,
                'expected': "",
                'description': lexicError.msg
            })
        
        return errors