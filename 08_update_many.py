import pymysql

connection = pymysql.connect(host='localhost',
                             user='richardadalton',
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        data = [
                (23, 'bob'),
                (24, 'jim'),
                (25, 'fred')
            ]
        rows = cursor.executemany("update friends set age = %s where name = %s", data)
        connection.commit()
finally:
    connection.close()