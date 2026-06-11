"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["Canada","Mexico","EUA","México","Brasil"]
numeros=[23,45,8,24]
varios=["hola",3.1416, 33, True]
vacia=[]


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacia)

#Imprimir nombre en pantalla con la posición
print(paises[0])

#Recorrer la lista 
#1er forma 
#i trae el valor de cada posicion que toma, por eso no se ocupa range. Guarda valor
for i in paises:
    print(i)

# #2do forma 
#Guarda posición con i al principio.Se ocupa cunado conoce el tamaño de tu lista
for i in range(0, 5):
    print(paises[i])

#SE usa cuando no se conoce el tamalo de l aestructura y que se quiera adaptar
for i in range(0,len()):
    print(paises[i])


#ordenar elementos de una lista


#dar la vuelta a una lista




#Agregar, insertar, Añadir un elemento a una lista
#1er forma 


#2da forma


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
#Funcion pop que pide parameteos y te regresa toda la lista.Se debe conocer la poscion a querer borarr para que sea automatico

paises.pop(4)
print(paises)

#2da forma 
#Funcion que permite borra un elemnto indicando el Valor.También borra elementos repetidos.
paises.remove("EUA")
print(paises)


#Buscar un elemento dentro de la lista.Regresa TRUE OR FALSE
resp="Brasil" in paises
print(resp)


   #Forma mas comun al ser una condición. 
if "Brasil" in paises:
    print("La respuesta es True")
else:
    print("La respuesta es False")

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
num=int(input("Dame un número: "))
cuantos=numeros.count(num)
print(f"El número de veces que aparece el {num} es {cuantos}")



    #Ordenarlos
numeros.sort()
print(numeros)


#Conocer la posicion o indice en el que se encuentra un elemento de la lista.Solo busca uno, para encontrar el mismo en distinas posiciones se usa un ciclonumeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
posicion=numeros.index(100)
print(f"La posicón del numero es: {posicion}")

#Unir el contenido de una lista dentro de otra lista.Loa grega al final
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
numeros2=[500,1000]
print(numeros2)
numeros.extend(numeros2)
print(numeros)


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros=[23,45,8,24,100,200,0,-1,-10,23,24,8,23,50]
print(numeros)
numeros2=[500,1000]
print(numeros2)
numeros.extend(numeros2)
print(numeros)

print()
numeros.reverse()
print(numeros)


