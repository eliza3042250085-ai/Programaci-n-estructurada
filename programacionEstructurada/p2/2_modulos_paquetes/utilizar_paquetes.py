from paquete1 import modulos, modulo_paquete
modulos.borrarPantalla()

nom="Juan"
ape="Polainas"

edad=modulo_paquete.solicitarEdad()

nombre, apellidos=modulos.funcion4(nom, ape)
print(f"Nombre: {nombre}\nApellidos:  {apellidos}\nEdad: {edad}")

