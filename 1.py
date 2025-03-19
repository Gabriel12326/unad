"""
Escribe un
 programa que pida al usuario que ingrese un número entero positivo.
El programa debe mostrar todos los números del 1 hasta el número ingresado, 
uno por uno, utilizando un bucle while."
"""
numero = int(input("ingrese un numero entero positivo: "))
while numero <=0:
      print("el numero tiene que ser positivo.")
      numero = int(input("ingrese un numero entero positivo: "))
   

i=1
while i<=numero:
 print(i)
 i+=1
