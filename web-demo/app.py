from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    data = {"name": "Johny", "age": 35, "salary": 28000}
    return render_template("index.html", myData=data)


@app.route('/about')
def about():
    lists = ["list1", "list2", "list3"]
    return render_template("about.html", myList=lists)


@app.route('/contactus')
def contactUs():
    return render_template("contactus.html")


@app.route('/submitForm')
def sendSubmitForm():
    fname = request.args.get('fname')
    desc = request.args.get('description')
    return render_template("submitformdone.html", data={"name": fname, "description": desc})


@app.route('/admin')
def admin():
    name = "Anonymous"
    age = 25
    return render_template("admin.html", myName=name, myAge=age)


@app.route('/user/<name>/<yob>')
def profile(name, yob):
    age = 2023 - int(yob)
    return ("<h1>Hello {} </h1>".format(name) +
            "<h1>Now You're {} years old</h1>".format(age))


if __name__ == '__main__':
    app.run(debug=True)
