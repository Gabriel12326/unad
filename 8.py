"""
Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término,
donde el valor de n lo ingresa el usuario, utilizando un bucle for."
"""
n = int(input("Ingrese cuántos números de Fibonacci desea: "))
a, b = 0,1
for _ in range(n):
 print(a,end = " ") 
 a,b=b,a+b
print()