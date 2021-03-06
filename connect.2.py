# import pymysql.cursors
import pymysql

# connect to the database
connection = pymysql.connect(host = 'localhost',
                             user = 'tomd100',
                             password = '',
                             db = 'Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:    
        data = ("Bob", 21, "1990-01-01")
        cursor.execute('insert into Friends values (%s,%s,%s)', data)
        connection.commit()
        
        cursor.execute('select * from Friends')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
finally:
    connection.close()
    