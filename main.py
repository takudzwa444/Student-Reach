from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)