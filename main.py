from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4e71e0249507fa6c34ba823f96986b09'  # Setting up a secret key to protect agaisnt modifying cookies and cross site requests 

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)