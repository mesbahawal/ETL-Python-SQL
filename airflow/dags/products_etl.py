import pandas as pd
import sqlalchemy as db

## Paths
path_products_table = '/opt/airflow/data/H+ Sport products.xlsx'

## db engine
engine = db.create_engine('postgresql+psycopg2://postgres:pg123@host.docker.internal:5432/ETL')


## main function 
def main():

    ## to create a data frame out of the excel file's data sheet
    products = pd.read_excel(path_products_table, sheet_name="Sheet1")


    ## to discrad any duplicated rows
    products.drop_duplicates()


    ## transform product price in Euros from $
    products["Price"] =  products["Price"]/0.92

    ## load to database
    products.to_sql("products", engine, 
                  if_exists='replace', 
                  index=False)

    print("ETL executed successfully.")