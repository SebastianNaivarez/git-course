# Calculadora de dos numeros
print("Caluladora de dos numeros!")
try:
    numero1 = float(input("Primer numero: "))
    numero2 = float(input("Segundo numero: "))
    operacion = input("¿Que opereacion realizar? (+ , - , * , /)")

    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    if resultado.is_integer():
        print(int(resultado))  
    else:
        print(resultado)  
except ValueError:
    print("Por favor Ingresar numeros!")