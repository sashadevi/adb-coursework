import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

crimeType=input("Please enter a crime type: ")

select_outcome_category= "SELECT MAX(Last_outcome_category) FROM west_midlands_data WHERE Crime_type = '"+ crimeType + "';"
select_outcome_category1= "SELECT MAX(Last_outcome_category) FROM cambridge_data WHERE Crime_type = '"+ crimeType + "';"
cursor.execute(select_outcome_category, select_outcome_category1)

list_tables = cursor.fetchall()
for row in list_tables:
    print("The most popular outcome type for this crime is: " + f"{row[0]}")


conn.close()