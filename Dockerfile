FROM python:3.11-slim

WORKDIR /app

# copiar SOLO requirements primero (evita cache raro)
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# ahora copiar código
COPY app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]