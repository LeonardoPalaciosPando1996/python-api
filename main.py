from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RequestData(BaseModel):
    text: str


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }


@app.post("/process")
def process(data: RequestData):

    resultado = data.text.upper()

    return {
        "original": data.text,
        "resultado": resultado
    }


@app.post("/sum")
def sum_numbers(data: Numbers):

    return {
        "resultado": data.a + data.b
    }