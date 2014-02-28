#!/usr/bin/env python

from urllib import urlopen
from bs4 import BeautifulSoup as bs

def look_up(word):
    url = 'http://www.merriam-webster.com/dictionary/'
    text = urlopen(url+word).read()
    soup = bs(text)
    return soup.p.get_text()

def run(prompt='> '):
    print 'Press Ctrl + C to quit\n'
    while True:
        val = look_up(raw_input(prompt))
        if val is not None: print val

if __name__ == '__main__':
    run()