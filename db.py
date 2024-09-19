import psycopg2
from psycopg2 import sql

# Function to connect to PostgreSQL
def connect_to_db(db_config):
    try:
        conn = psycopg2.connect(**db_config)
        print("Connected to PostgreSQL database!")
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Function to create the table if it doesn't exist
def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS addresses (
        house_no VARCHAR(50),
        city VARCHAR(100),
        state_code VARCHAR(10),
        zip_code VARCHAR(20),
        lat FLOAT,
        lng FLOAT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully!")
    cursor.close()

# Function to insert data into the table
def insert_data(conn, df_transformed):
    cursor = conn.cursor()
    insert_query = '''
    INSERT INTO addresses (house_no, city, state_code, zip_code, lat, lng)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    for index, row in df_transformed.iterrows():
        cursor.execute(insert_query, (row['house_no'], row['city'], row['state_code'], row['zip_code'], row['lat'], row['lng']))
    conn.commit()
    print("Data inserted successfully!")
    cursor.close()
