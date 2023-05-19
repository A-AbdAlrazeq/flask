from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", row=8, col=8, color1="red", color2="black")


@app.route('/<x>')
def set_row(x):
    return render_template("index.html", row=int(x), col=8, color1="red", color2="black")


@app.route('/<x>/<y>')
def set_row_col(x, y):
    return render_template("index.html", row=int(x), col=int(y), color1="red", color2="black")


@app.route('/<x>/<y>/<color1>/<color2>')
def set_all(x, y, color1, color2):
    return render_template("index.html", row=int(x), col=int(y), color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
