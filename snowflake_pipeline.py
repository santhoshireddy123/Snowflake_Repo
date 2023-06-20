import os
import snowflake.connector

conn = snowflake.connector.connect(
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        role=os.environ["SNOWFLAKE_ROLE"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
        database=os.environ["SNOWFLAKE_DATABASE"],
        schema=os.environ["SNOWFLAKE_SCHEMA"],
    )

warehouse = os.environ["SNOWFLAKE_WAREHOUSE"]
database = os.environ["SNOWFLAKE_DATABASE"]
schema = os.environ["SNOWFLAKE_SCHEMA"]

def run_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()

def snowflake_context(warehouse, database, schema):
    warehouse_sql = 'use warehouse {}'.format(warehouse)
    run_query(conn, warehouse_sql)

    sql = 'use database {}'.format(database)
    run_query(conn, sql)

    sql = 'use schema {}'.format(schema)
    run_query(conn, sql)

snowflake_context(warehouse,database,schema)


sql = 'create or replace table customer_incremental (id integer,name varchar)'
run_query(conn, sql)


