#!/usr/bin/env python

#----------------------------------------------------------------
# Import external libraries
#----------------------------------------------------------------
from __future__ import with_statement
#from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, \
     url_for, abort, render_template, flash
import feedparser
import os


#----------------------------------------------------------------
# Configuration variables
#----------------------------------------------------------------
DEBUG = True
SECRET_KEY = 'development key'
POSTSFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/postsfile.html')


#----------------------------------------------------------------
# Create our app instance
#----------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('GOOSEWEB_SETTINGS', silent=True)


#----------------------------------------------------------------
# Define flask routes
#----------------------------------------------------------------
@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():

    # grab the feed from planet gooseproject
    feed = feedparser.parse('http://planet.gooseproject.org/atom.xml')
    # open temp postsfile for writing
    postsfile = open(POSTSFILE, 'w')
    
    # format each post for placement on the home page
    for entry in feed.entries:
        postsfile.write('<span class="post_author">')
        postsfile.write(unicode(entry.author).encode('utf8'))
        postsfile.write('</span>')
        postsfile.write('<h3>')
        postsfile.write(unicode(entry.title).encode('utf8'))
        postsfile.write('</h3>')
        postsfile.write(entry.updated)  #or update-parsed
        postsfile.write(unicode(entry.content[0].value).encode('utf8'))
        postsfile.write(entry.link)

    postsfile.close()

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


#----------------------------------------------------------------
# If we were not loaded as a module, start the app instance
#----------------------------------------------------------------
if __name__ == '__main__':
    app.run()
