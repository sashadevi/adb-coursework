import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimesByCrimeTypeLocation(crime_type, location):
	if crime_type == "" and location == "":
		crimesByCrimeTypeLocation = '''SELECT Falls_within, Crime_type, Location, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Location ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC; '''
	elif crime_type == "" and location != "":
		crimesByCrimeTypeLocation = "SELECT Falls_within, Crime_type, Location, COUNT(Crime_type) FROM police_data WHERE Location = 'On or near " + location + "' GROUP BY Falls_within, Crime_type, Location ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	elif crime_type != "" and location == "":
		crimesByCrimeTypeLocation = "SELECT Falls_within, Crime_type, Location, COUNT(Crime_type) FROM police_data WHERE Crime_type = '" + crime_type + "' GROUP BY Falls_within, Crime_type, Location ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	else:
		crimesByCrimeTypeLocation = "SELECT Falls_within, Crime_type, Location, COUNT(Crime_type) FROM police_data WHERE Location = 'On or near " + location + "' AND Crime_type = '" + crime_type + "' GROUP BY Falls_within, Crime_type, Location ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	cursor.execute(crimesByCrimeTypeLocation)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
        

def crimesByTypeOutcome(crime_type, outcome):
	if crime_type == "" and outcome == "":
		crimesByTypeOutcome = '''SELECT Falls_within, Crime_type, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Crime_type, Last_outcome_category ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC; '''
	elif crime_type == "" and outcome != "":
		crimesByTypeOutcome = "SELECT Falls_within, Crime_type, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '" + outcome + "' GROUP BY Falls_within, Crime_type, Last_outcome_category ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	elif crime_type != "" and outcome == "":
		crimesByTypeOutcome = "SELECT Falls_within, Crime_type, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Crime_type = '" + crime_type + "' GROUP BY Falls_within, Crime_type, Last_outcome_category ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	else:
		crimesByTypeOutcome = "SELECT Falls_within, Crime_type, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Crime_type = '" + crime_type + "' AND Last_outcome_category = '" + outcome + "' GROUP BY Falls_within, Crime_type, Last_outcome_category ORDER BY Falls_within, Crime_type, COUNT(Crime_type) DESC;"
	cursor.execute(crimesByTypeOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


def crimesByLocationOutcome(location, outcome):
	if location == "" and outcome == "":
		crimesByLocationOutcome = '''SELECT Falls_within, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY 	Falls_within, Location, Last_outcome_category ORDER BY Falls_within, Location, COUNT(Crime_type) DESC; '''
	elif location == "" and outcome != "":
		crimesByLocationOutcome = "SELECT Falls_within, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '"+ outcome +"' GROUP BY Falls_within, Location, Last_outcome_category ORDER BY Falls_within, Location, COUNT(Crime_type) DESC; "
	elif location != "" and outcome == "":
		crimesByLocationOutcome = "SELECT Falls_within, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Location = 'On or near " + location + "' GROUP BY Falls_within, Location, Last_outcome_category ORDER BY Falls_within, Location, COUNT(Crime_type) DESC; "
	else:
		crimesByLocationOutcome = "SELECT Falls_within, Location, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '"+ outcome +"' AND Location = 'On or near " + location + "' GROUP BY Falls_within, Location, Last_outcome_category ORDER BY Falls_within, Location, COUNT(Crime_type) DESC; "
	cursor.execute(crimesByLocationOutcome)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
       
        
def crimesByLSOAOutcome(lsoa, outcome):
	if lsoa == "" and outcome == "":
		crimesByLSOA = '''SELECT Falls_within, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, LSOA_name, Last_outcome_category ORDER BY Falls_within, LSOA_name, COUNT(Crime_type) DESC; '''
	elif lsoa == "" and outcome != "":
		crimesByLSOA = "SELECT Falls_within, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '" + outcome + "' GROUP BY Falls_within, LSOA_name, Last_outcome_category ORDER BY Falls_within, LSOA_name, COUNT(Crime_type) DESC; "
	elif lsoa != "" and outcome == "":
		crimesByLSOA = "SELECT Falls_within, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE LSOA_name = '" + lsoa + "' GROUP BY Falls_within, LSOA_name, Last_outcome_category ORDER BY Falls_within, LSOA_name, COUNT(Crime_type) DESC; "
	else:
		crimesByLSOA = "SELECT Falls_within, LSOA_name, Last_outcome_category, COUNT(Crime_type) FROM police_data WHERE Last_outcome_category = '" + outcome + "' AND LSOA_name = '" + lsoa + "' GROUP BY Falls_within, LSOA_name, Last_outcome_category ORDER BY Falls_within, LSOA_name, COUNT(Crime_type) DESC; "
	cursor.execute(crimesByLSOA)
	list_tables = cursor.fetchall()
	for row in list_tables:
		print(f"{row[0]} {row[1]} {row[2]} {row[3]}")


# crimesByCrimeTypeLocation()
# crimesByTypeOutcome()
# crimesByLocationOutcome()
# crimesByLSOAOutcome()

