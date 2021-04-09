from postgreSQL.twoColumns import *

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

crime_type = input("Please enter the crime type. Press 'enter' if you would like to leave this blank: ")
crimesByCrimeType(crime_type)

location = input("Please enter a Point of Interest. Press 'enter' if you would like to leave this blank: ")
crimesByLocation(location)

lsoa_name = input("Please enter a LSOA name. Press 'enter' if you would like to leave this blank: ")
crimesByLSOA(lsoa_name)

outcome = input("Please enter an outcome category. Press 'enter' if you would like to leave this blank: ")
crimesByOutcome(outcome)


conn.close()