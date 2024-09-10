import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Các cấu hình chính
AIRFLOW_HOME = os.getenv('AIRFLOW_HOME', '/usr/local/airflow')
AIRFLOW_SQL_ALCHEMY_DATABASE_URI = os.getenv('AIRFLOW_SQL_ALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
SPARK_MASTER = os.getenv('SPARK_MASTER', 'local[*]')
DATA_DIR = os.getenv('DATA_DIR', 'data/vnexpress/')
