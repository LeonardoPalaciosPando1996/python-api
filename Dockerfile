FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN ls -la /app
RUN cat /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN pip freeze

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]