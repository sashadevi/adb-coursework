import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimesByCrimeTypeLocationLSOA():
	crimesByCrimeTypeLocationLSOA = '''SELECT Falls_within, Crime_type, Location, LSOA_name, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Location, LSOA_name ORDER BY Falls_within, Crime_type, Location, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByCrimeTypeLocationLSOA)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")


def crimesByTypeLocationOutcome():
	crimesByTypeLocationOutcome = '''SELECT Falls_within, Crime_type, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Location, Last_outcome_category ORDER BY Falls_within, Crime_type, Location, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByTypeLocationOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")


def crimesByCrimeTypeLSOAOutcome():
	crimesByCrimeTypeLSOAOutcome = '''SELECT Falls_within, Crime_type, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, LSOA_name, Last_outcome_category ORDER BY Falls_within, Crime_type, LSOA_name, COUNT(Crime_type) DESC; '''
	cursor.execute(crimesByCrimeTypeLSOAOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")


def locationLSOAOutcome():
	locationLSOAOutcome = '''SELECT Falls_within, Location, LSOA_name, Last_outcome_category, COUNT(Location) FROM police_data GROUP BY Falls_within, Location, LSOA_name, Last_outcome_category ORDER BY Falls_within, Location, LSOA_name, COUNT(Location) DESC; '''
	cursor.execute(locationLSOAOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")

