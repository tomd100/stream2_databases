# import pymysql.cursors
import pymysql

# connect to the database
connection = pymysql.connect(host = 'localhost',
                             user = 'tomd100',
                             password = '',
                             db = 'Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = cursor.execute('update Friends set name = "Tom" where name = "Henry"')
        connection.commit()
        cursor.execute('select * from Friends')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
finally:
    connection.close()
    