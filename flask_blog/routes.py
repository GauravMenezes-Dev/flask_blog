from flask import render_template, url_for, flash, redirect, request
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegForm, LoginForm
from flask_blog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful! Please check your credentials!','danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title="Account")
