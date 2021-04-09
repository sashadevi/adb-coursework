import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

city = input("Please enter location where you would like to search (type C for Cambridge or WM for West Midlands): ")

if city == "WM":
    road = input("Please enter a road: ")
    findCrimeType = ''' SELECT DISTINCT Crime_type FROM west_midlands_data WHERE Location = 'On or near ''' + road + '''' ;'''
    cursor.execute(findCrimeType)
    list_tables = cursor.fetchall()
    print("The crime types near this road are:")
    for row in list_tables:
        print(f"{row[0]}")

elif city=="C":
    road = input("Please enter a road: ")
    findCrimeType = ''' SELECT DISTINCT Crime_type FROM cambridge_data WHERE Location = 'On or near ''' + road + '''' ;'''
    cursor.execute(findCrimeType)
    list_tables = cursor.fetchall()
    print("The crime types near this road are:")
    for row in list_tables:
        print(f"{row[0]}")
else:
    print("Sorry, you did not enter a valid location")




conn.close()
