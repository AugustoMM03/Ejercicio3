from manejadorRegistro import ManejadorRegistro as MR
from menu import MenuOpciones

def test():

    contolador = MR()
    contolador.cargarArchivo()
    menu = MenuOpciones()
    menu.opciones(contolador)



if __name__ == "__main__":
    test()