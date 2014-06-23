__author__ = 'ali'
# -*- coding: utf-8 -*-

import nltk, nltk.corpus,codecs
import pyodbc
from nltk.corpus import XMLCorpusReader
from nltk.corpus.util import LazyCorpusLoader
import wx

connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\fars.mdb")
c = connection.cursor()
stopwords=[u'و',u'به',u'از',u'در',u'بر',u'را',u'با',u'که',u'های',u'می',u'یا',u'برای',
           u'است',u'تا',u'آن',u'دارد',u'شود',u'او',u'ها',u'هم',u'شده',u'کند',u'من',u'ای',u'هر',
           u'کنند',u'کند','دهند','اگر',u'آنها',u'دهند',u'اش',
           u'شد',
           u'اگر']

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





class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,400))

        panel = wx.Panel(self, -1)

        button = wx.Button(panel, label="Close", pos=(0, 10))
        button2 = wx.Button(panel, label="show senses", pos=(0, 40))
        button3 = wx.Button(panel,label="search corpus", pos=(0, 70))

       # wx.StaticText(panel, -1, "This is an example of static text",(100, 10))
        self.text=wx.TextCtrl(panel, -1,pos=(175, 60),style=wx.TE_RIGHT)
        self.printarea=wx.TextCtrl(panel, -1,size=(500,150),pos=(0, 100),style=wx.TE_MULTILINE|wx.TE_RIGHT)
        self.word = self.text.GetValue()







        self.Bind(wx.EVT_BUTTON, self.OnClose, button)
        self.Bind(wx.EVT_BUTTON, self.ShowSenses, button2)
        self.Bind(wx.EVT_BUTTON, self.SearchCorpus, button3)
        self.Show(True)

    def OnClose(self, event):
              self.Destroy()
    def ShowSenses(self, event):
      wordsense={}
      c.execute("select  wordtext,gloss,senseid from final2")

      word = self.text.GetValue()
      self.printarea.Clear()
      for item in c:

         item[1]= correctPersianString(item[1])
         item[0]= correctPersianString(item[0])


         if word==item[0]:
            frame.printarea.write(str(item[2])+' ')
            frame.printarea.write(item[1]+'\n')
            wordsense.setdefault(item[0], []).append((item[1],item[2]))
      return wordsense
           # print item[1]#,item[2]
    def SearchCorpus(self, event):
        count=0

        userword=self.text.GetValue()
        wordsenses=self.ShowSenses(self)
        corpus = LazyCorpusLoader('hamshahricorpus',XMLCorpusReader, r'(?!\.).*\.xml')
        for file in corpus.fileids():

       #if num==1000: break
          for doc in  corpus.xml(file).getchildren():

              cat=doc.getchildren()[3].text#
              text=doc.getchildren()[5].text
              newtext=correctPersianString(text)
              allwords=newtext.split()
             # sents=newtext.split('.'
              if userword in allwords:
                  overlap={}
                  bestsenses=[]
                  wordindx=allwords.index(userword)
                  context=allwords[wordindx-8:wordindx+8]
                  purecontextwords=set(context)-set(stopwords)
                  for i in range(len(wordsenses[userword])):
                        senseid=wordsenses[userword][i][1]
                        glosswords=wordsenses[userword][i][0].split()
                        pureglosswords=set(glosswords)-set(stopwords)
                        common=set(pureglosswords)&set(purecontextwords)
                        if userword in common:
                                 common.remove(userword)
                        overlap[senseid]=len(common)
                        
                  bestoverlap=max(overlap.values())
                  if bestoverlap>0:

                      for item  in overlap.keys():
                          if overlap[item]==bestoverlap:
                              bestsenses.append(item)
                  if len(bestsenses)==1:



                      # if 0 in bestsenses:

                           print ' '.join(context),'\t',bestsenses
                           frame.printarea.Clear()
                           frame.printarea.write(' '.join(context)+'\t'+str(bestsenses))

#        file.close()

class xmlcorpus():
   pass



app = wx.App(False)
frame = MyFrame(None,u'برچسب زن معنایی')











app.MainLoop()

connection.close()
