__author__ = 'David'
import mysql.connector
try:
   cnx = mysql.connector.connect(user='root',database='americanPy')
except:
    print("Connectie maken is niet gelukt")
