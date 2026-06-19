from sqlalchemy import create_engine

host = 'localhost'
port = 5432
user = 'postgres'
password = 'NadeeP00'
db_name = 'store_db'

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')


def load_to_postgres(df, table_name):
    df.to_sql(
        table_name,
        engine,
        if_exists='replace',
        index=False
    )

    print('Data loaded to PostgreSQL successfully')