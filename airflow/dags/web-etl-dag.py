from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 10),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'vnexpress_etl',
    default_args=default_args,
    description='ETL VNExpress Data with PySpark',
    schedule_interval=timedelta(days=1),
)

# Task 1: Thu thập dữ liệu từ VNExpress
def scrape_vnexpress():
    import requests
    from bs4 import BeautifulSoup
    import os

    # URL trang chủ VNExpress
    url = ""
    
    # Gửi request tới VNExpress
    response = requests.get(url)
    
    # Tạo BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Thu thập tiêu đề các bài viết từ trang chủ
    articles = soup.find_all('h3', class_='title-news')
    
    # Tạo danh sách để lưu trữ các bài viết
    data = []
    for article in articles:
        title = article.get_text(strip=True)
        link = article.a['href']
        data.append(f"{title} - {link}")
    
    # Ghi dữ liệu vào file
    with open('/path/to/data/vnexpress/articles.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)

scrape_task = PythonOperator(
    task_id='scrape_vnexpress',
    python_callable=scrape_vnexpress,
    dag=dag,
)

# Task 2: Xử lý dữ liệu với PySpark
def run_pyspark():
    subprocess.run(["spark-submit", "/path/to/pyspark_jobs/vnexpress_processing.py"])

spark_task = PythonOperator(
    task_id='process_vnexpress',
    python_callable=run_pyspark,
    dag=dag,
)

# Task 3: Gửi email báo cáo
send_email = BashOperator(
    task_id='send_email',
    bash_command='echo "ETL job for VNExpress completed!" | mail -s "ETL Report" admin@example.com',
    dag=dag,
)

# Set up the task pipeline
scrape_task >> spark_task >> send_email
