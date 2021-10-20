#####################################################################
# DB.PY --------------------------------------------------------
# Clase para el manejo de la base de datos MySQL
#####################################################################

from tkinter import messagebox
from string_para_db import *
from tkinter.constants import FALSE, TRUE
import mysql.connector


class base_de_datos():
    """
    Clase para manejo de la base de datos en MySQL
    inicializa / chequea de conexion y contiene metodos
    para modificar la DB
    """
    var_resultado = 0

    def __init__(self,):
        """
        Constructor de la clase base_de_datos

        Intentamos conectarnos a la base de datos con pass y usuario ya
        guardados. Siempre pregunta si la base de datos y la tabla estan
        definidas, creandolas o verificando existencia de las mismas
        """
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )
            self.crear_db()
        except:
            print("Error al intertar inicializar y conectar a DB")
            messagebox.showerror(title="Base de Datos",
                                 message="Chequee el estado del servicio SQL o reinicie el servicio")

    # Metodo get_cursor()
    # -------------------------
    def get_cursor(self,):
        """
        Selecciona el cursor de nuestra base de datos
        """
        self.cursor = self.db.cursor()

    # Metodo get_resultado()
    # -------------------------
    def get_resultado(self,):
        """
        Nos retorna las coincidencias encontradas por la base de datos
        """
        return self.var_resultado

    # Metodo clear_resultado()
    # -------------------------
    def clear_resultado(self,):
        """
        Descarta los resultados obtenidos por la base de
        datos a la ultima consulta realizada
        """
        self.var_resultado = 0

    # Metodo crear_db()
    # -------------------------
    def crear_db(self,):
        """
            Crea o verifica existencia de DB y Tabla
        """
        self.get_cursor()
        self.cursor.execute(string_db)
        self.cursor.execute(string_usar_db)
        self.cursor.execute(string_tabla)
        return 0

    # Metodo tabla_vacia()
    # -------------------------
    def tabla_vacia(self,):
        """
        Chequeamos si nuestra tabla tiene algun paciente
        ya definido. Retornando V/F segun el caso
        """
        self.cursor.execute(string_tabla_vacia)
        resultado = self.cursor.fetchall()
        if not resultado:
            print("La tabla esta vacia")
            return TRUE
        else:
            print("La tabla no esta vacia")
            return FALSE

    # Metodo db_conectada()
    # -------------------------
    def db_conectada(self,):
        """
        Verifica que la base de datos se encuentre
        conectada. 
        """
        print("La base de datos esta conectada? " +
              str(self.db.is_connected()))
        if self.db.is_connected == FALSE:
            self.db.reconnect
        print("Se reconecto a la tabla")

    # Metodo consultar_datos()
    # -------------------------
    def consultar_datos(self, var_item, var_consulta):
        """
        Pregunta a la base de datos si presenta coincidencia
        para la variable a consultar
        """

        self.db_conectada()
        self.get_cursor()
        sql = "SELECT * FROM Tabla_Socios WHERE " + \
            var_item+" LIKE '%"+var_consulta+"%'"
        self.cursor.execute(sql)
        self.var_resultado = self.cursor.fetchall()

    # Metodo modificar_datos()
    # -------------------------
    def modificar_datos(self, cadena, datos):
        """
        usada para crear/borrar y modificar socios de nuestra
        base de datos
        """
        self.db_conectada()
        self.cursor.execute(cadena, datos)
        self.db.commit()
        print(self.cursor.rowcount, "Registros afectados")
        pass

    # Metodo socios_prueba()
    # -------------------------
    def socios_de_prueba(self, condicion,):
        """
        Se precargan cuatro socios de muestra para 
        realizar pruebas rapidas 
        """

        if condicion == TRUE:
            self.get_cursor()
            self.cursor.execute(string_alta_socio, string_sql_socio1)
            self.cursor.execute(string_alta_socio, string_sql_socio2)
            self.cursor.execute(string_alta_socio, string_sql_socio3)
            self.cursor.execute(string_alta_socio, string_sql_socio4)
            self.db.commit()
            print(self.cursor.rowcount, "Cantidad de registros agregados.")

    # Metodo consultar_todos()
    # -------------------------
    def consultar_todos(self,):
        """
        Consulta por todos los elementos en la base de datos
        """
        self.get_cursor()
        self.cursor.execute(string_consultar_todos)
        resultado = self.cursor.fetchall()
        for x in resultado:
            print(x)

    # Metodo db_cerrar()
    # -------------------------
    def db_cerrar(self,):
        """
        Cierra la conexion a la base de datos
        """
        if (self.db.is_connected()):
            self.get_cursor()
            self.cursor.close()
            self.db.close()
            print("La conexion ha sido cerrada")
            return TRUE
# EOF
