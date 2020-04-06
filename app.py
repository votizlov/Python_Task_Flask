from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
import pandas as pd

app = Flask(__name__)
qrcode = QRcode(app)

# if __name__ == '__main__':
app.run()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    data = request.args.get("data", "")
    tables = pd.read_html('http://cbr.ru/key-indicators/')
    print(tables)
    return str(tables)

@app.route("/converter", methods=["GET"])
def get_qrcode():
    data = request.args.get("data", "")#1 - usd, 2 - eur
    tables = pd.read_html('http://cbr.ru/key-indicators/')
    print()
    #print(tables)
    return data
