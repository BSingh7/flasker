from flask import Flask, render_template

#Create a Flask Instance
app=Flask(__name__)

#Create a route decorate (URL)
@app.route('/')

#def index():
    #return "<h1>Hello World!</h1>"

def index():
    return render_template("index.html")

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)

# Filter can be put by using | and the filter (can be seen in user.html)
# Create Custom URL

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
