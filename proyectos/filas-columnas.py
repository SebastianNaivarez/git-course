try:
    fila = int(input("¿Cuantas filas quieres?: "))
    columnas = int(input("¿Cuantas columnas quieres?: "))
    simbolo = input("Ingrese un simbolo: ")

    for i in range(fila):
     for j in range(columnas):
          print(simbolo, end="")
     print()    
except ValueError:
    print("Por favor introducir numeros!")