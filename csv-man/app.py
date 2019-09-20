from flask import Flask
from flask import render_template
from flask import url_for
import pandas as pd
import sqlite3

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db_path = '/home/nadav/Desktop/db_example/chinook.db'
# c = conn.cursor()
# c.execute('select * from albums')
# res = c.fetchfirst()
# print(res)
# c.close()


@app.route('/')
def hello_world():
    conn = sqlite3.connect(db_path)
    albums = pd.read_sql_query("select * from albums limit 5;", conn)
    albums.reset_index(drop=True, inplace=True)
    tracks = pd.read_sql_query("select * from tracks limit 5;", conn)
    artists = pd.read_sql_query("select * from artists limit 5;", conn)
    return render_template('index.html', albums=albums,
                           tracks=tracks, artists=artists)
