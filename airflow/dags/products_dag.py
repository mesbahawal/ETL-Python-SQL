from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from products_etl import main
## from airflow.providers.standard.operators.bash import BashOperator

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime(2026, 1, 1),
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=3),
}

dag = DAG(
	'products_full_load',
	default_args=default_args,
	description='My Products Table ETL DAG',
	schedule='@daily'
)


run_etl = PythonOperator(
	task_id='run_etl',
	python_callable=main,
	dag=dag
)

run_etl
