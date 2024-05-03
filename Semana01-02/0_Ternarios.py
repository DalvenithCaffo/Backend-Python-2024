### Operador TERNARIO
# Condicion que sirve para ejecutarse en una sola linea y en base a la condicion RETORNARA un valor y otro

# Si el usuario es PERUANO pagara 5 soles si es EXTRANJERO pagara 8 soles. 
nacionalidad = 'ECUATORIANO'

if nacionalidad == 'PERUANO':
    print('Pague 5 soles')
else: 
    print('Pague 8 soles')

#       RESULTADO SI ES VERDADERO if CONDICIONAL(ES)  else RESULTADO SI ES FALSE
resultado = 'Pague 5 soles' if nacionalidad == 'PERUANO' else 'Pague 8 soles'
print(resultado)