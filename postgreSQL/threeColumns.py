import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimesByCrimeTypeLocation():
	crimesByCrimeTypeLocation = '''SELECT Falls_within, Crime_type, Location, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Location ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByCrimeTypeLocation)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
        

def crimesByTypeOutcome(): 
	crimesByTypeOutcome = '''SELECT Falls_within, Crime_type, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Last_outcome_category ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByTypeOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


def crimesByLocationOutcome() :
	crimesByLocationOutcome = '''SELECT Falls_within, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY 	Falls_within, Location, Last_outcome_category ORDER BY Falls_within, Location, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByLocationOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
       
        
def crimesByLSOAOutcome():
	crimesByLSOA = '''SELECT Falls_within, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, LSOA_name, Last_outcome_category ORDER BY Falls_within, LSOA_name, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByLSOA)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


crimesByCrimeTypeLocation()
crimesByTypeOutcome()
crimesByLocationOutcome()
crimesByLSOAOutcome()

