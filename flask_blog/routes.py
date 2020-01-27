from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.forms import RegForm, LoginForm
from flask_blog.models import User, Post

posts = [
    {
        'author': "Gaurav Menezes",
        'title': "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "November 11, 1994"
    },
    {
        'author': "Shashwat Gupta",
        'title': "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "November 02, 1998"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Login unsuccessful! Please check your credentials!','danger')
    return render_template('login.html', title="Login", form=form)
