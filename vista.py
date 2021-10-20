#####################################################################
# VISTA.PY --------------------------------------------------------
# Contiene la clase LibroSocioVista
#####################################################################

from constantes import *
from db import *
from string_para_db import *
from tkinter import Label, Listbox, Spinbox, messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import LabelFrame
from tkinter import Scrollbar
from tkinter import LabelFrame
from tkinter.constants import DISABLED, FALSE, INSERT, NORMAL, TRUE
import re

# ----------------------------------
# Clases


class LibroSociosVista:
    """
    Clase que controla aspectos y define metodos 
    para nuestra aplicacion, un libro de socios
    """

    def __init__(self, window):
        """
        Constructor de la clase LibroSociosVista

        En caso de que la base de datos no contenga socios o sea
        inicializada, se pregunta al usuario si desea tener una 
        precarga en la base de datos con socios prefijados

        Se definen eventos asociados a cada entry para borrar
        los places holders 
        """
        self.items_entries = []
        self.items_botones = []
        self.var_socio = []
        self.var_borrado_entry = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.root = window
        self.root.title("Libro de Socios")

        # Frame_Asociado
        self.datos_asociado = LabelFrame(self.root,
                                         text="Datos del Asociado:", bg="#80ff80")
        self.datos_asociado.grid(row=0, column=0,
                                 columnspan=4, sticky='E')

        # Frame_Consulta
        self.consulta = LabelFrame(self.root,
                                   text="Consulta:", bg="#80ffff")
        self.consulta.grid(row=0, column=4, columnspan=2,
                           rowspan=cant_entries, sticky='NS')

        # Frame_Acciones
        self.acciones = LabelFrame(self.root, text="Acciones:")
        self.acciones.grid(row=cant_entries, column=0,
                           columnspan=8, sticky='S')

        # Frame_Resultados
        self.resultados = LabelFrame(self.consulta, text="Resultados:")
        self.resultados.grid(row=8, column=3, columnspan=2,
                             rowspan=3, sticky='NS')
        for x in range(0, cant_entries):
            Label(self.datos_asociado, text=items_labels[x],
                  bg="#80ff80").grid(row=x, column=0,
                                     columnspan=2, sticky="w")

        # Entrys
        for x in range(0, cant_entries):
            self.items_entries.append(Entry(self.datos_asociado))
            self.items_entries[x].grid(row=x, column=2, columnspan=2)

        # Frame Consulta ---------------:
        self.scroll_consulta = Scrollbar(self.consulta)
        self.consulta_lista = Listbox(
            self.consulta, yscrollcommand=self.scroll_consulta.set,
            height=3, selectbackground="#3385ff")
        for x in range(0, cant_entries):
            self.consulta_lista.insert(x, items_labels[x])
        self.consulta_lista.grid(row=3, column=4, sticky="w")
        self.scroll_consulta.grid(row=3, column=4, sticky="e")
        self.scroll_consulta.config(command=self.consulta_lista.yview)
        self.consulta_entry = Entry(self.consulta)

        # Texto de ayuda en el Entry
        self.consulta_entry.insert(INSERT, placeholder_consulta_entry)
        self.consulta_entry.grid(row=1, column=4, columnspan=2, sticky="EW")

        # modificar el texto de Label a traves de var_consulta_texto
        self.var_texto_consulta = StringVar()
        self.var_texto_consulta.set(placeholder_consulta_label[0])
        self.consulta_texto = Label(
            self.consulta, textvariable=self.var_texto_consulta, bg="#80ffff")
        self.consulta_texto.grid(row=7, column=3, columnspan=2, sticky="S")

        # Frame Resultados ------------:
        self.consulta_texto2 = Label(
            self.resultados, text="Coincidencia N:", bg="#80ffff")
        self.consulta_texto2.grid(row=8, columnspan=4, sticky='es')
        self.resultados_spinbox = Spinbox(
            self.resultados, state=DISABLED, command=self.mostrar_resultados)
        self.resultados_spinbox.grid(row=8, column=4, sticky='ws')

        # Frame Acciones --------------:
        # ---botones
        self.items_botones.append(
            Button(self.acciones, text="Alta", command=self.para_alta))
        self.items_botones.append(
            Button(self.consulta, text="Consulta", command=self.para_consulta))
        self.items_botones.append(
            Button(self.acciones, text="Modificar", command=self.para_modificar))
        self.items_botones.append(
            Button(self.acciones, text="Baja", command=self.para_baja))

        # enlazamos los eventos con los entrys
        self.items_entries[0].bind("<Button-1>", self.clear_entry0)
        self.items_entries[1].bind("<Button-1>", self.clear_entry1)
        self.items_entries[2].bind("<Button-1>", self.clear_entry2)
        self.items_entries[3].bind("<Button-1>", self.clear_entry3)
        self.items_entries[4].bind("<Button-1>", self.clear_entry4)
        self.items_entries[5].bind("<Button-1>", self.clear_entry5)
        self.items_entries[6].bind("<Button-1>", self.clear_entry6)
        self.items_entries[7].bind("<Button-1>", self.clear_entry7)
        self.items_entries[8].bind("<Button-1>", self.clear_entry8)

        # seteos botones
        for x in range(0, len(self.items_botones)):
            self.items_botones[x].grid(
                row=10, column=2*x, sticky="w", columnspan=1)
            self.items_botones[x].config(state=DISABLED)
        self.items_botones[0].config(state=NORMAL)
        self.items_botones[1].grid(row=0, column=3, rowspan=4,
                                   columnspan=1, sticky='ns')
        self.borrar_entrys()

        # prefijar ayudas en entrys _ placeholder
        for x in range(1, cant_entries):  # que no escriba el numero de socio
            self.items_entries[x].insert(0, placeholders_labels_socio[x])
            self.items_entries[x].config(fg="grey")
        # seleccionamos por defecto la opcion Numero de Socio
        self.consulta_lista.selection_set(first=0)
        self.resultados_spinbox.config(state=NORMAL, from_=1,
                                       to=10)  # Iniciamos el SpinBox
        self.resultados_spinbox.config(state=DISABLED)
        # Objeto de la clase Base de Datos
        self.socio = base_de_datos()
        if(not self.socio.tabla_vacia()):
            self.items_botones[1].config(state=NORMAL)
        else:
            respuesta = messagebox.askyesno(title="Base de datos (SOCIOS)",
                                            messagebox='''La base de datos se encuentra vacia.
                    \nDesea cargar sujetos de prueba?''')
            if(respuesta):
                self.socio.socios_de_prueba()

    # Metodo regex_entries()
    # ------------ ----------------
    def regex_entries(self,):
        """
        Controlamos que antes hacer una ALTA o MODIFICAR los 
        datos ingresados en los distintos entries sean coherentes
        con el dato esperado
        """
        try:
            self.var_socio.clear()
            for x in range(1, cant_entries-1):
                self.var_socio.append(self.items_entries[x].get())
                print(re.search(string_patron[x], self.var_socio[x-1]))
                if re.search(string_patron[x], self.var_socio[x-1]) == None:
                    messagebox.showinfo(title="Datos de Socio",
                                        message="No hay coincidencia en: "+str(self.var_socio[x-1]))
                    return FALSE
            # este ultimo no requiere comprobacion
            self.var_socio.append(self.items_entries[8].get())
            return TRUE
        except:
            messagebox.showerror(title="Datos de Socio",
                                 message="Ha habido un error en los entries")

    # Metodo borrar_entrys()
    # ------------ ----------------
    def borrar_entrys(self,):
        """
        Despues de haber realizado alguna operación que nos modifique
        , es decir(Alta, Baja, Modificacion) los datos de algun socio
        limpiamos todos los entries.
        """
        for x in range(0, cant_entries):
            self.items_entries[x].delete(0, "end")

    # Metodo para_alta()
    # ------------ ----------------
    def para_alta(self,):
        """
        Se guarda en la base de datos al nuevo socio.

        Se verifica que tengamos conexion con la base de datos,
        entonces chequeamos que los datos sean los esperados 
        verificando por medio del metodo regex_entries(). 
        Indicamos a la base de datos la operacion de alta y
        los datos del socio; por último se des/habilitan
        botones correspondientes.
        """
        try:
            self.socio.db_conectada()
            if self.regex_entries():
                self.socio.modificar_datos(string_alta_socio, self.var_socio)
                self.items_botones[1].config(state=NORMAL)
                self.resultados_spinbox.config(state=DISABLED)
            else:
                messagebox.showinfo(title="Datos de Socio",
                                    message="Datos Inconsistentes")
        except:
            print("\n***Error dentro de metodo ALTA***\n")
            messagebox.showerror(title="Datos de Socio",
                                 message="Datos Inconsistentes")

    # Metodo para_modificar()
    # ------------ ----------------
    def para_modificar(self,):
        """
        En base a una consulta se modifica el socio seleccionado

        Se chequea la conexion a la base de datos, y se habilita el
        el entry numero de socio asi es seleccionable. Se chequean los
        entrys por medio de regex_entries() y se indica el nuevo cambio
        a la base de datos indicando en caso exito un mensaje al usuario.
        A continuación se borran los entries

        """
        print("Modificar Datos")
        self.socio.db_conectada
        self.items_entries[0].config(state=NORMAL)
        try:
            if(self.regex_entries()):
                self.var_socio.append(self.items_entries[0].get())
                self.socio.modificar_datos(string_modif_socio, self.var_socio)
                self.var_texto_consulta.set(
                    placeholder_consulta_label[5])  # Info de exito
                self.consulta_texto.grid(
                    row=7, column=3, columnspan=2, sticky="S")
                self.resultados_spinbox.config(state=DISABLED)
                self.borrar_entrys()
                self.socio.var_resultado = 0
                self.items_botones[2].config(state=DISABLED)  # boton borrar
                self.items_botones[3].config(state=DISABLED)  # boton borrar
            else:
                messagebox.showinfo(title="Modificacion de Datos",
                                    message="No es posible modificar los datos")
        except:
            messagebox.showerror(title="Modificacion de Datos",
                                 message="Error en base de datos o de Datos Ingresados")

    # Metodo para_consulta()
    # ------------ ----------------
    def para_consulta(self, ):
        """
        Se busca coincidencias en funcion de la categoria y 
        parametro para realizar la busqueda en la base de datos de los
        socios

        Se chequea que la categoria haya sido seleccionada
        y en funcion de categoria y strings de busqueda se realiza
        la consulta a la base de datos, previamente verificando conexion

        En caso de haber coincidencias se llama al metodo
        activar_resultados()
        """
        var_categoria = self.consulta_lista.curselection()
        if len(var_categoria) == 0:
            self.var_texto_consulta.set(placeholder_consulta_label[4])
            self.borrar_entrys()
            self.items_botones[2].config(state=DISABLED)  # boton modificar
            self.items_botones[3].config(state=DISABLED)  # boton borrar
            self.resultados_spinbox.config(state=DISABLED)
        else:
            var_sql_columna = string_busqueda_sql[var_categoria[0]]
            print("La categoria a buscar es: " +
                  str(var_categoria[0]) + " y tu busqueda es: " + self.consulta_entry.get())
            var_consulta = self.consulta_entry.get()
            try:
                self.socio.db_conectada()
                self.socio.consultar_datos(var_sql_columna, var_consulta)
                if len(self.socio.var_resultado) >= 1:
                    self.var_texto_consulta.set(
                        "\n\nHay "+str(len(self.socio.var_resultado))+" coincidencias!\n\n")
                    self.consulta_texto.grid(
                        row=7, column=3, columnspan=2, sticky="S")
                    for x in self.socio.var_resultado:
                        print(x)
                    self.activar_resultados()
                else:
                    self.var_texto_consulta.set(
                        placeholder_consulta_label[3]
                    )
                    self.consulta_texto.grid(
                        row=7, column=3, columnspan=2, sticky="S")
            except:
                messagebox.showerror(title="Consulta de Datos",
                                     message="Error en la Consulta")

    # Metodo para_baja()
    # ------------ ----------------
    def para_baja(self, ):
        """
        Elimina el socio seleccionado.

        Habiendo realizado una busqueda y seleccionado el socio de 
        interes lo borra. Tomando el numero de socio se chequea la
        conexion con DB, se envia la orden de borrado y deshabilitan
        botones de correspondientes. Se exhibe mensaje de borrado 
        exitoso
        """
        print("Dar de baja a Socio")
        self.items_entries[0].config(state=NORMAL)
        var_dato = (self.items_entries[0].get(),)
        self.socio.db_conectada()
        self.socio.modificar_datos(string_baja_socio, var_dato)
        self.borrar_entrys()
        self.items_botones[2].config(state=DISABLED)  # boton modificar
        self.items_botones[3].config(state=DISABLED)  # boton borrar
        self.resultados_spinbox.config(state=DISABLED)
        # Deshabilitamos el n de socio
        self.items_entries[0].config(state=DISABLED)
        messagebox.showinfo(title="Baja de Socio",
                            message="El socio ha sido borrado")

    # Metodo activar_resultados()
    # ------------ ----------------
    def activar_resultados(self,):
        """
        Habiendo coincidencia con lo consultado se habilitan
        botones para desplazarse a traves de los resultados
        y se realiza la primera carga de los socios consultados
        """
        self.resultados_spinbox.config(
            state=NORMAL, from_=1, to=len(self.socio.var_resultado))
        self.resultados_spinbox.grid(row=8, column=4, sticky='ws')

        # activamos el boton modificar y ponemos condicion en alta
        self.items_botones[2].config(state=NORMAL)  # boton modificar
        self.items_botones[3].config(state=NORMAL)  # boton borrar

        # condicion de alta para que no pise lo ya escrito

        # realizamos una primer carga
        self.items_entries[0].config(state=NORMAL)  # habilitamos el n de socio
        self.borrar_entrys()
        for x in range(0, cant_entries):
            self.items_entries[x].insert(0, self.socio.var_resultado[0][x])
            self.items_entries[x].config(fg="black")
        self.items_entries[0].config(state=DISABLED)

    # Metodo mostrar_resultados()
    # ------------ ----------------
    def mostrar_resultados(self,):
        """
        Cada vez que el valor del spinbox es modificado
        se llama a este metodo para actualizar los valores
        de los entrys en funcion de los resultados de la 
        busqueda
        """
        self.items_entries[0].config(state=NORMAL)
        self.borrar_entrys()
        var_spinbox_valor = int(self.resultados_spinbox.get())-1
        print("el valor del indice spinbox es:"+str(var_spinbox_valor))
        for x in range(0, cant_entries):
            self.items_entries[x].insert(
                0, self.socio.var_resultado[var_spinbox_valor][x])
            self.items_entries[x].config()
        self.items_entries[0].config(state=DISABLED)

    # Metodo cerrar_socio()
    # ------------ ----------------
    def cerrar_socio(self,):
        """
        Cierra la conexion con la base de datos
        """
        try:
            self.socio.db_cerrar()
        except:
            print("No se ha podido cerrar correctamente la Base de Datos")
            messagebox.showerror(title="Base de Datos",
                                 message="No se ha podido cerrar correctamente la Base de Datos")

    # Metodos clear_entry0() -----
    # ------------ ----------------
    def clear_entry0(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[0]:
            self.items_entries[0].delete(0, "end")
            self.items_entries[0].config(fg="black")
            self.var_borrado_entry[0] = 0

    # Metodos clear_entry1() -----
    # ------------ ----------------
    def clear_entry1(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[1]:
            self.items_entries[1].delete(0, "end")
            self.items_entries[1].config(fg="black")
            self.var_borrado_entry[1] = 0

    # Metodos clear_entry2() -----
    # ------------ ----------------
    def clear_entry2(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[2]:
            self.items_entries[2].delete(0, "end")
            self.items_entries[2].config(fg="black")
            self.var_borrado_entry[2] = 0

    # Metodos clear_entry3() -----
    # ------------ ----------------
    def clear_entry3(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[3]:
            self.items_entries[3].delete(0, "end")
            self.items_entries[3].config(fg="black")
            self.var_borrado_entry[3] = 0

    # Metodos clear_entry4() -----
    # ------------ ----------------
    def clear_entry4(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[4]:
            self.items_entries[4].delete(0, "end")
            self.items_entries[4].config(fg="black")
            self.var_borrado_entry[4] = 0

    # Metodos clear_entry5() -----
    # ------------ ----------------
    def clear_entry5(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[5]:
            self.items_entries[5].delete(0, "end")
            self.items_entries[5].config(fg="black")
            self.var_borrado_entry[5] = 0

    # Metodos clear_entry6() -----
    # ------------ ----------------
    def clear_entry6(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[6]:
            self.items_entries[6].delete(0, "end")
            self.items_entries[6].config(fg="black")
            self.var_borrado_entry[6] = 0

    # Metodos clear_entry7() -----
    # ------------ ----------------
    def clear_entry7(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[7]:
            self.items_entries[7].delete(0, "end")
            self.items_entries[7].config(fg="black")
            self.var_borrado_entry[7] = 0

    # Metodos clear_entry8() -----
    # ------------ ----------------
    def clear_entry8(self, var_):
        """
            borra el placeholder puesto a modo de 
            ejemplo para el respectivo entry
        """
        if self.var_borrado_entry[8]:
            self.items_entries[8].delete(0, "end")
            self.items_entries[8].config(fg="black")
            self.var_borrado_entry[8] = 0

    # Destructor
    # ------------------------------
    def __del__(self):
        """
        Destructor, cerramos tambien la conexion con la DB
        """
        self.socio.db_cerrar()
        print("Se ha eliminado el objeto y cerrada la DB")
# EOF
