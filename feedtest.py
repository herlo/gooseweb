#!/usr/bin/env python

# feedparser test
import feedparser

d = feedparser.parse('http://planet.gooseproject.org/atom.xml')
f = open('tempfeed.html', 'w')
for entry in d.entries:
    f.write(entry.author)
    f.write('<h3>')
    print entry.title
    t = entry.title
    t.encode('ascii','replace')
    f.write(t)
    f.write('</h3>')
    f.write(entry.updated)  #or update-parsed
    f.write(entry.content[0].value)
    f.write(entry.link)

f.close()
