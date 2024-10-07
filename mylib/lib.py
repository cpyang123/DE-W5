import pandas as pd
from sqlalchemy import create_engine

# Create an SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///example.db')

def create_connect_database(db_name: str):
    return create_engine('sqlite://./database/' + db_name)

def load_dataframe(df_path):
    return pd.read_csv(df_path)

# Write the data into a new SQLite table (replace or append mode)
def load_to_table(dataframe, name, connection):
    dataframe.to_sql(name, con=connection, if_exists='replace', index=False)

def select_all(table_name, connection):
    return connection.execute("SELECT * FROM " + table_name).fetchall()



# Verify by querying the table
with engine.connect() as conn:
    result = conn.execute("SELECT * FROM table_name LIMIT 5").fetchall()
    for row in result:
        print(row)
