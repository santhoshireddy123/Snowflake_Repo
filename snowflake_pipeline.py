import os
import snowflake.connector

conn = snowflake.connector.connect(
        user=os.environ["SNOWFLAKE_USER_ENV"],
        password=os.environ["SNOWFLAKE_PASSWORD_ENV"],
        account=os.environ["SNOWFLAKE_ACCOUNT_ENV"],
        role=os.environ["SNOWFLAKE_ROLE_ENV"],
        warehouse=os.environ["SNOWFLAKE_WAREHOUSE_ENV"],
        database=os.environ["SNOWFLAKE_DATABASE_ENV"],
        schema=os.environ["SNOWFLAKE_SCHEMA_ENV"],
    )


warehouse = os.environ["SNOWFLAKE_WAREHOUSE_ENV"]
database = os.environ["SNOWFLAKE_DATABASE_ENV"]
schema = os.environ["SNOWFLAKE_SCHEMA_ENV"]

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


sql = 'create or replace table empl(id integer,name varchar);'
run_query(conn, sql)


