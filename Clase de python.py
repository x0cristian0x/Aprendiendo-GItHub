#Variables logicas
3<2 or 4<5 #Basta con una de ellas sea verdad para que nos arroge True 
3<6 and 4<5 #Es necesario que ambas condiciones se cumplan para que sea True
not 3>5 #Otro variable logica.


#Se puede cambiar de un string a un int, float o bool(Todo distinto de cero(0)
# es TRUE)
float("13")+12 #Nos devuelve un float
int("13")+12 #Nos devuelve una entero
a=str(4)+str(5) # Esto es 45, pero es string
bool("0") # Esto es True, porque es string
str(4+5)+" segundos" # Nos devuelve la suma y lo convierte en str

##Para print
print("El","tesoro","esta","escondido",sep="..")#Con sep separaa con ..

##Como saludar
usuario=int(input("dime tu edad ")) #Si nose coloca int, sera un str
dias=365*usuario #Se tiene que seleccionar todo el programa
print("tu haz vivido",dias)

#Recordar bien el white
x=0
while x<4:
    print(x)
    x=x+1
else: print("listo")

#Recordar la secuencia range(inicio,fin,paso)
for i in range(5,11,2):
        print(i)
        
for i in range(10):
    print('hola mundo')


x=3
if x>5:   #Recuerda el elif, Tb se puede añadir "and if" o "or ir" a la condicion
    print("hola") 
else:     #Recordar que siempre se inicia con "if" y luego se puede usar el "elif"
    print("chau")  # o "else"

    
# Realiza un exponente de 3 si es par y si es impar 2, 
def exponenciacion(numero): #Las variables dentro de una funcion, no existen
  resultado = numero        #en el entorno de python, entonces "resultado" no
  if resultado %2==0:
    return resultado       #exite. Pero si una variable del entorno puede
  else:                     #afectar el resultado de una funcion si llevan el mismo 
    resultado=resultado**2  #nombre ejm: y=4 def num(x):print(x*y)
  return resultado          #por tanto tener cuidado. Se lo conoce como Scope


#Formas de IMPORTAR
import math   #1er metodo importa todo sus elementos
from math import sin ,sqrt #2Do Ahora  solamente importara los 2 elementos
from math import sqrt as raiz #3er. Con esto le damos un nombre al elemento sqrt
 #Como se UTILIZA LOS PAQUETES IMPORTADOS
math.sqrt(9) #1er Metodo. Siempre se comienza con el nombre del paquete
sin(60) #2do Metodo, solamente se utiliza el elemento de la libreria que se importa
raiz(9) #3er Metodo, al haber asignado un alias a sqrt, se utiliza ese alias



#STRING El uso
a="helado"
b=a+"chocolate" #b almacena puede tener variables string
print(b[0:5+1]) #Con los "[]" puede obtener las letras de las variable
#Los espacion tb se toma encuenta, tb se puede añadir operaciones aritmeticas
#"\n" para imprimir en otra linea."\\" para q aparezca una "\" al imprimir
print(b.lower()) #Escribira todo en minuscula, tb se usar asi "hola".lower()
print(b.upper()) #Escribira todo en mayuscula
print(b.strip("h"))#Remueve la letras del inicio o final
print(b.replace("chocolate","vainilla"))# reemplaza un texto por otro


s = input("Ingresa una palabra: ")
resultado = ""
i = 0
x=5
while i<len(s):
  resultado= resultado + s[len(s)-i-1]
  i=i+1
print(resultado)


#ABRIR un Archivo con open, el 2do parametro indicar si read con "r" o write
#con "w"., por default es read "r". No olvidar el ".txt"
import os #Luego "os.getcwd()" y veras donde esta el directorio de python
x=open("Documents\\Cursos de Coursera\\Python\\d.txt","r")
a=x.readlines() #Con el comando "readlines" se lee los txt
#Con "os.chdir()" cambias de directorio


def ocurrencias(string):
    a=str(string)
    b=len(a)
    e=0
    f=0
    for i in range(b):
        d=a[i]
        if d=="1":
            e=e+1
        elif d=="0":
            f=f+1
    return e-f

ocurrencias("11000110101")








