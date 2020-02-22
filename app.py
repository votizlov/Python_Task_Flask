from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode

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

#deprecated
@app.route("/getimage")
def get_img():
    img = qrcode.make(request.form['text'])
    # img.save('\static\img.png')
    return "a.jpg"


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    img = qrcode(data, mode="raw")
    return qrcode(data)
