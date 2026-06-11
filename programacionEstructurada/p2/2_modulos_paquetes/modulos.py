# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")
borrarPantalla()


def funcion1():
    nombre = input("Ingresa tu nombre: ").strip().upper()
    apellido = input("Ingresa tu apellido: ").strip().upper()
    print(f"Hola soy {nombre} {apellido}")

funcion1()

def funcion3(nom, ape):
   nombre = nom.strip().upper()
   apellido = ape.strip().upper()
   print(f"Hola mucho gusto soy {nombre} {apellido}")

funcion3()


def funcion2():
    nombre = input("Ingresa tu nombre: ").strip().upper()
    apellido = input("Ingresa tu apellido: ").strip().upper()
    return nombre, apellido

funcion2()

def funcion4(nom, ape):
    nombre = nom.strip().upper()
    apellido = ape.strip().upper()
    return nombre, apellido
funcion4()
