"""
Escribe un programa que pida al usuario un número entero positivo y luego imprima
todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.
"""

numero = int(input("digite un numero entero positivo:"))
while numero <= 0:
    numero = int(input("digite un numero entero positivo:"))
i=1

while i <= numero:
    print(i)
    i+=2