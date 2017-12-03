from flask import Flask, render_template
from firebase import firebase
# connect to appp

firebase = firebase.FirebaseApplication(''0)

app = Flask(__name__)


@app.route('/')
def hello_world():
    alexis = 'cherry'
    return render_template('index.html', alexis=alexis)

@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/login2')
def login1():

    return render_template('market.html')

@app.route('/register')
def signup():

    return render_template('register.html')

@app.route('/<string:uid>')
def auth(uid):

    return render_template('market.html', uid=uid)

if __name__ == '__main__':
    app.run()

