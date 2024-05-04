from flask import Flask, request

# __name__ > variable de python que sirve para indicar si el archivo que estamos utilizando es el archivo principal del proyecto esto sirve para que la instancia de flask solamente corra en el archivo principal y asi evitar instancias de flask en archivos secundarios del proyecto

app = Flask(__name__) # es el encargado de crear mi servidor del backend 
## request > donde se almacenara toda la informacion de la peticion actual del cliente 
# cada vez que el cliente realice una peticion toda esa informacion se almacenara en el request

# si el archivo es el archivo principal el valor de __name__ sera __main__ 


### Decoradores:
# Sirve para utilizar un metodo sin la necesidad de modificarlo desde la clase en la cual estamos haciendo la referencia

# GET > DEVOLVER 
# POST > CREACIONES 
# PUT > ACTUALIZACIONES
@app.route('/', methods = ['GET','POST','PUT'])
def inicio():
    #request.method > devolvera el metodo http que esta realizando el cliente 
    if request.method == 'PUT': 
        return{
        'message':'Actualizacion exitosa.'
        }, 202 #estado de respuesta http (Accepted)
    elif request.method == 'GET':
        return{
        'message':'Devolucion exitosa.'
        }, 200 #ok
    elif request.method == 'POST':
        return{
        'message':'Creacion exitosa.'
        }, 201 #Created
    
    print(request.method)
    return{
        'message':'Bienvenidos a mi primera API con Flask.',
        'content':'Hola'
        }


# levantamos nuestro servidor de flask 
app.run(debug=True)