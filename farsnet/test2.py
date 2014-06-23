import pyodbc



connection = pyodbc.connect("Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\farsnettest.mdb")
cursor = connection.cursor()

cursor.execute("select pos,wordtext from words")
for i in cursor:
    print i

  