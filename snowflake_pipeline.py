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

def run_query(connection,sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()

warehouse_sql = 'use warehouse {}'.format(warehouse)
run_query(conn, warehouse_sql)

sql = 'use database {}'.format(database)
run_query(conn, sql)

sql = 'use schema {}'.format(schema)
run_query(conn, sql)


sql_folder = './sql_scripts'

with conn.cursor() as cursor:
    for file_name in os.listdir(sql_folder):
        if file_name.endswith('.sql'):
            with open(os.path.join(sql_folder, file_name), 'r') as f:
                sql_commands = f.read().split(';')
                for sql in sql_commands:
                    if sql.strip():
                        cursor.execute(sql)








