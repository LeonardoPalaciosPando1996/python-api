from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RequestData(BaseModel):
    text: str


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
