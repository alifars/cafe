# -*- coding: utf-8 -*-
import nltk, nltk.corpus,codecs
import pyodbc

def correctPersianString(source):
    if source is not None:
        source = source.strip()#.replace("\\b\\s{2,}\\b", " ")

        #replace shift x with persian ye
        source = source.replace(u'\u064a', u'\u06cc' )

        #replace arabic k with persian k
        source = source.replace(u'\u0643', u'\u06a9' )

        #replace h dar shift+n
        source = source.replace(u'\u0623', u'\u0627' )

        #persian z
        source = source.strip().replace(u'\u0632\\s', u'\u0632' )

        #persian d
        source = source.strip().replace(u'\u062F\\s',u'\u062F' )

        #persian r
        source = source.strip().replace(u'\u0631\\s',   u'\u0631' )

        #persian zhe
        source = source.strip().replace(u'\u0698\\s',   u'\u0698' )

        #persian vav
        source = source.strip().replace(u'\u0648\\s',u'\u0648' )

        #persian dal zal
        source = source.strip().replace(u'\u0630\\s', u'\u0630' )

        #persian alef bi kolah
        source = source.strip().replace(u'\u0627\\s',       u'\u0627' )

        #persian alef ba kolah
        source = source.strip().replace(u'\u0622\\s',   u'\u0622' )

        return source

connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\fars.mdb")
c = connection.cursor()
c.execute("select wordtext, gloss, synsets.senseID from words inner join synsets on  words.wordID=synsets.wordID where words.senseID=synsets.senseid")
file=codecs.open('e:\\test.txt','r','utf-8')
#tw=raw_input('enter a word')
#print type(tw)
#new=tw.encode('utf-8')
words=[]
#for line in file:
#    tokens=line.split()
#    for token in tokens:
#        words.append(token)

#for word in  words:
#    print word

dic={}
for item in c:
    #print len(item)
    print item[0], item[1], item[2]

#    if  item[0] not in dic.keys():
#           dic[item[0]]=item[1]
#
#for item in dic.keys():
#    print item,dic[item]
#    #if item[4]> 10: print item[3],item[1],item[2],item[3],item[4]#,item[5],item[6],item[7]#,item[8],item[10]
connection.close()