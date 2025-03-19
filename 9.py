"""
Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle
while. El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
"""
n=int(input("ingrese un numero:"))

factorial=1
while n >0:
    factorial *= n
    n -= 1
print(f"el factorial de {n} es {factorial}")