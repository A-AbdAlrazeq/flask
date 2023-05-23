from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    print(request.form)
    name = request.form['name']
    city = request.form['city']
    Language = request.form['Language']
    Gender = request.form['gender']
    Checkbox = request.form['Check']
    Comment = request.form['comment']
    if request.form.get("Check") == "":
        request.form['Check'] = ""
    return render_template("show.html",
                           name_on_template=name,
                           city_on_template=city,
                           Language_on_template=Language,
                           gender_on_template=Gender,
                           Checkbox_on_template=Checkbox,
                           Comment_on_template=Comment,
                           )


if __name__ == "__main__":
    app.run(debug=True)
