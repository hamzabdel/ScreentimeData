import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from dotenv import load_dotenv
import os
import transforming_data

load_dotenv()

def connect_to_snowflake():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    return conn

def upload_to_snowflake(df, table_name):
    conn = connect_to_snowflake()
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name.upper())
    print(f"Uploaded success: {success}, rows inserted: {nrows}")
    conn.close()

def main():
    df = pd.read_csv('data/processed/transformed_digital_diet_data.csv')
    upload_to_snowflake(df, "digital_diet_data")

if __name__ == "__main__":
    main()
