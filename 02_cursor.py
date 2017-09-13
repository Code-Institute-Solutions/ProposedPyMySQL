# import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='richardadalton',
                             password='',
                             db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre"
        cursor.execute(sql)
        rows = cursor.fetchall()  
        for row in rows:
            print(row)
finally:
    connection.close()