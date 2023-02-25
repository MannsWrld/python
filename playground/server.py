from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play1():
    return "Welcome"
    
@app.route('/play/3')
def play2():
    return render_template("index.html",num=3,color="purple")

@app.route('/play/7')
def play3():
    return render_template("index.html",num=7,color="blue") 

@app.route('/play/5')
def play4():
    return render_template("index.html",num=5,color="red")

# html file is not understanding jinja2
    
if __name__=="__main__":
    app.run(debug=True)


