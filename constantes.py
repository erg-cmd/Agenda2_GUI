#####################################################################
# CONSTANTES.PY ----------------------------------------------------
# Constantes y strings utilizadas de placeholders, regex,y
# demas constantes
#####################################################################
cant_entries = 9

# para frame datos_socio
items_labels = ["Numero de Socio", "Nombre", "Apellido",
                "DNI", "Domicilio", "Localidad", "Nacionalidad",
                "Fecha de Nacimiento", "Meses Impagos"]
placeholders_labels_socio = ["123456", "Elias", "Gracia",
                             "12345678", "Calle 123", "Lomas de Zamora", "Argentino",
                             "2000-01-24", "Abril2018,Junio2019"]
placeholder_consulta_entry = "Ingrese aqui su busqueda"
placeholder_consulta_label = ["\n\nNo se han realizado consultas\n\n", "Se han encontrado",
                              "coincidencias", "\n\nNo se han encontrado coincidencias\n\n",
                              "\n\nNo se ha seleccionado categoria\n\n",
                              "\n\nCambios realizados exitosamente!\n\n"]
# para regex
string_patron = ["^\d{1,5}$", "^[a-zA-Z]+$", "^[a-zA-Z]+$",
                 "([1-9][0-9]{6}$|[1-5][0-9]{7}$)",
                 "(^[a-zA-Z]+\s([a-zA-Z]+\s)?([a-zA-Z]+\s)?([a-zA-Z]+\s)?)\d{1,6}\Z",
                 '''(^(\d{1,2}) [a-zA-Z]+ ([a-zA-Z]+)?|(^[a-zA-Z]+$)|(^[a-zA-Z]+\s([a-zA-Z]+\s)?([a-zA-Z]+)\Z)|^[a-zA-Z]+ (\d{1,6})?\Z)''',
                 "^[a-zA-Z]{2,15}$", "(1|2)[0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])"
                 ]
