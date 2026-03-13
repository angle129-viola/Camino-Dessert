from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 建立一個小工具，幫我們處理資料庫連線
def get_db_connection():
    conn = sqlite3.connect('camino.db')
    conn.row_factory = sqlite3.Row  # 啟動「標籤法」，讓妳可以用名稱抓資料
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    # 執行 SQL 抓所有甜點
    desserts = conn.execute('SELECT * FROM desserts').fetchall()
    conn.close()
    return render_template('home.html', desserts=desserts)

@app.route('/admin')
def admin():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM desserts').fetchall()
    conn.close()
    return render_template('admin.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('dessert_name')
    price = request.form.get('dessert_price')
    ingredients = request.form.get ('dessert_ingredients')
    if name and price and ingredients:
        conn = get_db_connection()
        conn.execute('INSERT INTO desserts (name, price, ingredients) VALUES (?, ?, ?)', (name, price, ingredients))
        conn.commit()
        conn.close()
    return redirect('/admin') # 新增完回到後台，不是首頁！
@app.route('/delete', methods=['POST'])
def delete():
    # 這裡我們領取標籤叫 'target_id' 的包裹
    dessert_id = request.form.get('target_id')
    
    if dessert_id:
        conn = get_db_connection()
        # SQL 指令：刪除 id 等於我們拿到的那個標籤值
        conn.execute('DELETE FROM desserts WHERE id = ?', (dessert_id,))
        conn.commit()
        conn.close()
    
    # 動作完成後，同樣 redirect 回到辦公室 (/admin)
    return redirect('/admin')

@app.route('/dessert/<int:id>')
def dessert_detail(id):
    conn = get_db_connection()
    # 根據點擊的 ID，去資料庫只抓那一格甜點
    dessert = conn.execute('SELECT * FROM desserts WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('detail.html', dessert=dessert)

if __name__ == '__main__':
    app.run(debug=True)