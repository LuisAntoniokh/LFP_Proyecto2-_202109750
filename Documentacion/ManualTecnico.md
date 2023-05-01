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
El siguiente codigo limpia el area de texto y llama a la funcion guardarComo()

![Boton nuevo](/src/Imagenes/btnNuevo.png)

# Boton Tokens
El siguiente codigo muestra una nueva ventana en donde se muestran los tokens que reconocio el programa

![Boton Tokens](/src/Imagenes/btnTokens.png)

# Boton errores
 El siguiente codigo muestra una nueva ventana en donde se muestran los errores que reconocio el programa

![Boton errores](/src/Imagenes/btnErrores.png)

# Funcion getErros()
Obtiene los errores (lexemas no reconocidos) del archivo de texto

![Funcion getErros()](/src/Imagenes/getErrors.png)

# Funcion runLexicAnalysis()
Ejecuta el analizador lexico del programa

![Funcion runLexicAnalysis()](/src/Imagenes/defRunLexicAnalysis.png)


# Clase ErrorTable()
Da el diseño que llevará la tabla, además creará la función loadData(data) que permitirá ingresar la cadena de texto del archivo a una tabla.

![Clase ErrorTable()](/src/Imagenes/classErrorTable.png)