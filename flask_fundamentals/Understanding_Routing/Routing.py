from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def hello():
    return 'Dojo!'


@app.route('/say/<name>')
def say(name):
    return "Hi " + name.capitalize()+"!"


@app.route('/repeat/<times>/<name>')
def repeat(name, times):
    return render_template("index.html", phrase=name, num_times=int(times))


@app.route('/<any>')
def Sorry(any):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)
