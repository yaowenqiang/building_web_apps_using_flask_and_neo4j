from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hello World"
    # data = [1,2,3]
    data = [{'x':1}, {'x':2}, {'x':5}]
    # return render_template('index.html', message="Hello World message")
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return "about"

@app.route('/err')
def err():
    return x