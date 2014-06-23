__author__ = 'ali'
# -*- coding: utf-8 -*-
import nltk, nltk.corpus,codecs
import pyodbc
from nltk.corpus import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader

connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\farsnettest.mdb")
c = connection.cursor()
corpus = LazyCorpusLoader('farsnet\\relations',XMLCorpusReader, r'(?!\.).*\.xml')

for doc in  corpus.xml():


          word1=doc.getchildren()[0].text#
          word2=doc.getchildren()[1].text
          relation=doc.getchildren()[2].text
          print word1,word2,relation
#          sense2=doc.getchildren()[3].text
#          relation=doc.getchildren()[4].text

         # print word1,sense1, word2,sense2,relation
          c.execute('insert into synrelations(synsetID1,synsetID2,relation) values (?,?,?)',(word1,word2,relation))


connection.commit()
c.close()

