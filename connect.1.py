# import pymysql.cursors
import pymysql

# connect to the database
connection = pymysql.connect(host = 'localhost',
                             user = 'tomd100',
                             password = '',
                             db = 'Chinook')

try:
    # with connection.cursor() as cursor:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:    
        cursor.execute('drop table if exists Friends')
        cursor.execute('create table Friends(name char(20), age int, DOB datetime)')
finally:
    connection.close()
    