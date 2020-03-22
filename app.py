from flask import Flask, render_template, request, jsonify
from flask_qrcode import QRcode
from tablib import Dataset
import tablib

app = Flask(__name__)
qrcode = QRcode(app)

# if __name__ == '__main__':
app.run()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route('/upload', methods=['POST'])
def upload_file():
    # I used form data type which means there is a
    # "Content-Type: application/x-www-form-urlencoded"
    # header in my request
    # raw_data = request.files['file'].read()  # In form data, I used "myfile" as key.
    # dataset = Dataset().load(raw_data)
    my_dataset = tablib.Dataset()
    my_dataset.xls = request.files['file'].read()
    return my_dataset.export('json')
