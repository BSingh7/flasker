from flask import Flask, render_template
from flask.helpers import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Create a Flask Instance
app=Flask(__name__)
app.config['SECRET_KEY']="Royalarsenal121-"
#Create a route decorate (URL)

class NamerForm(FlaskForm):
    name=StringField("Whats's Your Name?",validators=[DataRequired()])
    submit=SubmitField("Submit")

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

@app.route('/name', methods=['GET','POST'])
def name():
    name=None
    form=NamerForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("Form Submitted Successfully")


    return render_template("name.html",
    name=name,
    form=form)