"""
Escribe un
 programa que pida al usuario que ingrese un número entero positivo.
El programa debe mostrar todos los números del 1 hasta el número ingresado, 
uno por uno, utilizando un bucle while."
"""
while True:
    
     numero = int(input("ingrese un numero entero positivo:"))
     if numero >0:
      i=1
      while i>=numero:
       print(i)
       i+=1
      break
     else:
       print("el numero tiene que ser positivo.")