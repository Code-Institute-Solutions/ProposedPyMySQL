import pymysql

connection = pymysql.connect(host='localhost',
                             user='richardadalton',
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("update friends set age = 22 where name = 'bob'")
        connection.commit()
finally:
    connection.close()