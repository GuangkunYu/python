from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/test2')
def test():
    return render_template("index2.html")


@app.route('/test3')
def test3():
    return render_template("index3.html")


@app.route('/test4')
def test4():
    return render_template("index4.html")


@app.route('/test5')
def test5():
    return render_template("index5.html")


@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == "GET":
        name = request.args.get("username")
        title = request.args.get("title")
        print(name, title)
        data = {
            "name": name,
            "title": title
        }
        return jsonify(data)

    if request.method == 'POST':
        name = request.form["username"]
        age = request.form["age"]
        print(name, age)
        data = {
            "name": name,
            "age": age
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
