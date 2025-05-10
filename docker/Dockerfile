FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt update && apt install -y postgresql-client
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

