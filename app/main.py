from fastapi import FastAPI, HTTPException
from app.models import Operacao
import app.operations as operations

app = FastAPI()

@app.post("/soma")
def rota_soma(valores: Operacao):
    resultado = operations.soma(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/subtracao")
def rota_subtracao(valores: Operacao):
    resultado = operations.subtracao(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/multiplicacao")
def rota_multiplicacao(valores: Operacao):
    resultado = operations.multiplicacao(valores.a, valores.b)
    return {"resultado": resultado}

@app.post("/divisao")
def rota_divisao(valores: Operacao):
    try:
        resultado = operations.divisao(valores.a, valores.b)
        return {"resultado": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/exponenciacao")
def rota_exponenciacao(valores: Operacao):
    resultado = operations.exponenciacao(valores.a, valores.b)
    return {"resultado": resultado}