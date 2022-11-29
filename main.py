from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4e71e0249507fa6c34ba823f96986b09'  # Setting up a secret key to protect agaisnt modifying cookies and cross site requests 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    job = db.relationship('Job', backref='recruiter', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return f"Job details:('{self.job_title}', '{self.company}', '{self.location}', '{self.date_posted}')"

posts = [
    {
        'job_title': 'Data Scientist intern',
        'company': 'Microsoft',
        'Description': 'zero years of experince, knowledge in Python, Java',
        'date_posted': '2 November 2022',
         'location': 'Atlanta'
    },

    {
        'job_title': 'Software Engineer Intern ',
        'company': 'Microsoft',
        'Description': 'zero years of experince, knowledge in Python, Java',
        'date_posted': '19 November 2022',
        'location': 'NewYork'
    },


]
# Home function 
@app.route("/")
# @app.route("/home")
def home():
    return  render_template("home.html", posts=posts)


# About function 
@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@job.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. Please check your username and password', 'danger')
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)