# STRING PARA MYSQL
string_tabla_vacia = "SELECT * from Tabla_Socios limit 1"
string_db = "CREATE DATABASE IF NOT EXISTS Club_Python"
string_usar_db = "USE Club_Python"
string_consultar_todos="SELECT * FROM Tabla_Socios"
string_tabla = '''CREATE TABLE IF NOT EXISTS Tabla_Socios( 
    socio int(1) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre CHAR(20),
    apellido char(20),
    dni INT,
    domicilio CHAR(35), 
    localidad char(30), 
    nacionalidad CHAR(35),
    fnacimiento DATE, 
    meses_impagos CHAR(40))'''
string_socio = '''INSERT INTO Tabla_Socios (
    socio, nombre, apellido,dni,domicilio,localidad,
    nacionalidad, fnacimiento, meses_impagos) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
string_alta_socio = '''INSERT INTO Tabla_Socios (
    nombre, apellido,dni,domicilio,localidad,
    nacionalidad, fnacimiento, meses_impagos) 
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)'''
string_modif_socio = '''UPDATE Tabla_Socios SET nombre=%s, apellido=%s,
    dni=%s,domicilio=%s,localidad=%s,nacionalidad=%s, fnacimiento=%s, meses_impagos=%s
    WHERE socio=%s'''
string_baja_socio = "DELETE FROM Tabla_Socios WHERE socio=%s"
string_busqueda_sql = ["socio", "nombre", "apellido", "dni", "domicilio",
                       "localidad", "nacionalidad", "fnacimiento", "meses_impagos"]
string_sql_socio1 = ["123456", "Elias", "Gracia",
                     "10456789", "Pasteur 260", "Lomas de Zamora", "Argentino",
                     "1999-01-20", "Debe todo el 2019"]
string_sql_socio2 = ["123457", "Juan", "Garcia",
                     "20459876", "Plank 170", "Cleypole", "Paraguayo",
                     "1990-02-24", "Abril2018"]
string_sql_socio3 = ["123458", "Alejandra", "Perez",
                     "39056789", "Einsten 100", "Lanus", "Uruguaya",
                     "1980-03-14", "Junio2019"]
string_sql_socio4 = ["123459", "Cecilia", "Ortega",
                     "92056789", "Milsten 998", "Avellaneda", "Brasilera",
                     "2010-04-04", "No adeuda"]
