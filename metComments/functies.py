import mysql.connector
import datetime
import xmltodict
import codecs
import requests
'''Connectie maken met MYSQL'''
connectie_met_mysql = mysql.connector.connect(host='localhost', password='', user='root', database='americanPy') #connect leggen met mysql
cursor = connectie_met_mysql.cursor(buffered=True) #mysql commands kunnen uitvoeren

'''Kijken of inlog klopt'''
inlog_query = ("SELECT * FROM aanbieders")
cursor.execute(inlog_query) # haal aanbieders op
username_wachtwoord = {}

for row in cursor:
    username_wachtwoord[row[4]] = row[5]
'''We printen hier nog username en wachtwoord zodat we kunnen laten zien in screencast wat overeenkomt'''
print(username_wachtwoord)

''' Vraag api op en schrijf in XML'''
def vraag_api_en_schrijf_xml():
    datum = datetime.date.today().strftime("%d-%m-%Y") # datum in format dd-mm-yyyy
    request = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=qx4ugph3my32lh95qf4wixt7zxo9qee5&dag=' + datum + '&sorteer=0') # api request met actuele datum
    bestand = codecs.open('api.xml', 'w', 'utf-8') # fouten voorkomen met schrijven
    bestand.write(str(request.text))
    bestand.close()
vraag_api_en_schrijf_xml()
'''Xml omzetten naar dict'''
def xml_naar_dictionary():
    bestand = open('api.xml', 'r') # open net geschreven xml bestand
    string = bestand.read()
    return xmltodict.parse(string) # return dictionary van de string van het bestand

film_dictionary = xml_naar_dictionary()
'''Api gegevens uit de dict doorgeven aan de MYSQL database'''
def voer_api_gevens_in_mysql():
    for i in range(0,6): # 7 films dus 0-6
        titel_van_api = film_dictionary['filmsoptv']['film'][i]['titel']
        cover_van_api = film_dictionary['filmsoptv']['film'][i]['cover']
        synopsis_van_api = film_dictionary['filmsoptv']['film'][i]['synopsis']
        genres_van_api = film_dictionary['filmsoptv']['film'][i]['genre']
        duur_van_api = film_dictionary['filmsoptv']['film'][i]['duur']
        if duur_van_api is None: # controleren dat er een duurtijd beschikbaar is
            duur_van_api = "Geen tijd beschikbaar"
        link_van_api = film_dictionary['filmsoptv']['film'][i]['ft_link']
        zender_van_api = film_dictionary['filmsoptv']['film'][i]['zender']
        rating_van_api = film_dictionary['filmsoptv']['film'][i]['imdb_rating']
        starttijd_van_api = film_dictionary['filmsoptv']['film'][i]['starttijd']
        film_toevoegen_query = ("INSERT INTO films (titel, cover, synopsis, genres, filmduur, link, zender, rating, starttijd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(film_toevoegen_query, (titel_van_api, cover_van_api, synopsis_van_api, genres_van_api, duur_van_api, link_van_api, zender_van_api, rating_van_api, starttijd_van_api))
        connectie_met_mysql.commit()


voer_api_gevens_in_mysql()
