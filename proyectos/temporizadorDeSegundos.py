import time
pedir_usuario = int(input("¿Cuantos segundos quisieras poner en el temporizador?: "))

for i in range(pedir_usuario, 0 , -1):
    print(i)
    time.sleep(1)
    
print("El temporadizador ha terminado!")