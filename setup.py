import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''DROP DATABASE IF EXISTS CS3800; ''';

#Creating a database
cursor.execute(sql)

newSql = '''CREATE DATABASE CS3800;'''
cursor.execute(newSql)
print("Database created successfully........")

dropTable = '''DROP TABLE IF EXISTS police_data;'''
cursor.execute(dropTable)

createTable = ''' CREATE TABLE police_data (
Crime_ID VARCHAR,
Month DATE,
Reported_by VARCHAR,
Falls_within VARCHAR,
Longitude DOUBLE PRECISION,
Latitude DOUBLE PRECISION,
Location VARCHAR, 
LSOA_code CHAR(9), 
LSOA_name VARCHAR,
Crime_type VARCHAR,
Last_outcome_category VARCHAR,
Context VARCHAR
); '''

cursor.execute(createTable)
print("Created table!")

#Closing the connection
conn.close()
