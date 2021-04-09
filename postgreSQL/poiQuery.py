import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

POI = input("Please enter a point of interest: ")

findCrimeType = ''' SELECT DISTINCT Crime_type FROM west_midlands_data WHERE Location = 'On or near ''' + POI + '''' ;'''
findCrimeTypeCambridge = ''' SELECT DISTINCT Crime_type FROM cambridge_data WHERE Location = 'On or near ''' + POI + '''' ;'''
cursor.execute(findCrimeType, findCrimeTypeCambridge)

list_tables = cursor.fetchall()
print("The different types of crimes near this point of interest are:")
for row in list_tables:
    print(f"{row[0]}")



conn.close()
