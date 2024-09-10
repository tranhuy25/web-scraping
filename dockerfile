# Sử dụng Python làm image base
FROM python:3.9-slim

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    default-jre \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt PySpark
RUN pip install pyspark==3.4.0

# Cài đặt Airflow và các dependency
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code dự án vào container
COPY . /app
WORKDIR /app

# Command để khởi động Airflow
CMD ["airflow", "scheduler"]
