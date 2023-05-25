from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['POST',"GET"])
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']
    session ['city'] = request.form['city']
    session ['Language'] = request.form['Language']
    session ['Gender'] = request.form['gender']
    session ['Comment'] = request.form['comment']
    if 'Check'not in request.form :
       session ['Checkbox'] ="not checked" 
    else:
       session ['Checkbox'] = request.form['Check']

    return redirect("/show")

@app.route('/show', methods=['POST',"GET"])
def show_results():
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)
