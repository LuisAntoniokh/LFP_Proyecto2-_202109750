# Manual técnico
```sh
Luis Antonio Castro Padilla
202109750
```

# Tabla de tokens
| Token | Representacion |
| ------ | ------ |
| ID  | L+ |
| EQUALS | = |
| PARENTHESIS_OPENING | ( |
| PARENTHESIS_CLOSING | ) |
| COMMA | , |
| SEMICOLON | ; |
| STRING | "L+" |
| OPEN_MORE_ONE_ROW | --- |
| OPEN_MORE_ONE_ROW | /* |
| CLOSE_MORE_ONE_ROW | */ |
| JSON | "{}" |


# Método del árbol

![Arbol](/src/Imagenes/Arbol.png)

# AFD

![Automata finito determinista](/src/Imagenes/AFD.png)

# Gramática libre de contexto

    init : instrucciones

    instrucciones : instruccion instrucciones
                | instruccion

    instruccion : crearDB ;
                | eliminarDB ; 
                | crearColeccion ;
                | eliminarColeccion ;
                | insertarUnico ;
                | actualizarUnico ;
                | eliminarUnico ;
                | buscarTodo ;
                | buscarUnico ;

    crearDB : CrearDB ID = nueva CrearDB ( )

    eliminarDB : EliminarDB ID = nueva EliminarDB ( )

    crearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING )

    eliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING )

    insertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING )

    actualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , STRING )

    eliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING )

    buscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING )

    buscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING )

# Boton Nuevo
## El siguiente codigo limpia el area de texto y llama a la funcion guardarComo()

def btnNuevo(self):
    if self.filename:
        respuesta = messagebox.askyesnocancel(title="Guardar cambios", message="¿Desea guardar los cambios antes de limpiar el editor?")
        if respuesta == True:
            self.guardarComo()
            self.filename = None
            lbNomArch = self.vMain.nametowidget("lbNombre")
            lbNomArch.config(text="")
        elif respuesta == False:
            self.filename = None
        else: 
            return
    else:
        messagebox.showinfo(title="Información", message="No hay ningún archivo seleccionado, seleccione uno")
    txt_data = self.vMain.nametowidget("txt_data")
    txt_data.delete(1.0, END)

# Boton Tokens
## El siguiente codigo muestra una nueva ventana en donde se muestran los tokens que reconocio el programa

def pTokens(self):
    try:
        file = open(self.filename, 'r', encoding="utf-8", errors='ignore')
        text = file.read()
        file.close()
        lexer = Lexer(text)
        tokens = lexer.runLexicAnalysis()
        self.tokenWindow = Toplevel(self.vMain)
        self.tokenWindow.geometry("1000x900")
        self.tokenTable = TokenTable(self.tokenWindow)
        self.tokenTable.table.pack(expand=1, fill=BOTH)
        self.tokenTable.loadData(tokens)
    except Exception as e:
        print(e)

# Boton errores
## El siguiente codigo muestra una nueva ventana en donde se muestran los errores que reconocio el programa
def pErrores(self):
    try:
        file = open(self.filename, 'r', encoding="utf-8", errors='ignore')
        text = file.read()
        file.close()
        lexer = Lexer(text)
        tokens = lexer.runLexicAnalysis()
        core = Core()
        errors = core.getErrors()
        if len(errors) > 0:
            self.errorWindow = Toplevel(self.vMain)
            self.errorWindow.geometry("1000x900")
            self.errorTable = ErrorTable(self.errorWindow)
            self.errorTable.table.pack(expand=1, fill=BOTH)
            self.errorTable.loadData(errors)
            return
    except Exception as e:
        print(e)

# Funcion getErros()
## Obtiene los errores (lexemas no reconocidos) del archivo de texto

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

# Funcion runLexicAnalysis()
## Ejecuta el analizador lexico del programa

def runLexicAnalysis(self):
    resp = True
    while resp != None:
        resp = self.dfa.getNextToken()
        if isinstance(resp, Token):
            self.tokenFlow.append(resp)
        elif isinstance(resp, LexicError):
            self.lexicErrors.append(resp)
    # self.printTokenFlow()
    return self.getTokens()

# Clase ErrorTable()
## Da el diseño que llevará la tabla, además creará la función loadData(data) que permitirá ingresar la cadena de texto del archivo a una tabla.

class ErrorTable():
    def __init__(self, window):
        self.window = window
        self.table = ttk.Treeview(self.window, height=35)
        self.window.title("Tabla de errores")
        self.table['columns'] = ('Tipo', 'Fila', 'Columna', 'Lexema', 'Esperaba', 'Descripcion')
        self.table.column('#0', width=0, stretch=NO)
        self.table.column("Tipo", anchor=CENTER, width=10)
        self.table.column("Fila", anchor=CENTER, width=10)
        self.table.column("Columna", anchor=CENTER, width=10)
        self.table.column("Lexema", anchor=CENTER, width=50)
        self.table.column("Esperaba", anchor=CENTER, width=120)
        self.table.column("Descripcion", anchor=CENTER, width=80)
        self.table.heading('#0', text="", anchor=CENTER)
        self.table.heading("Tipo", text="Tipo", anchor=CENTER)
        self.table.heading("Fila", text="Fila", anchor=CENTER)
        self.table.heading("Columna", text="Columna", anchor=CENTER)
        self.table.heading("Lexema", text="Lexema", anchor=CENTER)
        self.table.heading("Esperaba", text="Esperaba", anchor=CENTER)
        self.table.heading("Descripcion", text="Descripcion", anchor=CENTER)
    def loadData(self, data):
        for row in self.table.get_children():
            self.table.delete(row)
        for row in data:
            self.table.insert('', 'end', values=(row['type'], row['row'], row['column'], row['lexema'], row['expected'], row['description']))
