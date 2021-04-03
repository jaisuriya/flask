
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/client", methods=['GET','POST'])
def client():
    return render_template("client.html")

@app.route("/login", methods=['GET','POST'])
def Login():
    return render_template("login.html")
if __name__ == '__main__':
    app.run(debug=True)
