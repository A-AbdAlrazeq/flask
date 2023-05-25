from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    blackberry = request.form['blackberry']

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count = int(strawberry) + int(raspberry) + int(apple) + int(blackberry)
    date = datetime.now()
    print(f"Charging { first_name } { last_name } for { count } fruit") 

    return render_template("checkout.html",straw=strawberry,rasp=raspberry,apple=apple,black=blackberry,fname=first_name,lname=last_name,std_id=student_id,count_fruit=count,date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    