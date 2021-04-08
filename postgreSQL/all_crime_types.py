import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

crime_types = input("To find out all crime types in the West Midlands and Cambridge enter 'all crime types': ");
if crime_types == "all crime types":
	
	#select the different crime types from west midlands table
	midlands_crime_types = '''SELECT DISTINCT Crime_type FROM west_midlands_data; '''

	#select the different crime types from cambridge table
	cambridge_crime_types = '''SELECT DISTINCT Crime_type FROM cambridge_data;'''

	#execute query
	cursor.execute(midlands_crime_types, cambridge_crime_types)

	list_crime_types = cursor.fetchall()
	print(list_crime_types)
else : 
	print("command not found")










