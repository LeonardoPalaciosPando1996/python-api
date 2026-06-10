from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from app.model import fit_sarima_series
from app.preprocessing import prepare_series

app = FastAPI(title="SARIMA API")

class RequestData(BaseModel):
    dates: list
    values: list
    steps: int = 12

@app.post("/forecast")
def forecast(req: RequestData):

    df = pd.DataFrame({
        "ds": pd.to_datetime(req.dates),
        "y": req.values
    })

    series = prepare_series(df)
    pred = fit_sarima_series(series, req.steps)

    return {
        "forecast": pred.tolist()
    }