from tkinter import *
import functies

def bezoekerKlik():
    ''' Hier destroyen wij de knoppen die je gebruikt om te kiezen voor bezoeker of aanbieder '''
    bezoekerButton.destroy()
    aanbiederButton.destroy()
    ''' deze functie wordt aangeroepen bij het klikken op de knop van welke aanbieder, we geven hier de waarde mee met lambda'''
    def show_films(naam):
        '''we destroyen hier weer knoppen en titels die gebruikt worden in het scherm om een aanbieder aan te klikken'''
        aanbiederTitel.destroy();ButtonDennis.destroy();ButtonTarik.destroy();ButtonMitchel.destroy();ButtonRik.destroy();        ButtonDavid.destroy()
        '''we nemen hier een variabele die we de waarde die we in de functie meegeven toekennnen
        en daarna maken we gebruik van MYSQL syntax om de waardes van aanbieders te gebruiken waar
        naam van de aanbieder overeenkomt met de meegegeven waarde
        '''
        ingevoerde_naam = naam
        kies_aanbieder_query = ('SELECT * FROM aanbieders WHERE aanbieders.naam =%s')
        functies.cursor.execute(kies_aanbieder_query, (ingevoerde_naam,))
        naam = Label(text="U heeft gekozen voor: " + naam)
        naam.grid()
        for row in functies.cursor:
            film = row[3]
            aanbieder_id = row[0]
        '''Film informatie ophalen en vervolgens showen'''
        film_informatie = ("SELECT * FROM films WHERE titel=%s")
        functies.cursor.execute(film_informatie, (film,))
        film_gegevens = []
        for row in functies.cursor:
            for i in range(0,9):
                film_gegevens.append(row[i])
        if not film_gegevens:
            leeg_label = Label(text="De gekozen aanbieder vertoont momenteel geen film")
            leeg_label.grid()
        else:
            titel_label = Label(text=film_gegevens[1]);synopsis_label = Label(text=film_gegevens[3]);genre_label = Label(text=film_gegevens[4]);duur_label = Label(text=film_gegevens[5]);rating_label = Label(text=film_gegevens[8]);starttijd_label = Label(text=film_gegevens[9]);
            titel_label.grid();synopsis_label.grid();genre_label.grid();duur_label.grid();rating_label.grid();starttijd_label.grid();
            knop = Button(text="Reserveren", command=lambda: reserveer(ingevoerde_naam, film_gegevens[1]))
            knop.grid()
        '''functie om film te reserveren, zet tegelijk de reservering in de MYSQL database'''
        def reserveer(naam, film):
            def reserveerfunctie():
                bezoeker_naam = bezoeker_naam1.get()
                bezoeker_email = bezoeker_email1.get()
                bezoeker_email_label.destroy();bezoeker_email1.destroy();bezoeker_naam1.destroy();bezoeker_naam_label.destroy();reserveer_button.destroy()
                eticket = bezoeker_naam + film_gegevens[1]
                eticket_ascii = [ord(i) for i in eticket]
                for i in range(len(eticket_ascii)):
                    eticket_ascii[i] += 3
                code = [chr(b) for b in eticket_ascii]
                code = ''.join(code)
                bezoeker_insert = ("INSERT INTO bezoekers (naam, email, aanbiederid, uniekecode) VALUES (%s, %s, %s, %s)")
                functies.cursor.execute(bezoeker_insert, (bezoeker_naam,bezoeker_email, aanbieder_id, code, ))
                functies.connectie_met_mysql.commit()
                UniekeCodeLabel = Label(root, text="Uw unieke code is: " + code)
                UniekeCodeLabel.grid()


            titel_label.destroy();synopsis_label.destroy();genre_label.destroy();duur_label.destroy();rating_label.destroy();starttijd_label.destroy();knop.destroy()
            Nieuw = Label(text="U heeft gereserveerd voor de film " + film + " Van aanbieder " + naam )
            bezoeker_naam_label = Label(text="Uw naam");bezoeker_naam1 = Entry()
            bezoeker_email_label = Label(text="Uw email");bezoeker_email1 = Entry()
            bezoeker_naam_label.grid();bezoeker_naam1.grid();bezoeker_email_label.grid();bezoeker_email1.grid()

            reserveer_button = Button(text="Reserveer", command=reserveerfunctie)
            reserveer_button.grid()
            Nieuw.grid()



        print(film)

    '''hier zijn alle knoppen en labels op het scherm gebracht'''
    aanbiederTitel = Label(text="Hier kunt u uw aanbieder kiezen")
    aanbiederTitel.grid(row=0, column=0)
    ButtonDennis = Button(text="Dennis", command= lambda: show_films("Dennis"))
    ButtonTarik = Button(text="Tarik", command= lambda: show_films("Tarik"))
    ButtonMitchel = Button(text="Mitchel", command= lambda: show_films("Mitchell"))
    ButtonDavid = Button(text="David", command= lambda: show_films("David"))
    ButtonRik = Button(text="Rik", command= lambda: show_films("Rik"))
    ButtonDennis.grid(row=0, column=1)
    ButtonTarik.grid(row=0, column=2)
    ButtonMitchel.grid(row=0, column=3)
    ButtonDavid.grid(row=0, column=4)
    ButtonRik.grid(row=0, column=5)

