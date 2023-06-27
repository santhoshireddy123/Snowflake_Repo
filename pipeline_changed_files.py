import os
import sys
from snowflake.connector import connect
account = os.environ['SNOWFLAKE_ACCOUNT']
user = os.environ['SNOWFLAKE_USER']
password = os.environ['SNOWFLAKE_PASSWORD']
role = os.environ['SNOWFLAKE_ROLE']
warehouse = os.environ['SNOWFLAKE_WAREHOUSE']
database = os.environ['SNOWFLAKE_DATABASE']
schema = os.environ['SNOWFLAKE_SCHEMA']
changed_sql_files = os.environ['changed_sql_files']


with connect(
    account=account,
    user=user,
    password=password,
    role=role,
    warehouse=warehouse,
    database=database,
    schema=schema,
   ) as connection:
    for sql_file in changed_sql_files:
        with open(sql_file, 'r') as f:
            sql = f.read().split(';')
            for sql_command in sql:
                if sql_command.strip():
                    connection.cursor().execute(sql_command)
            print(f'Executing {sql_file}...')
            print(f'Successfully executed {sql_file}')