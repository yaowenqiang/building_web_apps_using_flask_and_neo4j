from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello World"
    # data = [1,2,3]
    data = [{'x':1}, {'x':2}, {'x':5}]
    # return render_template('index.html', message="Hello World message")
    message = 'this is a get request'
    if request.method == 'POST':
        message = 'this is a post request'
    return render_template('index.html', data=data, message=message)

@app.route('/about/<something>')
def about(something):
    return f'This page is about {something}'

@app.route('/err')
def err():
    return x