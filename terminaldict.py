#!/usr/bin/env python

from urllib import urlopen
from bs4 import BeautifulSoup as bs

def look_up(word):
    url = 'http://dict.youdao.com/search?q='
    text = urlopen(url + word).read()
    soup = bs(text)
    ph = soup.find('div', {'class': 'baav'}).get_text()
    mean = soup.find('div', {'class': 'trans-container'}).find('ul').get_text()
    print ph, mean

def run(prompt='> ', opt=True):
    print 'Press Ctrl + C/D to quit.\n'
    word_list = []

    try:
        while True:
            w = raw_input(prompt)
            word_list.append(w)
            val = look_up(w)
            if val is not None: print val
    except (KeyboardInterrupt, EOFError, AttributeError):
        if opt == True:
            print 'History:'
            for i in word_list:
                print i

if __name__ == '__main__':
    run()
