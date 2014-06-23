__author__ = 'ali'
__author__ = 'ali'

# -*- coding: utf-8 -*-
import nltk, nltk.corpus,codecs
import pyodbc
#from nltk.book import *
from nltk.corpus import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import TaggedCorpusReader

connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\myfarsnet.mdb")
cursor = connection.cursor()

#cursor.execute("select * from words")





corp= LazyCorpusLoader('farsnet\words', XMLCorpusReader, r'(?!\.).*\.xml')
#print len(corp.xml())

for item in corp.xml():

    wordID=item.getchildren()[0].text
    pos=item.getchildren()[1].text
    wordtext=item.getchildren()[2].text
    ava=item.getchildren()[3].text
    senses=item.getchildren()[5].getchildren()
    #wordID=wordID.encode('utf-8')
    print wordID,pos, wordtext,ava
    for item in senses:
        senseID=item.getchildren()[0].text

       # print  wordtext, senseID

      #  cursor.execute('insert into words(wordID,pos, wordtext,phonetics, senseID) values (?,?,?,?,?)',(wordID,pos,wordtext,ava,senseID))


connection.commit()
cursor.close()

  
  