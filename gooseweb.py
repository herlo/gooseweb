from __future__ import with_statement
#from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, \
     url_for, abort, render_template, flash

# configuration
#DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'


# create app instance
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('GOOSEWEB_SETTINGS', silent=True)


#def connect_db():
#    """Returns a new connection to the database."""
#    return sqlite3.connect(app.config['DATABASE'])


#def init_db():
#    """Creates the database tables."""
#    with closing(connect_db()) as db:
#        with app.open_resource('schema.sql') as f:
#            db.cursor().executescript(f.read())
#        db.commit()


#@app.before_request
#def before_request():
#    """Make sure we are connected to the database each request."""
#    g.db = connect_db()


#@app.teardown_request
#def teardown_request(exception):
#    """Closes the database again at the end of the request."""
#    if hasattr(g, 'db'):
#        g.db.close()


@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/community')
def community():
    return 'You clicked community...'

@app.route('/download')
def download():
    return 'You clicked download...'

@app.route('/help')
def help():
    return 'You clicked help...'

@app.route('/about')
def about():
    return 'You clicked about...'

# If we were not loaded as a module, start the app instance
if __name__ == '__main__':
    app.run()
