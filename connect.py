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
        # sql = "SELECT albumid, title, artistid FROM Album"
        # sql = "SELECT * FROM Artist"
        sql = "SELECT * FROM Genre"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row['GenreId'])
finally:
    connection.close()
    