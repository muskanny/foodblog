from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from Sentiment_Analysis import sentiment_analyser

from forms import RegistrationForm, LoginForm

app= Flask(__name__) #instance of the flask class

app.config['SECRET_KEY']='0afad545231860ddc7747e78cd8ad6a3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

posts=[{'name':'muskan singh', 'title':'blog post 1','content':'first post content','date_posted':'April 20,2018'},
{'name':'srishti chugh', 'title':'blog post 2','content':'second post content','date_posted':'April 22,2018'},
{'name':'shreeya aggarwal', 'title':'blog post 3','content':'third post content','date_posted':'April 23,2018'},
{'name':'nishtha gupta', 'title':'blog post 4','content':'fourth post content','date_posted':'April 21,2018'},
{'name':'shruti tripathi', 'title':'blog post 5','content':'fifth post content','date_posted':'April 20,2018'}]

# @app.route("/home", methods = ['GET', 'POST'])
@app.route("/", methods = ['GET', 'POST'])
def home():
	if (request.method == 'POST') :
		print("hey")
		link = request.form.get('link')
		sentiment_analyser(link)

	#posts=[{'name':'muskan singh', 'title':'blog post 1','content':'first post content','date_posted':'April 20,2018'},
	#{'name':'srishti chugh', 'title':'blog post 2','content':'second post content','date_posted':'April 22,2018'},
	#{'name':'shreeya aggarwal', 'title':'blog post 3','content':'third post content','date_posted':'April 23,2018'},
	#{'name':'nishtha gupta', 'title':'blog post 4','content':'fourth post content','date_posted':'April 21,2018'},
	#{'name':'shruti tripathi', 'title':'blog post 5','content':'fifth post content','date_posted':'April 20,2018'}]

	else :
		print("hello")
		return render_template('index.html', posts=posts)
	'''<!doctype html>
	<html>
	'''
#def hello():
#	return "<h1>home page</h1>"

@app.route("/about")

def about():
	return render_template('about.html', title='about page')

@app.route("/register", methods=['GET','POST'])

def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))

	return render_template('register.html',title='Register', form=form)

@app.route("/login", methods=['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)





if __name__=="__main__":
	app.run(debug=True)