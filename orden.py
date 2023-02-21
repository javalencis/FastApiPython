from fastapi import FastAPI


appq = FastAPI()


#El orden en la declaración de las funciones es importante, ya que las operaciones de path son evaluadas en orden
@appq.get('/users/me')
async def read_user_me():
    return {"user_id":"the current user"}

@appq.get('/users/{user_id}')
async def read_user(user_id:str):
    return {"user_id": user_id}
