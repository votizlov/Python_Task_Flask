from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

# if __name__ == '__main__':
app.run()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route("/converter", methods=["GET"])
def convert():
    curr = request.args.get("curr", "")  # 1 - usd, 2 - eur
    val = request.args.get("val", "")
    tables = pd.read_html('http://cbr.ru/key-indicators/')
    output = "Неизвестная валюта"
    if curr == "Евро":
        t = tables[0][2][2]
        output = float(t[:2]+'.'+t[2:])*float(val)
    elif curr == "Доллары":
        t = tables[0][1][1]
        output = float(t[:2]+'.'+t[2:])*float(val)
    print(curr)
    print(tables)
    return str(output)
