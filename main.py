from postgreSQL.twoColumns import *
from postgreSQL.threeColumns import *
from postgreSQL.fourColumns import *
from postgreSQL.fiveColumns import *
from postgreSQL.all_crime_types import *
from options import *

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

keyWord = ''

print("Welcome, this application compares police data in January 2021 for the West Midlands and Cambridge")
while keyWord != 'q':

    keyWord = input("Please enter an option. If you would like to see all options press 'h'. If you want to quit, press 'q': ")

    if keyWord == "1":
        allCrimeTypes()

    elif keyWord == "2":
        crime_type = input("Please enter the crime type. Press 'enter' if you would like to view all crimes by crime type: ")
        crimesByCrimeType(crime_type)

    elif keyWord == "3":
        location = input("Please enter a Point of Interest. Press 'enter' if you would like to view all crimes by Points of Interest: ")
        crimesByLocation(location)

    elif keyWord == "4":
        lsoa_name = input("Please enter a LSOA name. Press 'enter' if you would like to view all crimes by LSOA name: ")
        crimesByLSOA(lsoa_name)

    elif keyWord == "5":
        outcome = input("Please enter an outcome category. Press 'enter' if you would like to view all crimes by outcome category: ")
        crimesByOutcome(outcome)

    elif keyWord == "6":
        location = input("Please enter a location. Press 'enter' if you would like to view all locations: ")
        crime_type = input("Please enter crime type. Press 'enter' if you would like to view all crime types: ")
        crimesByCrimeTypeLocation(crime_type, location)

    elif keyWord == "7":
        crime_type = input("Please enter crime type. Press 'enter' if you would like to view all crime types: ")
        outcome = input("Please enter an outcome category. Press 'enter' if you would like to view all outcomes: ")
        crimesByTypeOutcome(crime_type, outcome)

    elif keyWord == "8":
        location = input("Please enter a location. Press 'enter' if you would like to view all locations: ")
        outcome = input("Please enter an outcome category. Press 'enter' if you would like to view all outcomes: ")
        crimesByLocationOutcome(location, outcome)

    elif keyWord == "9":
        outcome = input("Please enter an outcome category. Press 'enter' if you would like to view all outcomes: ")
        lsoa = input("Please enter a LSOA name. Press 'enter' if you would like to view all LSOA names: ")
        crimesByLSOAOutcome(lsoa, outcome)

    elif keyWord == "10":
        crimesByCrimeTypeLocationLSOA()
    
    elif keyWord == "11":
        crimesByTypeLocationOutcome()
    
    elif keyWord == "12":
        crimesByCrimeTypeLSOAOutcome()
    
    elif keyWord == "13":
        locationLSOAOutcome()

    elif keyWord == "14":
        crimesByCrimeTypeLocationLSOAOutcome()
    
    elif keyWord == "q":
        keyWord = 'q'

    elif keyWord == "h":
        printOptions()

conn.close()
