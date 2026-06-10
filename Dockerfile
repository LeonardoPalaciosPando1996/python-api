FROM python:3.11-slim

WORKDIR /app

# 1. copiar requirements primero
COPY requirements.txt /app/requirements.txt

# 2. instalar dependencias
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

# 3. debug real (ESTO ES CLAVE)
RUN python -c "import pandas; print('PANDAS OK')"

# 4. copiar código
COPY . /app

# 5. ejecutar app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]