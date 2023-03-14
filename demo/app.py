from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index() :
    return render_template("index.html")

@app.route('/about')
def about() :
    return render_template("about.html")

@app.route('/admin')
def admin() :
    return render_template("admin.html")

@app.route('/user/<name>/<yob>')
def profile(name, yob) :
    age = 2023 - int(yob) 
    return ("<h1>Hello {} </h1>".format(name) + 
            "<h1>Now You're {} years old</h1>".format(age))

if __name__ == '__main__':
    app.run(debug = True)