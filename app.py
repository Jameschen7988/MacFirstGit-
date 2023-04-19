from flask import Flask #載入flask
from flask import request #載入Request 物件
import json #載入json模組
from flask import render_template #載入render_template 函式

#建立 application 物件 可以設定靜態檔案的路徑，除了name 這個參數，我們還可以加入更多參數
app = Flask(
    __name__,
    static_folder='public',  #靜態檔案的資料夾名稱
    static_url_path='/', #靜態檔案對應的網址路徑
    ) 

#所有在public 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

#使用GET方法，建立路徑/對應的處理函式 
@app.route('/')    
def index():
    return render_template('index.html')

#建立路徑/page對應的處理函式
@app.route('/page')
def page():
    return render_template('page.html')

#建立路徑/show對應的處理函式
@app.route('/show')
def show():
    name = request.args.get('name','')
    return '歡迎光臨' + name

#使用POST，建立路徑/calculate對應的處理函式
@app.route('/calculate', methods=['POST'])
def calculate():
    # 接收GET方法的Query String
    # maxNumber = request.args.get('max','')
    # 接受POST方法的Query String
    maxNumber = request.form['max']
    maxNumber = int(maxNumber)
    # 1 + 2 + 3 + ...... + maxNumber 
    result = 0 
    for n in range (1, maxNumber+1):
        result+=n
    return render_template('result.html', data = result)


#啟動網頁伺服器 可透過 port 參數指定埠號
app.run(port=3000)