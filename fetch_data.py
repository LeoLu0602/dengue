import pymssql
import csv

SERVER = '140.116.214.181:1433'
USER = 'uclab'
PWD = 'uclabDB2022'
DB = 'sinopac_data'
QUERY = 'SELECT TOP 10 [店家類別], lat, lng FROM [飲食店家]'

conn = pymssql.connect(server=SERVER, user=USER, password=PWD, database=DB)  
cursor = conn.cursor()  
cursor.execute(QUERY)
row = cursor.fetchone()  
with open("data.csv", "w", newline='') as csv_file:  # Python 3 version    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)    