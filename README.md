Web Scraping ETL Project
This project involves scraping data from websites, processing it using PySpark, and managing the entire ETL (Extract, Transform, Load) process with Apache Airflow.

Contents
Requirements
Environment Setup
Running the Project
Configuration
Project Structure
References
Requirements
Docker and Docker Compose
Python 3.9
Environment Setup
Clone the Repository
git clone <URL_OF_YOUR_REPOSITORY>
cd big_data_project
Install Docker
Ensure that you have Docker and Docker Compose installed. You can download and install Docker from the official Docker website.

Create .env File
Create a .env file in the config/ directory with the following content, and replace the values with your actual information:
plaintext
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
DB_HOST=localhost
DB_PORT=5432
DB_USER=your-username
DB_PASSWORD=your-password
DB_NAME=web_log_db
Install Dependencies
Build the Docker image and install dependencies by running:

docker-compose build
Running the Project
Start the Services
Start the services using Docker Compose:

docker-compose up
The PostgreSQL service will run PostgreSQL to store data.
The Airflow service will run Apache Airflow to manage the ETL process.
Access Apache Airflow
Open a browser and go to http://localhost:8080 to access the Apache Airflow interface. Log in with the default credentials airflow/airflow.

Monitor DAG
In the Airflow interface, you will see the vnexpress_etl DAG. Activate this DAG to start the ETL process.

Configuration
Dockerfile: Configuration to create the Docker image for the project, including PySpark and Apache Airflow.
docker-compose.yml: Configuration for the services, including PostgreSQL and Airflow.
vnexpress_etl_dag.py: Defines the ETL process using Airflow.
vnexpress_processing.py: Processes the collected data using PySpark.
requirements.txt: List of dependencies required for the project.
Project Structure
airflow/dags/: Contains Airflow DAGs.
config/: Contains configuration files and environment variables.
data/: Directory for data collected from VNExpress.
pyspark_jobs/: Contains PySpark code for data processing.
requirements.txt: List of libraries to install.
Dockerfile: Dockerfile to create the Docker image.
docker-compose.yml: Docker Compose configuration to manage services.
References
Apache Airflow Documentation
PySpark Documentation
BeautifulSoup Documentation
Requests Documentation






