from fastapi import FastAPI #importamos la clase FastAPI que provee toda la funcionalidad de la API

app = FastAPI()  #Creamos su una instancia de FastAPI

#crear una operación de path
#path en la manera principal de separar los "intereses" y los "recursos"
#Operación se referie a uno de los metodos HTTP
#Los mas comunes: POST, PUT, GET, DELETE 
#Los mas exóticos: OPTIONS, HEAD,  PATCH, TRACE
#@ 'decorador' se pone encima de una función y hace algo con ella
#Aqui estamos diciendo a FastAPI que el path "/" usa la operación GET
@app.get('/') 
#esta es nuetsra función de la operación de path
#sera llamada cada vez que reciba un request en la URL "/" usando una operación GET
async def root(): #Función asincrona
    return {"message":"Hello Word"} #retorno de la función
