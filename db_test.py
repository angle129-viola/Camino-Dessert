import sqlite3

# 1. 建立連結 (像開門進入 camino.db 這個檔案)
conn = sqlite3.connect('camino.db')
cursor = conn.cursor() # 請服務生準備

# 2. 建立資料表 (SQL 指令：如果沒有這張表就建一個，包含 ID、品名、價格)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS desserts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER
    )
''')

# 3. 插入資料 (SQL 指令：把可麗露跟巴斯克塞進去)
cursor.execute("INSERT INTO desserts (name, price) VALUES ('Canelé', 85)")
cursor.execute("INSERT INTO desserts (name, price) VALUES ('Basque Cheesecake', 120)")

# 4. 存檔並關閉 (這步最重要，沒 commit 資料就不會寫入)
conn.commit()
conn.close()

print("✅ 資料庫 camino.db 已建立，且資料已存入！")