from flask import Flask, request, redirect, url_for, make_response, json, jsonify, session

app = Flask(__name__)
app.secret_key = 'secret string'


@app.route('/hello', methods=['GET', 'POST'])
def index():
    response = ''
    name = request.args.get("name", 'Flask')
    if name is None:
        name = request.cookies.get("name")
        response = f'<h1>hello {name}!</h1>'
    # name = request.args["name"]
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


@app.route('/goback/<int:year>')
def go_back(year):
    return f'welcome to {2018 - year}'


@app.route('/colors/<any(blue, green, red):color>')
def three_color(color):
    return f'<p>love is patient and kind. love is not jealous or boastful or proud or rude.</p>'


# @app.before_request
def do_something():
    return '请求前执行'


# @app.route('/hello/')
# def hello():
#     return redirect('http://www.example.com')


@app.route('/hi')
def hi():
    return redirect(url_for('hello'))


@app.route('/foo')
def foo():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get("name")
    data = {
        'name': name,
        'gender': 'male'
    }
    # response = make_response(json.dumps(data))
    # response.mimetype = 'application/json'
    return jsonify(data)


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))