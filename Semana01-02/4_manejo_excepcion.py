### TRY (Intentalo)
# Si es que falla entonces capturo el error con una excepción 

try: 
    print(10/0)  

except ZeroDivisionError: 
    print('No se puede dividir entre 0')
except Exception as error: 
    # ver que es el causante el error 
    print(error.args)

    # ver
    print(type(error))
    print('Operacion incorrecta')

    #crear una funcion que reciba dos numero y devulva cual es el mayor, si el usuario ingresa un valor que no sea un unmero entonces volver a pedirselo hasta que sa un numero 

# Lambda funciones / funcionaes anonimas 
# funcion no recibe ningun parametro y retorna el valor de 1
# esta funcion ademas no puede tener mas de una linea de codigo
resultado = lambda valor1, valor2, valor3: valor1 + valor2 + valor3 
print(resultado(10,11,12))

def numeroMayor(numero1, numero2) :
    return numero1 if numero1 > numero2 else numero2 

    # psita: utilicen un while, un if y un try-except 
while True:
        try:
            numero1 = int(input('Ingrese el primer numero:'))
            numero2 = int(input('Ingrese el segundo numero:'))
            #resultado = numeroMayor(numero1, numero2)
            resultado = lambda numero1, numero2: numero1 if numero1 > numero2 else numero2 
            print('El numero mayor es {}'.format(resultado(numero1, numero2)))
            break
        except: 
            print('Tienes que ingresar solo numeros')