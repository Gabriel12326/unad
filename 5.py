"""
Escribe un programa que pida al usuario un número entero y luego imprima todos los 
números desde ese número hasta el 0 en orden descendente utilizando un bucle while."
"""

numero=int(input("digite un numero entero positivo:"))
while numero <=0:
   numero=int(input("digite un numero entero positivo:"))
    
while numero>=0:
    print(numero)
    numero-=1