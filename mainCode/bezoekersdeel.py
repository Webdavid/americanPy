__author__ = 'rikru'
import requests
import codecs
import xmltodict
from time import strftime
from urllib import request
import tkinter as tk
from PIL import ImageTk, Image

datum = strftime("%d-%m-%Y") #haalt de huidige dag, maand en jaar op.
response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=qx4ugph3my32lh95qf4wixt7zxo9qee5&dag=' + datum + '&sorteer=0')
#haalt de response van de api op.

def schrijf_xml(reponse): #deze functie schijft de response in een xml bestand.
    bestand = codecs.open('filmlijst.xml', "w", "utf-8")
    bestand.write(str(response.text))
    bestand.close()


def verwerk_xml(): #deze functie leest het xml bestand en returned alle waardes die aangeroepen worden.
    bestand = open('filmlijst.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)


def aanbiederkeuze(aanbieder): #functie om te kiezen tussen de aanbieders.
    if aanbieder in aanbieders:
        print('U heeft', aanbieder, 'als aanbieder gekozen.')
        print('Selecteer een van de volgende films:')
        filmkeuze()


def filmkeuze(): #functie die de films koppelt aan de aanbieders en deze laat zien.
    if aanbieder == 'Rik':
        for i in range(0, 2):
            print(films_dict['filmsoptv']['film'][i]['titel']) #print titel
            print(films_dict['filmsoptv']['film'][i]['starttijd']) #print starttijd
            #print(films_dict['filmsoptv']['film'][i]['cover']) #print cover
    elif aanbieder == 'Tarik':
        print(films_dict['filmsoptv']['film'][2]['titel'])
        #print(films_dict['filmsoptv']['film'][2]['cover'])
        print(films_dict['filmsoptv']['film'][2]['starttijd'])
    elif aanbieder == 'Mitchell':
        print(films_dict['filmsoptv']['film'][3]['titel'])
        #print(films_dict['filmsoptv']['film'][3]['cover'])
        print(films_dict['filmsoptv']['film'][3]['starttijd'])
    elif aanbieder == 'David':
        for i in range(4, 6):
            print(films_dict['filmsoptv']['film'][i]['titel'])
            #print(films_dict['filmsoptv']['film'][i]['cover'])
            print(films_dict['filmsoptv']['film'][i]['starttijd'])
    elif aanbieder == 'Dennis':
        print(films_dict['filmsoptv']['film'][6]['titel'])
        print(films_dict['filmsoptv']['film'][6]['cover'])
        print(films_dict['filmsoptv']['film'][6]['starttijd'])


def film_selected(): #Als film aangeklikt wordt. Dit achter button per film doen met i van 0 t/m 6.
    print('Genre:', films_dict['filmsoptv']['film'][i]['genre'])
    print('Duur:', films_dict['filmsoptv']['film'][i]['duur'], 'minuten')
    print('Rating:', films_dict['filmsoptv']['film'][i]['imdb_rating'] + '/10')
    print('Votes:', films_dict['filmsoptv']['film'][i]['imdb_votes'])
    print('Synopsis:', films_dict['filmsoptv']['film'][i]['synopsis'])


def reserveren(): #als op button geklikt word met reserveren geef dan de ingevoerde naam en een qr code terug.
    print(naam)
    #print(qrcode)


schrijf_xml(response)
films_dict = verwerk_xml()

naam = input("Voer uw naam in: ") #invoer naam aan het begin van het programma
mail = input("Voer uw e-mail in: ") #invoer email aan het begin van het programma

aanbieders = ['Rik', 'Tarik', 'Dennis', 'Mitchell', 'David'] #de lijst met aanbieders
print(aanbieders) #print de lijst met aanbieders, kan worden getoont in buttons en is later dus overbodig.
aanbieder = input('Selecteer een aanbieder:') #gebruiker selecteert een aanbieder, met buttons ook overbodig.
aanbiederkeuze(aanbieder) # roept funcite aan die de keuze van de gebruiker bevestigt.
reserveren() #roept reserveren aan wanneer bij een film de knop reserveren ingedrukt wordt.

f = open('film1.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][0]['cover']).read())
f.close()
f = open('film2.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][1]['cover']).read())
f.close()
f = open('film3.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][2]['cover']).read())
f.close()
f = open('film4.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][3]['cover']).read())
f.close()
f = open('film5.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][4]['cover']).read())
f.close()
f = open('film6.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][5]['cover']).read())
f.close()
f = open('film7.jpg', 'wb')
f.write(request.urlopen(films_dict['filmsoptv']['film'][6]['cover']).read())
f.close()

window = tk.Tk()
window.title("Films")
window.geometry("1000x1000")
window.configure(background='grey')

path = "film1.jpg"
path2 = "film2.jpg"
path3 = "film3.jpg"
path4 = "film4.jpg"
path5 = "film5.jpg"
path6 = "film6.jpg"
path7 = "film7.jpg"

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=img)
panel.pack(side="left", fill="both", expand="yes")


img2 = ImageTk.PhotoImage(Image.open(path2))
panel = tk.Label(window, image=img2)
panel.pack(side="left", fill="both", expand="yes")
img3 = ImageTk.PhotoImage(Image.open(path3))
panel = tk.Label(window, image=img3)
panel.pack(side="left", fill="both", expand="yes")
img4 = ImageTk.PhotoImage(Image.open(path4))
panel = tk.Label(window, image=img4)
panel.pack(side="left", fill="both", expand="yes")
img5 = ImageTk.PhotoImage(Image.open(path5))
panel = tk.Label(window, image=img5)
panel.pack(side="left", fill="both", expand="yes")
img6 = ImageTk.PhotoImage(Image.open(path6))
panel = tk.Label(window, image=img6)
panel.pack(side="left", fill="both", expand="yes")
img7 = ImageTk.PhotoImage(Image.open(path7))
panel = tk.Label(window, image=img7)
panel.pack(side="left", fill="both", expand="yes")
window.mainloop()

#webbrowser.open(films_dict['filmsoptv']['film'][5]['cover']) #opent browser met jpg cover.