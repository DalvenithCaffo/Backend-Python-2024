alumnos = ['Angel','Bryan','Carlos','Hiroito','Claudia','Samuel', 'Marco']

for alumno in alumnos:
    print(alumno)
print('----------------------------------')
# for se puede utilizar con string (textos) 
frase = 'No hay mal que por bien no venga'


for letra in frase:
    print(letra)
print('----------------------------------')
# ejercicio - imprimir las letras sin el espacio. 
for letra in frase: 
    if letra !=' ': 
        print(letra)
print('----------------------------------')
# Forma 2 - imprimir las letras sin el espacio. 
for letra in frase: 
    if letra ==' ': 
        continue    
    print(letra)
    
# Forma 3, Operador TERNARIO solo se puede colocar en sus resultados PALABRAS NO CLAVE
# None > Nada / nadie
# Para definir una variable y esta no queremos colocarle un valor inicial podemos usar la palabra None
# Si no queremos realizar nada en un operador ternario podemos colocarlo ahí 
print('----------------------------------')
for letra in frase:
    None if letra ==' ' else print(letra) 

print('----------------------------------')
### Range
# Range > si quiero realizar un for manual sin uso de listas, tuplas, set o textos 
# range(limite) > el for se ejecutara hasta que el valor sea menor que el tope
for numero in range(4):
    print(numero)

print('----------------------------------')
#Range(Inicio, limite) , siendo el ultimo valor menor al tope
for numero in range(1,4):
    print(numero)
print('----------------------------------')
#range(inicio, limite, incremento/decremento)
for numero in range(1,10,2):
    print(numero)

print('----------------------------------')
#ejercicio 01 de bucles
texto = 'hola me llamo eduardo'
vocales = ['a','e','i','o','u']
print( 'j' in vocales)
print( 'e' in vocales)

#iterar la varibale textos y ver cuatas vocales hay
# respuesta: 9

#Incrementador 
contador = 0 
for letra in texto:
        if letra in vocales:
            #al valor anterior del contador le sumamos 1
            contador = contador + 1

print('Hay ',contador, ' vocales')
print('Hay {} vocales'.format(contador))
print(f'Hay {contador} vocales')
print('Hay %s vocales' % (contador))

# Ejercicio 02 - como saber si un numero es par o impar 
# 
contador = 0
for numero in range(1,56):
    if numero % 2 ==0:
        contador +=1

print('Hay ', contador,' numeros pares')
