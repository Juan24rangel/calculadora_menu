# calculadora con menu

from math import log

print("---------------------------")
print("----CALCULADORA - MENU-----")
print("---------------------------")

#input
bandera = False
x = float(input("Digite el valor de x: "))
y = float(input("Digite el valor de y: "))

print("\nDame la opcion de deseas realizar: \n")

# Se despliega el menu para seleccionar la opcion que deseas realizar
print("1. sumar (el primero mas el segundo)")
print("2. restar (el primero menos el segundo)")
print("3. multiplicar (el primero por el segundo)")
print("4. dividir (el primero entre el segundo)")
print("5. potencia (el primero a la potencia del segundo)")
print("6. logaritmo (el logaritmo del primero)")

opcion = int(input("\nDame la opcion: "))

# processing

if(opcion==1):
    z=x+y
    print(x,"+",y)
elif(opcion==2):
    z=x-y
    print(x,"-",y)
elif(opcion==3):
    z=x*y
    print(x,"*",y)
elif(opcion==4 and y!=0):
    z=x/y
    print(x,"/",y)
elif(opcion==4 and y==0):
    print("El denominador es igual a cero y")
    print("NO se puede realizar la division.")
    bandera = True
elif(opcion==5):
    z=pow(x,y)
    print(x,"^",y)
elif (opcion==6 and x>0):
    z = log(x)
    print("Logaritmo de", x)
elif(opcion==6 and x<=0):
    print("el valor de x es menor o igaul a cero y")
    print("NO se puede calcular el logaritmo.")
    bandera = True
else:
    print("Opcion no valida")
    
# se escribe el resultado con otra condicion

if (opcion<7 and bandera==False):
    print("Resultado:", z)
    
#fin