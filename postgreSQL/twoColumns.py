import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimesByCrimeType() :
    crimes_by_type = '''SELECT Falls_within, Crime_type, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    cursor.execute(crimes_by_type)
    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByLocation():
    query = '''SELECT Falls_within, Location, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Location ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    cursor.execute(query)

    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByLSOA():
    query = '''SELECT Falls_within, LSOA_name, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, LSOA_name ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    cursor.execute(query)

    list_tables = cursor.fetchall()

    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByOutcome():
    crimes_by_outcome = '''SELECT Falls_within, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Last_outcome_category ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    cursor.execute(crimes_by_outcome)
    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

crimesByCrimeType()
crimesByLocation()
crimesByLSOA()
crimesByOutcome()

conn.close()