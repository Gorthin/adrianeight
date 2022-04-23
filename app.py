from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/about_me')
def about_me():
    return render_template("about_me.html")


if __name__=="__main__":
    app.run()
