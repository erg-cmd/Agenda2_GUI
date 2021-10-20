#####################################################################
# CONTROL.PY --------------------------------------------------------
# Main - Aplicacion en Python para manejar la cartera
# de socios de un Club. Desde aqui llamamos a vista.py y este a su vez
# a db.py para manipular Base de Datos(MYSQL).
#####################################################################

from tkinter import Tk
from tkinter import messagebox
from vista import LibroSociosVista


class LibroSocios:
    """
    #LibroSocios:
        crea / conecta a la base de datos (MySQL) por medio
        de la clase socio e inicia la interfaz gráfica
        por medio de TKINTER. Opcion de crear / modificar / 
        consultar / eliminar socios.
    """

    def __init__(self, window):
        """
        #__init_:
        constructor de LibroSocios
        """
        self.ventana = window
        LibroSociosVista(self.ventana)


if __name__ == "__main__":
    try:
        root = Tk()
        App = LibroSocios(root)
        root.mainloop()
    except:
        print('Ha ocurrido un error', __name__)
        messagebox.showerror(title="Datos de Socio",
                             message="Ha habido un error en los entries")
    finally:
        print("\n*** Programa finalizado ***\n")
# EOF
