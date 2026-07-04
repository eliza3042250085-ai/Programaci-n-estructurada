import funciones


def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR CARACTERISTICAS A UNA PELICULA ::::...\n")
    caracteristica=input("Ingresa la caracteristica: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis) > 0:
        print("\tCaracterística\t\tValor")
        for i in pelis:
            print(f"\t{i}\t\t{pelis[i]}")
        funciones.espereTecla()
    else:
        input("\n\t...¡No existe ninguna característica en la película, verifique! ....")

def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS lAS CARACTERÍSTICAS DE LA PELICULA ::::...\n") 
     if len(pelis)>0:
         opc=""
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las características de la película (Si/No)? ").lower().strip()
         if opc=="si":
             pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen características que borrar, verifique! ....")
    


def borrarPeliculas(pelis):
    print("\t\t....:::: BORRAR PELICULAS ::::...\n")   
    peli = input("Escribe el nombre de la pelicula: ").lower().strip()
    if peli in pelis:
        opc = input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
        while opc != "si" and opc != "no":
            opc = input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip() 
        if opc == "si":
            pelis.remove(peli)
            funciones.accionExitosa()
    else:
        input("\n\t...¡No existe esa película en el registro! ....")


def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR CARACTERÍSTICA DE LA PELICULA ::::...\n")   
    caracteristica = input("Escribe el nombre de la característica: ").lower().strip()
    noencontro = True
    for i in pelis:
        if caracteristica == i:
            noencontro = False 
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas modificar la película (Si/No)? ").lower().strip()
            if opc == "si":
                pelis[i] = input("Escribe el nuevo valor: ").upper().strip()
                funciones.accionExitosa()
    if noencontro:
        input("\n\t...¡No existe la característica que andas buscando!...")

def buscarPeliculas2(pelis):
    print("\t\t ¡BUSCAR CARACTERÍSTICA DE LA PELICULA!\n")
    caracteristica = input("Escribe el nombre de la característica: ").lower().strip()
    noencontro = True
    for i in pelis:
        if caracteristica == i:
            print("\tCaracterística\t\tValor")
            print(f"\t{i}\t\t\t{pelis[i]}")
            noencontro = False   
    funciones.espereTecla()
    if noencontro:
        input("\n\t...No existe esa característica!...")

	


 


