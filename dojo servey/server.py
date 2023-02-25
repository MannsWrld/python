from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/formsubmission', methods=['post'])
def submit():
    print('post route')
    print(request.form)
    session['fn'] = request.form['first_name']
    session['ln'] = request.form['Last_name']
    session['site'] = request.form['Location']
    session['#'] = request.form['code']
    session['text'] = request.form['comment']
    return redirect('/dojo')

@app.route('/dojo')
def dojo():
    return render_template("survey.html")

@app.route('/clear')
def reset():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)