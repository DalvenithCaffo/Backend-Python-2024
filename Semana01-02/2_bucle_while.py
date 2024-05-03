# while puede convertise en un bucle infinito 

numero = 20
# while se ejecutara hasta que la condicion sea verdadera
# while primero valida la condicion y luego ejecuta el codigo 
# en Python no existe el do-while 
while numero < 20:
    print('Hola')
    print(numero)
    numero = numero + 1

# recibiendo valores
#valor = input('Porfavor ingresa un numero: ')
#print(valor)

# juego adivina un numero 
numero = 75 
numero_adivinado = 0 
while numero_adivinado != numero:
    numero_adivinado = int(input('Pro favor ingresa un numero: '))
    if numero_adivinado < numero: 
        print('El numero es Mayor!')
    elif numero_adivinado == numero:
        print('Felicidades Acertaste!')
    else:
        print('El numero es Menor!')


# si queremos salir de un bucle for o while infinito usamos BREAK
while True: 
    print('Hola Mundo')
    break

