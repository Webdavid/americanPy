__author__ = 'David'
import datetime
import xmltodict
import codecs
import mysql.connector
import requests
def request_api_and_write():
    datum = datetime.date.today();datum = datum.strftime("%d-%m-%Y")
    request = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=qx4ugph3my32lh95qf4wixt7zxo9qee5&dag='+  datum + '&sorteer=0')
    bestand = codecs.open('api.xml', 'w', 'utf-8')
    bestand.write(str(request.text))
    bestand.close()
def xml_to_dictionary():
    bestand = open('api.xml', 'r')
    string = bestand.read()
    return xmltodict.parse(string)

connectie = mysql.connector.connect(host='localhost',password='',user='root',database='americanPy')
cursor = connectie.cursor()
request_api_and_write()
film_dictionary = xml_to_dictionary()
for i in range(0,6):
    titel_api = film_dictionary['filmsoptv']['film'][i]['titel']
    synopsis_api = film_dictionary['filmsoptv']['film'][i]['synopsis']
    cover_api = film_dictionary['filmsoptv']['film'][i]['cover']
    genres_api = film_dictionary['filmsoptv']['film'][i]['genre']
    filmduur_api = film_dictionary['filmsoptv']['film'][i]['duur']
    if filmduur_api is None:
        filmduur_api = "Geen tijd beschikbaar"
    print(filmduur_api)
    link_api = film_dictionary['filmsoptv']['film'][i]['ft_link']
    zender_api = film_dictionary['filmsoptv']['film'][i]['zender']
    rating_api = film_dictionary['filmsoptv']['film'][i]['imdb_rating']
    starttijd_api = film_dictionary['filmsoptv']['film'][i]['starttijd'
    film_toevoegen = ("INSERT INTO films (titel, cover, synopsis, genres, filmduur, link, zender, rating, starttijd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(film_toevoegen, (titel_api, cover_api, synopsis_api, genres_api, filmduur_api, link_api, zender_api, rating_api, starttijd_api))
    connectie.commit()

cursor.close()
connectie.close()

request_api_and_write()
xml_to_dictionary()