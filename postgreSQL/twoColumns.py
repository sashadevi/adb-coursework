import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimesByCrimeType(crime_type):
    if crime_type == "":
        crimes_by_type = '''SELECT Falls_within, Crime_type, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    else:
        crimes_by_type = "SELECT Falls_within, Crime_type, COUNT(Crime_type) FROM police_data WHERE Crime_type = '" + crime_type + "' GROUP BY Falls_within, Crime_type ORDER BY Falls_within, COUNT(Crime_type) DESC; "
    cursor.execute(crimes_by_type)
    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByLocation(location):
    if location == "":
        query = '''SELECT Falls_within, Location, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Location ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    else: 
        query = "SELECT Falls_within, Location, COUNT(Crime_type) FROM police_data WHERE Location = 'On or near " + location + "' GROUP BY Falls_within, Location ORDER BY Falls_within, COUNT(Crime_type) DESC; "
    cursor.execute(query)

    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByLSOA(LSOA_name):
    if LSOA_name == "":
        query = '''SELECT Falls_within, LSOA_name, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, LSOA_name ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    else:
        query = "SELECT Falls_within, LSOA_name, COUNT(Crime_type) FROM police_data WHERE LSOA_name = '" + LSOA_name + "' GROUP BY Falls_within, LSOA_name ORDER BY Falls_within, COUNT(Crime_type) DESC;"
    
    cursor.execute(query)

    list_tables = cursor.fetchall()

    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

def crimesByOutcome(outcome):
    if outcome == "":
        crimes_by_outcome = '''SELECT Falls_within, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Last_outcome_category ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
    else: 
        crimes_by_outcome = "SELECT Falls_within, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '" + outcome + "' GROUP BY Falls_within, Last_outcome_category ORDER BY Falls_within, COUNT(Crime_type) DESC;"
    
    cursor.execute(crimes_by_outcome)
    list_tables = cursor.fetchall()
    for row in list_tables:
        print(f"{row[0]} {row[1]} {row[2]}")

#crimesByCrimeType()
# crimesByLocation()
# crimesByLSOA()
# crimesByOutcome()

