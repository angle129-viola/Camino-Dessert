from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 我們不再回傳一串文字，而是告訴 Flask 渲染 (render) 那個 HTML 檔案
    return render_template('index.html')

if __name__ == '__main__':
    # 開啟 debug 模式，方便我們之後邊改邊看
    app.run(debug=True)