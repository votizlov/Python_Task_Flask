from flask import Flask, render_template, request, send_file
import qrcode
from pathlib import Path

app = Flask(__name__)

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


@app.route('/', methods=['GET'])
def generate_qr():
    img = qrcode.make(request.form['text'])
   # path = Path('C:\Users\User\PycharmProjects\Python_Task_Flask\img')
    img.save('\img','png')
    return img
