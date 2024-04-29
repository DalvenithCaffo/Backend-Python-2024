#+ Puedo agrupar varios valores en una variable 

### LISTAS
# Que se puede modificar, es ordenada (maneja indices)

alumnos = ['Dalvenith Aurelio Caffo', 'Diana Elizabeth Olarte', 'Diana Valentina Caffo', 'Diana Elizabeth Caffo']

# Las listas empiezan con la posicion 0 
print(alumnos[0])
print(alumnos[3])

# Para saber el contenido (longitud) de datos
print(len(alumnos))

# Para saber el contenido (longitud) de datos
print(alumnos[-2])

# Para agregar elementos a una lista ya creada 
alumnos.append("Chinchin Mascota Oficial")
print(alumnos)

# Remover un elemento de la lista lo podemos guardar en una variable 
alumno_eliminado = alumnos.pop(0)
print(alumnos)
print(alumno_eliminado)

# Del > podemos eliminar variables, eliminar posiciones de la lista y otras cosas 
del alumnos[3]
print(alumnos)
# Cada vez que se elimina una posicion de la lista, todas las demas posiciones ocupan ese lugar disponible 

# Modificar el valir de una posicion de una lista 
alumnos[0] = 'Diana Elizabeth Olarte Paitan'
print(alumnos)

# Limpiamos toda la lista y la dejamos vacia 
alumnos.clear() 
print(alumnos)

# Las listas pueden contener varios tipos de datos 
mixto = ['Lunes', 10, False, 80.5, [1, 2, 3]]


# -- Ejercicio 
ejercicio = [1,2,3, [4, 5, 6]]
# Devolver el valor de 3 
print(ejercicio[2])
# como puedo devolver el valor de 5
sub_lista = ejercicio[3]
print(sub_lista[1])

# -- o tambien 
print(ejercicio[3][1])


### TUPLAS 
# No se puede modificar y es ordenada (indices)
# Se usa para guardar valores que jamas van a poder cambiar

meses = ('Enero','Febrero', 'Marzo', 'Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

print(meses[0])

data = ('Juan', 'Roberto', [1,2,3,['Eduardo','Frank']])
# Obtener Eduardo
print(data[2][3][0])

### SET (Conjuntos)
# Desordenada y modificable
colores = {'Negro','Blanco', 'Guinda', 'Violeta'}

print(colores)
colores.add('Azul')
print(colores)

print('Verde' in colores) # Flase, el color Verde no se encuentra en colores

colores.remove('Blanco')
print(colores)

### DICCIONARIOS
# Ordenados pero por llaves y modificables 
persona = {
    'nombre':'Dalvenith',
    'edad':31,
    'nacionalidad':'Peruano',
    'apellido':'Caffo'
}

print(persona.keys()) # Llaves
print(persona.values()) # Valroes
print(persona['edad'])
# print(persona['edades']) # JAVASCRIPT si no existe me retorna undefined, aca lanza error.

persona['nombre'] = 'Dalvenith Aurelio'
persona['hobbie'] = 'Futboll' # Si la llave no existe, la crea. 

print(persona)


# + Ejecicio

ejercicioDiccionario = {
    'nombre' : "Roberto",
    'edad': 40,
    'hobbies': ['Nada','Pescar','Jugar videojuegos'],
    'idiomas': [
        {
            'nombre':'Ingles',
            'nivel':'Intermedio'
        },
        {
            'nombre':'Frances',
            'nivel':'Basico'
        }
    ],
    'habilidades':{'Puntual','Economico','Proactivo'},
    'debilidades':('Mentiroso','Resentido','Comelon')
}

# Dame la Edad
print(ejercicioDiccionario['edad'])

# Mostrar los hobbies
print(ejercicioDiccionario['hobbies'])

# Mostrar el ultimo hobbie ingresado
print(ejercicioDiccionario['hobbies'][-1])

# Mostrar los idiomas SOLO SUS NOMBRE
print(ejercicioDiccionario['idiomas'][0]['nombre'])
print(ejercicioDiccionario['idiomas'][1]['nombre'])

# Ver si es Proactivo
print('Proactivo' in ejercicioDiccionario['habilidades'])

# Ver cuantas debilidades tiene (cantidad)
print(len(ejercicioDiccionario['debilidades']))