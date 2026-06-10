from statsmodels.tsa.statespace.sarimax import SARIMAX

def fit_sarima_series(series, steps=12):

    model = SARIMAX(
        series,
        order=(1,1,1),
        seasonal_order=(1,1,1,12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    res = model.fit(disp=False)

    forecast = res.forecast(steps=steps)

    return forecast