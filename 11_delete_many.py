import pymysql

connection = pymysql.connect(host='localhost',
                             user='richardadalton',
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        list_of_names = ['jim', 'bob']
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("delete from friends where name in ({0})".format(format_strings), list_of_names)

        connection.commit()
finally:
    connection.close()