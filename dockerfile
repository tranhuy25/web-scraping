FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    default-jre \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pyspark==3.4.0

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8080

CMD ["airflow", "scheduler"]