'''Deze functie is gemaakt voor als er op de aanbieder knop gedrukt wordt'''
def aanbiederKlik():
    '''Hier verwijderen wij de knoppen en declareren wij foute inlog voor als we deze nog willen gebruiken in het fout inloggen'''
    bezoekerButton.destroy()
    aanbiederButton.destroy()
    meldingFoutInlog = Label(text="Foute inlog")

    '''Functie om in te loggen in het aanbieder scherm'''
    def log_in():
        NaamOphalen = NaamE.get()
        WachtwoordOphalen = WachtwoordE.get()
        if NaamOphalen in functies.username_wachtwoord:
            if WachtwoordOphalen == functies.username_wachtwoord[NaamOphalen]:
                NaamL.destroy()
                WachtwoordL.destroy()
                NaamE.destroy()
                WachtwoordE.destroy()
                inlogButton.destroy()
                meldingFoutInlog.destroy()


                UsernameL = Label(text="Aanbieder naam is: " + NaamOphalen)
                UsernameL.grid()

                '''haal films op'''
                films_query = ("SELECT * FROM films")
                functies.cursor.execute(films_query)
                films = []
                '''zet films in list'''
                for row in functies.cursor:
                    films.append(row[1])
                film_keuze = Label(text="Kies een film uit onderstaande lijst: ")
                film_keuze.grid()
                filmlist = Listbox(root)
                for i in range(len(films)):
                    filmlist.insert(i, films[i-1])
                filmlist.grid()
                ''' Aanbieder kiest film en er wordt geshowed welke film er gekozen is'''
                def keuzeKlik(x):
                    values = [filmlist.get(idx) for idx in filmlist.curselection()]
                    if len(values) == 1:
                        filmlist.destroy()
                        film_keuze.destroy()
                        laat_bezoekers_zien_knop.destroy()
                        filmgekozen = Label(text="U heeft " + values[0] + " gekozen")
                        filmgekozen.grid()
                    films_in_gebruik_query = ("SELECT film FROM aanbieders")
                    functies.cursor.execute(films_in_gebruik_query)
                    films_in_gebruik = []
                    for row in functies.cursor:
                        films_in_gebruik.append(row[0])
                    x = 0
                    '''Controleren of film in gebruik is'''
                    while values[0] in films_in_gebruik:
                        filmgekozen.destroy()
                        film_in_gebruik_label = Label(text="De film is in gebruik")
                        film_in_gebruik_label.grid()
                        x = x + 1
                        if x == 1:
                            break
                    '''Als film niet in gebruik is, neem hem dan bezet'''
                    while values[0] not in films_in_gebruik:
                        maak_bezet_query = ("UPDATE aanbieders SET film=%s WHERE naam=%s")
                        functies.cursor.execute(maak_bezet_query, (values[0], NaamOphalen))
                        functies.connectie_met_mysql.commit()
                        x = x + 1
                        if x == 1:
                            break
                ''' lijst om films uit te zien'''
                filmlist.bind('<<ListboxSelect>>', keuzeKlik)

                '''bezoekers laten zien die bij de aanbieder horen die ingelogd is'''
                def laat_bezoekers_zien_functie():
                    filmlist.destroy()
                    film_keuze.destroy()
                    UsernameL.destroy()
                    laat_bezoekers_zien_knop.destroy()
                    gebruikers_bij_aanbieder_query = ("SELECT * FROM bezoekers")
                    functies.cursor.execute(gebruikers_bij_aanbieder_query)
                    bezoekerslijst = {}
                    for row in functies.cursor:
                        bezoekerslijst[row[1]] = row[3]
                    ''' Alles uit aanbieders halen '''
                    aanbieders_query = ("SELECT * FROM aanbieders")
                    functies.cursor.execute(aanbieders_query)
                    aanbiedersidlijst = {}
                    for row in functies.cursor:
                        aanbiedersidlijst[row[1]] = row[0]

                    ''' controleren welke aanbieders id van de bezoeker hoort bij welke aannbieder hoort
                     ook wordt er gecontroleerd welke aanbieder ingelogd is dus er wordt pas geshowed als de aanbieder en zijn id
                     overeenkomen met de bezoeker waar een aanbieder id bij hoort
                     '''

                    for i, k in bezoekerslijst.items():
                        naam = i
                        naamid = k

                        for i, k in aanbiedersidlijst.items():
                            if i == NaamOphalen:
                                if k == naamid:
                                    labelBezoekers = Label(root, text=naam)
                                    labelBezoekers.grid()
                ''' Knop van bezoekers laten zien met functie oproep'''
                laat_bezoekers_zien_knop = Button(text="Laat bezoekers zien", command=laat_bezoekers_zien_functie)
                laat_bezoekers_zien_knop.grid()
                ''' Als wachtwoord niet klopt komt er een return met foute inlog'''
            else:
                meldingFoutInlog.grid()


    ''' Naam invoeren knoppen samen met invoer mogelijkheden'''
    NaamL = Label(text="Naam:", font=("Helvetica", 28))
    WachtwoordL = Label(text="Wachtwoord:", font=("Helvetica", 28))

    NaamE = Entry()
    WachtwoordE = Entry()



    inlogButton = Button(text="Inloggen", command=log_in, width=10, height=5, bg="green")

    NaamL.grid(row=0, column=0)
    WachtwoordL.grid(row=1, column=0)
    NaamE.grid(row=0, column=1)
    WachtwoordE.grid(row=1, column=1)
    inlogButton.grid(row=2, columnspan=4)
''' Het hoofdscherm'''
root = Tk()
'''Eerste scherm met knoppen'''
bezoekerButton = Button(root, text="Bezoeker", command=bezoekerKlik, height=25, width=50, bg="yellow", font=("Helvetica", 20))
aanbiederButton = Button(root, text="Aanbieder", command=aanbiederKlik, height=25, width=50, bg="green", font=("Helvetica", 20))
bezoekerButton.grid(row=0, column=0)
aanbiederButton.grid(row=0, column=1)
root.mainloop()