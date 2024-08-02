# Calculando el IMC de una persona
def calculadora():
    try:
        user_peso = float(input("Ingrese su peso en kilos: "))
        user_altura = float(input("Ingrese su altura en metros: "))
        
        imc = user_peso / user_altura**2
        
        if imc < 18.5:
            print("Bajo peso")
        elif 18.5 <= imc < 24.9:
            print("Peso normal")
        elif 25 <= imc < 29.9:
            print("Sobrepeso")
        elif imc >= 30:
            print("Obesidad")
    except ValueError:
        print("Por favor no introducir un valor no numerico!")
    except ZeroDivisionError:
        print("No existe 0 metros")
        
calculadora()
        