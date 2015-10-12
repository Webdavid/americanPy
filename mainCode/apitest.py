__author__ = 'David'
import requests
import datetime
import codecs
def verbind_en_schrijf():
    datum = datetime.date.today();datum = datum.strftime("%d-%m-%Y")
    try:
        request = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=qx4ugph3my32lh95qf4wixt7zxo9qee5&dag=' + datum + '&sorteer=0')
        bestand = open('films.xml', 'w')
        bestand.write(str(request.text))
        bestand.close()
    except:
        print("Het is mislukt de gegevens op te halen.")
verbind_en_schrijf()