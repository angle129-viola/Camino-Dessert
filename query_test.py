import sqlite3

conn = sqlite3.connect('camino.db')
cursor = conn.cursor()

# 1. 叫服務生去撈所有資料
cursor.execute("SELECT * FROM desserts")
rows = cursor.fetchall() # 把菜全部端出來 (存進 rows 這個清單)

print("--- 🧁 Camino Dessert 現有菜單 ---")
for row in rows:
    # 這裡就是 List 的 index 應用：0是ID, 1是名字, 2是價格
    print(f"編號: {row[0]} | 品名: {row[1]} | 價格: {row[2]} 元")

conn.close()