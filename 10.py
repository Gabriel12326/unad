"""
Escribe un programa que pida al usuario ingresar una contraseña y repita la 
solicitud mientras la contraseña ingresada sea incorrecta.
El programa debe continuar hasta que el usuario ingrese la contraseña correcta.
Utiliza una estructura whilepara simular un do while.
"""
contraseña_correcta=input("Define la contraseña:")
while True:
     contraseña =input("digite la contraseña:")
     
     if contraseña == contraseña_correcta:
       print("contraseña correcta. iniciando seccion.")
       break
     else:
      print("contraseña incorrecta. acceso denegado.")
    
    