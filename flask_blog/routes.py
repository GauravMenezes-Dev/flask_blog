from flask import render_template, url_for, flash, redirect
from flask_blog import app, db, bcrypt
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
        
        #hashing a password
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #user creation
        user= User(username=form.username.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        #success message
        flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))

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
