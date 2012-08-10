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
POSTSLIMIT = 5 #number of blog posts to display on newsfeed sidebar
WORDLIMIT = 150 #number of words to limit to restrict blog post snippets


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
    
    # limit number of posts shown by POSTSLIMIT
    # unless actual number of posts are less than that
    plimit = POSTSLIMIT
    if len(feed.entries) < POSTSLIMIT:
        plimit = len(feed.entries)

    # format each post for placement on the home page
    for p in range(0,plimit):
        postsfile.write('<p><div class="post_info">')
        postsfile.write('<table width="100%"><tr><td>')
        postsfile.write(unicode(feed.entries[p].author).encode('utf8'))
        postsfile.write('</td><td align="right">')
        postsfile.write(feed.entries[p].updated.split('T')[0])
        postsfile.write('</td></tr></table></div>')
        postsfile.write('<h3><a href="')
        postsfile.write(feed.entries[0].link)
        postsfile.write('">')
        postsfile.write(unicode(feed.entries[p].title).encode('utf8'))
        postsfile.write('</a></h3>')
        """postwords = unicode.split(entry.content[0].value)
        wlimit = WORDLIMIT
        if len(postwords) < 150:
            wlimit = len(postwords)
        for x in range (0,limit):
            postsfile.write(unicode(postwords[x]).encode('utf8'))
            postsfile.write(' ')"""


        # ian bicking is awesome
        # http://stackoverflow.com/questions/2649751/python-remove-everything-between-div-class-comment-any-div
        from lxml import html

        content = unicode(feed.entries[p].content[0].value).encode('utf8')

        doc = html.fromstring(content)
        for el in doc.cssselect('img'):
            el.drop_tree()
        for el in doc.cssselect('div'):
            el.drop_tree()
        entries = html.tostring(doc)


        postsfile.write(entries[:200])
        postsfile.write('... <span class="full_link"><a href="')
        postsfile.write(feed.entries[0].link)
        postsfile.write('">(Full Article)</a></span></p>')

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
