from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
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
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    img = qrcode(data, mode="raw")
    driver = webdriver.Opera
    driver.get("http://www.cbr.ru")
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')
    return qrcode(data)
