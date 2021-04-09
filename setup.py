import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to drop a database if it exists
dropDatabase = '''DROP DATABASE IF EXISTS CS3800; '''

#Drop database
cursor.execute(dropDatabase)

createDatabase = '''CREATE DATABASE CS3800;'''
cursor.execute(createDatabase)
print("Database created successfully")

dropTable = '''DROP TABLE IF EXISTS police_data;'''
cursor.execute(dropTable)

createTable = ''' CREATE TABLE police_data (
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
print("Created table for police data")

midlands_data = open('crime-data/2021-01/2021-01-west-midlands-street.csv', 'r')
cursor.copy_from(midlands_data, "police_data", sep=",")
print("Police data for the West Midlands has been added")

cambridge_data = open('crime-data/2021-01/2021-01-cambridgeshire-street.csv', 'r')
cursor.copy_from(cambridge_data, "police_data", sep=",")
print("Police data for Cambridge has been added")

#selectData = '''SELECT DISTINCT Falls_within, Crime_type FROM police_data; '''
#cursor.execute(selectData)

#list_tables = cursor.fetchall()

#print(list_tables)

#Closing the connection
conn.close()
