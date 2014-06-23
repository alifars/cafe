__author__ = 'ali'
# -*- coding: utf-8 -*-

import nltk, nltk.corpus,codecs
import pyodbc
from nltk.corpus import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader

connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\fars.mdb")
c = connection.cursor()
corpus = LazyCorpusLoader('hamshahricorpus',XMLCorpusReader, r'(?!\.).*\.xml')

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


c.execute("select  wordtext,gloss,example,senseid from finaljoint")
file2=codecs.open('d:\\wsdtext.txt','r','utf-8')
outfile=codecs.open('d:\\wsd\\milk.txt','w','utf-8')

stopwords=[u'و',u'به',u'از',u'در',u'بر',u'را',u'با',u'که',u'های',u'می',u'یا',u'برای',
           u'است',u'تا',u'آن',u'دارد',u'شود',u'او',u'ها',u'هم',u'شده',u'کند',u'من',u'ای',u'هر',
           u'کنند',u'کند','دهند','اگر',u'آنها',u'دهند',u'اش',
           u'شد',
           u'اگر']
words=[]
count=0
for line in file2:
    line=line.strip()
    tokens=line.split()
    for token in tokens:
        words.append(token)
wordsense={}
#for word in  words:
#    print word


for item in c:
   for word in words:
      item[1]= correctPersianString(item[1])
      item[0]= correctPersianString(item[0])


      if word==item[0]:
         mixed=item[1]+' '+item[2]
         wordsense.setdefault(item[0], []).append((mixed,item[3]))

anothercount=0
total=0
nooverlap=0
num=0
commonwords={}
for file in corpus.fileids():
  
   #if num==1000: break
   for doc in  corpus.xml(file).getchildren():

          cat=doc.getchildren()[3].text#
          text=doc.getchildren()[5].text
          newtext=correctPersianString(text)
          allwords=newtext.split()
          sents=newtext.split('.')
          for word in words:
           # print word
            for sent in sents:
                 if word in sent.split():
                #  print sent
                  total+=1


                  overlap={}

                  bestsenses=[]
                  #wordindx=sents.index(sent)
                  context=sent.split()
#                  print ' '.join(context)

                  purecontextwords=set(context)-set(stopwords)

                  for i in range(len(wordsense[word])):
                          senseid=wordsense[word][i][1]
                          glosswords=wordsense[word][i][0].split()
                         # print senseid,' '.join(glosswords)
                          pureglosswords=set(glosswords)-set(stopwords)
                          common=set(pureglosswords)&set(purecontextwords)
                          if word in common:
                                 common.remove(word)
                          overlap[senseid]=len(common)
                          if common:
                           #commonwords[senseid]=list(common)
                           commonwords.setdefault(senseid, []).append(' '.join(common))
#                          if common:
#                                print ' '.join(common)

                  #print overlap
                  bestoverlap=max(overlap.values())
                  if bestoverlap>0:

                      for item  in overlap.keys():
                          if overlap[item]==bestoverlap:
                              bestsenses.append(item)
                  else:
                      nooverlap+=1
                  if len(bestsenses)==0:
                      pass


#                  else:
#                      if 3 in bestsenses:
#                          pass

                       #  print ' '.join(context),'\t',bestsenses
                        # num+=1

                  elif len(bestsenses)==1:
               #       print ' '.join(context),'\t',bestsenses

                        anothercount+=1
                        if bestsenses[0]==0 or bestsenses[0]==1 or bestsenses[0]==2:
                          print ' '.join(context)
                          outfile.write(' '.join(context))
                          print '\n'
                          num+=1
                   
                     # print len(bestsenses)

#for item in  commonwords:
#    print item, ' '.join(set(commonwords[item]))
print 'total samples of target word',total
print 'dont have overlap:',nooverlap
print 'have one sene:',anothercount
print 'sense#0 milk', num
file2.close()
connection.close()
outfile.close()