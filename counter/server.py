from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def count():
    session['count'] += 1
    return render_template("index.html")

@app.route('/formsubmission', methods=['post'])
def submit():
    print('post route')
    return redirect('/')

@app.route('/delete')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)