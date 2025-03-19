"""
Escribe un programa que pida al usuario un número entero positivo. 
El programa debe contar cuántos dígitos tiene el número utilizando un bucle while."
"""
numero=int(input("ingrese un numero positivo:"))
while numero <=0:
    numero=int(input("ingrese un numero positivo:"))
  
contador=0
i = numero

while i >0:
  i//=10
  contador+=1
print(f"el numero {numero} tiene {contador} digitos.")