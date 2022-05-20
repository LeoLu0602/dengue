import pymssql

SERVER = '140.116.214.181:1433'
USER = 'uclab'
PWD = 'uclabDB2022'
DB = 'sinopac_data'

conn = pymssql.connect(server=SERVER, user=USER, password=PWD, database=DB)  
cursor = conn.cursor()  
cursor.execute('SELECT TOP 30 [店家類別], lat, lng FROM [飲食店家]')
row = cursor.fetchone()  
while row:  
    print(row)  
    row = cursor.fetchone()    