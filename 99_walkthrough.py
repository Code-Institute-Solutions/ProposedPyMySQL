#!/usr/bin/env python
import os
from flask import Flask, render_template
import pymysql

app = Flask(__name__)


def do_select(sql):
    # Get the username from the Cloud9 workspace
    # (modify this variable if running on another environment)
    username = os.getenv('C9_USER')

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user=username,
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
    return render_template("index.html",
                           artists=do_select("SELECT * FROM Artist;"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
