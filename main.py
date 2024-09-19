from etl import extract_and_transform
from db import connect_to_db, create_table, insert_data

# Define your PostgreSQL connection parameters
db_config = {
    # enter your database name , user and password
    'dbname': '',
    'user': '',
    'password': '', 
    'host': 'localhost',
    'port': '5432'
}

# File path to your Excel file
# Enter file path
file_path = ""

# Extract and transform the data
df_transformed = extract_and_transform(file_path)

# Connect to the database
conn = connect_to_db(db_config)

if conn:
    # Create the table
    create_table(conn)
    
    # Insert the transformed data into the table
    insert_data(conn, df_transformed)

    # Close the connection
    conn.close()
