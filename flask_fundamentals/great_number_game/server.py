from flask import Flask, render_template, session,request, redirect
import random


app = Flask (__name__)
app.secret_key = 'secret2023'

@app.route('/')
def index():
    number = random.randint(1, 100)
    if 'number' not in session:
        session['number'] = number
    print (session['number'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    num=request.form['guess']
    if num =="":
         session['guess']=0
    else:
         session['guess'] = int(num)

    if 'attempts' not in session:
        session['attempts'] = 0
    session['attempts'] = int(session['attempts']) + 1
    print(session['attempts'])
    return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')

if __name__ == ('__main__'):
    app.run(debug=True)