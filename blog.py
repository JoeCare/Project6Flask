from flask import (
    Flask, 
    render_template,
    url_for
    )
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'sajdklSD!KHasK#;dj8K273J4Grfdaaq3'


posts = [
    {
        'author': 'Joseph Careless',
        'title': 'Post #1',
        'content': 'First post content',
        'date_posted': 'March 21, 2017',
        },
    {
        'author': 'Joey Carelessness',
        'title': 'Post #2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2017',
        },
    {
        'author': 'Josephine Carey',
        'title': 'Post #3',
        'content': 'Third post content',
        'date_posted': 'May 11, 2017',
        },
    ]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html',title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)

