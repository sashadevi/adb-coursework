import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='hai', password='12345678', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#creating a cursor object using the cursor() method
cursor = conn.cursor()

def crimes_by_outcome():
 crimes_by_outcome = '''SELECT Falls_within, Last_outcome_category, COUNT(Crime_type) FROM police_data GROUP BY Falls_within, Last_outcome_category ORDER BY Falls_within, COUNT(Crime_type) DESC; '''
 cursor.execute(crimes_by_outcome)
 list_tables = cursor.fetchall()
 for row in list_tables:
    print(f"{row[0]} {row[1]} {row[2]}")
 
crimes_by_outcome()
