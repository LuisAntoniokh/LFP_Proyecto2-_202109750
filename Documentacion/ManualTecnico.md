# Manual técnico
```sh
Luis Antonio Castro Padilla
202109750
```

# Tabla de tokens
```sh
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
```

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