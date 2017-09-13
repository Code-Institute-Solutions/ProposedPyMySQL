from flask import Flask, render_template
import pymysql

app = Flask(__name__)



def do_select(sql):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='richardadalton',
                                 password='',
                                 db='Chinook')

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
                
    finally:
        connection.close()




@app.route('/')
def get_artists():
    return render_template("index.html", artists=do_select("select * from Artist"))
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)