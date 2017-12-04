from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    alexis = 'cherry'
    return render_template('index.html', alexis=alexis)

@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/test')
def login1():

    return render_template('market.html')

@app.route('/auth/', defaults = {'authtype' :'register'})
@app.route('/auth/<string:authtype>')
def signup(authtype):


    return render_template('register.html', authtype=authtype)

@app.route('/<string:uid>')
def auth(uid):

    return render_template('market.html', uid=uid)

if __name__ == '__main__':
    app.run()

