__author__ = 'David'
import requests
import datetime
import codecs
import xmltodict
# Misschien soort geschiedenis van films bijhouden. Elke dag api opslaan in nieuwe file met datum naam
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
def verwerk_xml():
    bestand = open('films.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)
film_dict = verwerk_xml()

for i in range(6):
    print('Titel: ' + film_dict['filmsoptv']['film'][i]['titel'] + '\nJaar: ' + film_dict['filmsoptv']['film'][i]['jaar'] + '\nCast:' + film_dict['filmsoptv']['film'][i]['cast'] + '\n')


