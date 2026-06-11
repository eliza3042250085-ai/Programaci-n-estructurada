print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[10,34,25,45]
print(numeros)

 #PRIMERA FORMA
lista="["
for i in numeros:
    lista+=f"{i}, "
print(f"{lista}]")

 #SEGUNDA FORMA
lista="["
for i in range(0, len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"{lista}]")

 #TERCERA FORMA
lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1
print(f"{lista}]")

                  # f"{}"" se puede usar para calcular cosas. No solo en el print

#opc="si"

#while opc=="si":
#    numeros=int(input("Ingrese un número: "))
#    numeros.append(numeros)
#    opc=input("¿Desea ingresar otro: ? si/no").lower().strip()
#print(numeros)

 


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["UTD","segundo","TI","MTI"]
print(palabras)
palabra=input("Dame una palabra a buscar: ").strip()

  #PRIMER FORMA
#in hace que palabra este dentro de palabras.Solo lo hace una vez
if palabra in palabras:
    print("Encontramos la palabra en la lista c:")
else:
    print("No está la palabra a buscar :c")


  #2DA FORMA
encontre=False
for i in palabras:
    if i==palabra:
        encontro=True
if encontro:
    print("Encontré la palabra en la lista c:")
else:
    print("No encontré la palabra en la lista c:")


  #3er FORMA
for i in range(0, len(palabras)):
    if palabras[i]==palabra:
          encontro=True
if encontro:
    print("Encontré la palabra en la lista c:")
else:
    print("No encontré la palabra en la lista c:")


encontro=False
i=0
while i<len(palabras):
     if palabras[i]==palabra:
          encontro=True
          i+=1
if encontro:
    print("Encontré la palabra en la lista c:")
else:
    print("No encontré la palabra en la lista c:")



#Ejemplo 3 Añadir elementos a la lista
  #Versión 1
lista=[]

true=True
while true:

    dato=input("Ingrese un valor para la  lista: ").strip().upper()
    lista.append(dato)
    true=input("¿Deseas añadir más elementos a la lista?(si/no)").lower().strip()
    if true=="no":
        true=False

#   Versión 2
true="si"
while true=="si":
    dato=input("Ingrese un valor para la  lista: ").strip().upper()
    lista.append(dato)
    true=input("¿Deseas añadir más elementos a la lista?(si/no)").lower().strip()

print(lista)

  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
         ["Carlos", "6181234567"],
         ["Alberto","6182344567"],
         ["Martin","6181231223"],
       ]
print(agenda)

for i in agenda:
    print(i)


for c in range(0,2):
    for r in range(0,3):
        print(agenda[r],[c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print("["+lista+"]")