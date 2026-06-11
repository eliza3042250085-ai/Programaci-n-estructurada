# """
#  Sets.- 
#   Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

#   Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
# """
print("\033c")
set1={"Python,","SQL","Estructurado"}
print(set1)

for i in set1:
    print(i)


set2={"Hola", True, 33, 3.1416}
print(set2)
set2_respaldo=set2.copy


set3={""}
print(set3)

set3.add("Hola")
print(set3)
set3.add("3")
set3.add(10.0)
print(set3)
set3.add(3)
print(set3)

# #Funcnón POP:Quita valores aleatoriamente
set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=lista(conjunto)
print(lista)



#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
       
        #Solucion 1
print("\033c")
lista_emails_UTD=[]
#set_email={""}
opc="S"
while opc=="S":
    lista_emails_UTD.append(input("Ingresa un Email: ").lower().strip())
    #set_email.add(input("Ingresa un Email: ")).lower().strip()
    opc=input("¿Desea ingresar otro: ? (s/n)").lower().strip()
#print(lista_emails_UTD)
set_emails=set(lista_emails_UTD)
#print(set_emails)
lista_emails_UTD=list(set_emails)
print(lista_emails_UTD)

        #Solución 2
print("\033c")
lista_emails_UTD=[]

cont=True
while cont:
    lista_emails_UTD.insert(0, (input("Ingresa un Email: ").strip()))

    opc=input("¿Desea ingresar otro: ? (s/n)").upper().strip()
    if cont=="NO":
         cont=False

set_emails=set(lista_emails_UTD)

lista_emails_UTD=list(set_emails)
print(lista_emails_UTD)

# #Solo son utiles los for al querer mostrar los valores, no son funcionales los while o los forlen() pues no trabajan con posiciones o indices.
  



