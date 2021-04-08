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

dropTable = '''DROP TABLE IF EXISTS west_midlands_data;'''
cursor.execute(dropTable)

dropTable1 = '''DROP TABLE IF EXISTS cambridge_data;'''
cursor.execute(dropTable1)

createTable = ''' CREATE TABLE west_midlands_data (
Crime_ID VARCHAR,
Month VARCHAR,
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

midlands_data = open('crime-data/2021-01/2021-01-west-midlands-street.csv', 'r')
cursor.copy_from(midlands_data, "west_midlands_data", sep=",")
print("Police data for the West Midlands has been added!")

createTable = ''' CREATE TABLE cambridge_data (
Crime_ID VARCHAR,
Month VARCHAR,
Reported_by VARCHAR,
Falls_within VARCHAR,
Longitude VARCHAR,
Latitude VARCHAR,
Location VARCHAR, 
LSOA_code CHAR(9), 
LSOA_name VARCHAR,
Crime_type VARCHAR,
Last_outcome_category VARCHAR,
Context VARCHAR
); '''

cursor.execute(createTable)
print("Created table!")

cambridge_data = open('crime-data/2021-01/2021-01-cambridgeshire-street.csv', 'r')
cursor.copy_from(cambridge_data, "cambridge_data", sep=",")
print("Police data for Cambridge has been added!")

# selectData = '''SELECT * FROM police_data; '''
# cursor.execute(selectData)

print("Data has been added to table!")

#list_tables = cursor.fetchall()

#print(list_tables)

#Closing the connection
conn.close()
