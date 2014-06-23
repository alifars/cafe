__author__ = 'ali'

# -*- coding: utf-8 -*-
import nltk, nltk.corpus,codecs
import pyodbc

#from nltk.book import *
from nltk.corpus import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import TaggedCorpusReader

#connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\farsnettest.mdb")
#cursor = connection.cursor()
#
#cursor.execute("select * from synsets")
##for item in cursor:
#    print item





corp= LazyCorpusLoader('wn3', XMLCorpusReader, r'(?!\.).*\.xml')
#print len(corp.xml())

for item in corp.xml():
    

    print item.getchildren()
    synsetID=item.getchildren()[0].text
    #pos=item.getchildren()[1].text
    pos=item.getchildren()[2].text
    example=item.getchildren()[4].text
    gloss=item.getchildren()[5].text
    i=item.getchildren()[7].text




