from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template("index.html", times=3, color="blue")


@app.route('/play/<x>')
def boxes(x):
    return render_template("index.html", times=int(x))


@app.route('/play/<x>/<color>')
def box_color(x, color):
    return render_template("index.html", times=int(x), color=color)


@app.route('/<any>')
def Sorry(any):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)
