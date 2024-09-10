from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import vnexpress_scraper
import vnexpress_processing

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'vnexpress_etl',
    default_args=default_args,
    description='ETL DAG for VNExpress data',
    schedule_interval='@daily',
)

def extract():
    vnexpress_scraper.main()

def transform_load():
    vnexpress_processing.main()

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_load_task = PythonOperator(
    task_id='transform_load',
    python_callable=transform_load,
    dag=dag,
)

extract_task >> transform_load_task
