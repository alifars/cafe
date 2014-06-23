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





corp= LazyCorpusLoader('farsnet\synset', XMLCorpusReader, r'(?!\.).*\.xml')
#print len(corp.xml())
mapExistsCont=0
itemnum=0
for item in corp.xml():
    itemnum+=1
    

   # print item.getchildren()
    synsetID=item.getchildren()[0].text
    #pos=item.getchildren()[1].text
    pos=item.getchildren()[2].text
    example=item.getchildren()[4].text
    gloss=item.getchildren()[5].text
    i=item.getchildren()[7].text
    wordnetID = item.getchildren()[-2]
    if len(wordnetID.getchildren())!=0:

        mapExistsCont+=1
        print wordnetID.getchildren()[0].text

print itemnum,mapExistsCont
#    if gloss and example:
#      mix=gloss+" "+example
#    offset=item.getchildren()[9]#.text
#    if len(offset.getchildren())==2:
#         wnid=offset.getchildren()[0].text
#    print synsetID, wnid,gloss
#   # print  item.getchildren()[10].getchildren()
#    for i in range(len(item.getchildren()[10].getchildren())):
#           wordid=item.getchildren()[10].getchildren()[i].getchildren()[0].text
#           senseid=item.getchildren()[10].getchildren()[i].getchildren()[1].text
#           print wordid,senseid

      #     cursor.execute('insert into synsets(synsetID,wordnetID,pos, gloss,example,wordid,senseid) values (?,?,?,?,?,?,?)',(synsetID,wnid,pos,gloss,example,wordid,senseid))
          # print wnid
           


  # print"llllllllllllllllllllllllllllll"
#    sense=item.getchildren()[10]
#    for i in range(len(sense.getchildren())):
#         wordID=sense.getchildren()[i].getchildren()[0].text
#         senseID=sense.getchildren()[i].getchildren()[1].text
#         #print mix, wordID, senseID
#         cursor.execute('insert into synsets(synsetid,pos, gloss, example ,wordid,senseid) values (?,?,?,?,?,?)',(synsetID,pos, gloss,mix,wordID,senseID))

### Save (commit) the changes
#connection.commit()
#cursor.close()

  