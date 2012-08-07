from __future__ import with_statement
#from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, \
     url_for, abort, render_template, flash

# configuration
DEBUG = True
SECRET_KEY = 'development key'


# create app instance
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('GOOSEWEB_SETTINGS', silent=True)


@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/help')
def help():
    return render_template('help.html')

#############################################################
# If we were not loaded as a module, start the app instance #
#############################################################
if __name__ == '__main__':
    app.run()
