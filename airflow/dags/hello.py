from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG("hello_world", start_date=datetime(2026, 1, 1), schedule=None, catchup=False):
    BashOperator(task_id="hello", bash_command="echo Hello from Airflow")