from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
intento = 3

class Reset(BaseModel):
    reset: str
def limitar_ejecuciones(func):
    def wrapper():
        global intento
        print(intento)
        if intento > 5:
            raise HTTPException(status_code=429, detail="Demasiadas peticiones")
        intento += 1
        return func()
    return wrapper

@app.get('/')
def home():
    return {'message': 'Bienvenido'}

@app.get('/consultar')
@limitar_ejecuciones
def peticion():
    return {'message': 'peticion aceptada'}

@app.get('/consultar2')
@limitar_ejecuciones
def peticion2():
    return {'message': 'peticion aceptada'}

@app.post('/reset')
def reset_peticion(reset:Reset):
    global intento
    intento = 0
    return {'type': reset.reset}