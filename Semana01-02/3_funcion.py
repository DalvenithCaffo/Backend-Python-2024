### FUNCIONES
# toda funcion puede recibir parametros
# toda funcion puede devolver un resultado 

def Saludar(): 
    print('Hola buenas noches!')

# Si la funcion esta definida pero no esta siendo implementada (llamada) el código dentro de la funcion nunca se ejecutara 
Saludar()

def Sumar(numero1, numero2):
    resultado = numero1 + numero2 
    print('La suma es:',resultado)

Sumar(10,20)

def Multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

resultado_multiplicacion = Multiplicar(50,20)
print(resultado_multiplicacion)

# Si no queremos pasar algun valor (parametro) de la funcion.
# Si queremos pasar un parametro por defecto, siempre van al final de la declaracion de la funcion. 
def saludarCordialmente(nombre, cargo='Señor'):
    return 'Buenas noches {} {}'.format(cargo, nombre)

print(saludarCordialmente('Dalvenith'))
print(saludarCordialmente('Dalvenith','Caffo'))

print(saludarCordialmente(cargo='Gerente', nombre='Dalvenith'))

# el * al momento de definir una funcion idincaremos que esta pueda recibir n valores
def sumarNumeros(*args):
    resultado = 0
    # devolver la sumatoria de todos los valores que recibe el args
    for numero in args:
        # resultado = resultado + numero
        resultado +=numero
    return resultado

resultado = sumarNumeros(10,20,30,40,50,60,70,80,90,110)
print(resultado)

# el ** srive para recibir un numero ilimitado de parametros 
def caputarPersona(**kwargs): 
    return kwargs

caputarPersona(nombre='Dalvenith'
            , apellido='caffo'
            , correo='dcffa86@gmail.com'
            , estatus = 1.72
            )
