import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('camino.db')
    conn.row_factory = sqlite3.Row # 這行能讓妳用 row['name'] 而不只是 index
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    desserts = conn.execute('SELECT * FROM desserts').fetchall()
    conn.close()
    return render_template('index.html', desserts=desserts)

if __name__ == '__main__':
    app.run(debug=True)