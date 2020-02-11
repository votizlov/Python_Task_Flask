from flask import Flask, render_template, request

app = Flask(__name__)



#if __name__ == '__main__':
app.run()

@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text
