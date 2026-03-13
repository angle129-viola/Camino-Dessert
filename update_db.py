import sqlite3

conn = sqlite3.connect('camino.db')
# 指令：在 desserts 表格中，新增一個叫 ingredients 的文字欄位
try:
    conn.execute('ALTER TABLE desserts ADD COLUMN ingredients TEXT')
    print("成功加蓋新房間：ingredients 欄位已新增！")
except:
    print("欄位可能已經存在囉。")

# 順便幫妳現有的甜點補上成分，免得空空的
conn.execute("UPDATE desserts SET ingredients = '法國奶油、日本麵粉、香草籽' WHERE name = 'Canelé'")
conn.commit()
conn.close()