from flask import Flask
from flask import render_template
import pandas as pd
import sqlite3

app = Flask(__name__)

# c = conn.cursor()
# c.execute('select * from albums')
# res = c.fetchfirst()
# print(res)
# c.close()




@app.route('/')
def hello_world():
    conn = sqlite3.connect('/home/nadav/Desktop/db_example/chinook.db')
    df = pd.read_sql_query("select * from albums limit 5;", conn)
    data=df.to_html()
    return render_template('index.html',data=df)

