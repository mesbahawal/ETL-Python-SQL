import pandas as pd
import sqlalchemy as db

## Paths
path_orders_table = '/opt/airflow/data/H+ Sport orders.xlsx'

## db engine
engine = db.create_engine('postgresql+psycopg2://postgres:pg123@host.docker.internal:5432/ETL')


## main function 
def main():

    ## to create a data frame out of the excel file's data sheet
    orders = pd.read_excel(path_orders_table, sheet_name="data")


    ## to discrad any duplicated rows
    orders.drop_duplicates()


    ## to drop columns set the list of column-names here
    orders = orders.drop(columns=['CustomersComment','SalespersonsComment'])

    ## load to database
    orders.to_sql("orders", engine, 
                  if_exists='replace', 
                  index=False)

    print("ETL executed successfully.")