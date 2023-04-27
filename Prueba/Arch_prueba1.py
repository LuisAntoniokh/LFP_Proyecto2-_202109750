entrada = '''
CrearBD ejemplo = nueva CrearBD();
EliminarBD elimina = nueva EliminarBD();
CrearColeccion colec = nueva CrearColeccion("NombreColeccion");
EliminarColeccion eliminacolec = nueva
EliminarColeccion("NombreColeccion");
InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion" ,
"
{
 "nombre" : "Obra Literaria",
 "autor" : "Jorge Luis"
 }
");
Funcion Nombre = nueva Funcion("identificador");
Funcion Nombre = nueva Funcion();
Funcion Nombre = nueva Funcion("", "JSON");
ActualizarUnico actualizadoc = nueva ActualizarUnico("NombreColeccion",
"
{
 "nombre" : "Obra Literaria"
},
{
 $set: {"autor" : "Mario Vargas"}
}
");
EliminarUnico eliminadoc = nueva EliminarUnico("NombreColeccion",
"
{
 "nombre" : "Obra Literaria"
}
");
BuscarTodo todo = nueva BuscarTodo ("NombreColeccion");
BuscarUnico todo = nueva BuscarUnico ("NombreColeccion");
'''