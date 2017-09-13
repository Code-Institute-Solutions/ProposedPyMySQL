import pymysql

connection = pymysql.connect(host='localhost',
                             user='richardadalton',
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("delete from friends where name = %s", 'bob')
        connection.commit()
finally:
    connection.close()