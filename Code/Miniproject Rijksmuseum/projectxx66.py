from tkinter import *
from tkinter import messagebox
import Jsonfiles
import json

ingelogd = ""

#functies

def login_galerij(naam, wachtwoord):
    '''checkt of de gallerijhouder bestaat, en de juiste inloggegevens heeft. Data word uit een .json gehaald.'''
    galerijdata = Jsonfiles.get_galerijdata()
    for galerij in galerijdata['Gallerijhouders']:
        if galerij['Gebruikersnaam'] == naam and galerij['Wachtwoord'] == wachtwoord:
            global ingelogd
            ingelogd = naam
            raise_frame(houder)

def leen_item(kunststuk):
    galerijdata = Jsonfiles.get_galerijdata()
    for galerij in galerijdata['Gallerijhouders']:
        if galerij['Gebruikersnaam'] == ingelogd:
            galerij['Kunst'].append(kunststuk)
            galerijdata = json.dumps(galerijdata,indent=2)
            with open('galleries.json','w') as f:
                f.writelines(galerijdata)
            kunstdata = Jsonfiles.get_kunstdata()
            for item in kunstdata:
                if item['Naam'] == kunststuk:
                    item['Available'] = False
            with open('KunstUitleen.json','w') as f:
                kunstdata = json.dumps(kunstdata,indent=2)
                f.writelines(kunstdata)
            messagebox.showinfo("Success!","Het lenen is gelukt!")


'''logt de gebruiker in. checkt enkel op een 'valide' mailadres.'''
def login_gebruiker(email):
    global ingelogd
    persoondata = Jsonfiles.get_persoondata()
    for persoon in persoondata["Persoonsgegevens"]:
        if email == persoon['Email']:
            ingelogd = email
            raise_frame(gebruiker)
    if '@' in email and ('.com' or '.nl' in email):
        ingelogd = email
        persoondata["Persoonsgegevens"].append({"Naam" : "", "Email": email, "Kunststukken": {}})
        with open ('persoonsgegevens.json', 'w') as f:
            persoondata = json.dumps(persoondata,indent=2)
            f.writelines(persoondata)
        raise_frame(gebruiker)
    else:
        messagebox.showinfo("Helaas","Dit is geen geldig mailadres. Probeer het nog eens!")
    


#Framework
def raise_frame(frame):
    frame.tkraise()

root = Tk()


main = Frame(root)
inloghouder = Frame(root)
inloggebruiker = Frame(root)
gebruiker = Frame(root)
houder = Frame(root)
nietgeleend = Frame(root)
geleend = Frame(root)
bezoekers = Frame(root)
controle = Frame(root)
selectie = Frame(root)
ticketscherm = Frame(root)

"""Hier loopt hij door de frames heen die er zijn."""

for frame in(main, inloghouder, inloggebruiker, gebruiker, houder, nietgeleend, geleend, bezoekers, controle, selectie, ticketscherm):
    frame.grid(row=0, column=0, sticky='news')


#mainscreen
"""Het hoofdscherm met buttons om te kiezen tussen gebruiker of galeriehouder."""


Label(main, text='').grid(row=0, column=1, pady=20)
Label(main, text='Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(main, text='').grid(row=2, column=1)
Button(main, text='Galeriehouder', command=lambda: raise_frame(inloghouder)).grid(row=3, column=3)
Label(main, text='').grid(row=4, column=2)
Button(main, text='Gebruiker', command=lambda: raise_frame(inloggebruiker)).grid(row=5, column=3)


#inloggen gebruiker
"""Invoeren van de gegevens van de gebruiker."""

e1 = Entry(inloggebruiker)
e2 = Entry(inloggebruiker)

e1.grid(row=3,column=7)
e2.grid(row=4,column=7)

Label(inloggebruiker, text='').grid(row=0, column=1, pady=20)
Label(inloggebruiker, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloggebruiker, text= '').grid(row=2,column=3)
Label(inloggebruiker, text= 'Naam').grid(row=3,column=5)
Label(inloggebruiker, text= 'Email adres').grid(row=4,column=5)
Label(inloggebruiker, text= '').grid(row=5,column=3)
Button(inloggebruiker, text='Login', command= lambda: login_gebruiker(e2.get())).grid(row=6,column=7)

Label(inloggebruiker, text= '').grid(row=7,column=3)
Button(inloggebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#inloggen galeriehouder
"""Invoer van de inloggegevens van de galeriehouder."""
e3 = Entry(inloghouder)
e4 = Entry(inloghouder)

e3.grid(row=3, column=7)
e4.grid(row=4, column=7)

Label(inloghouder, text='').grid(row=0, column=1, pady=20)
Label(inloghouder, text= 'Voer uw gegevens in:').grid(row=1, column=7, padx=50, pady=10)
Label(inloghouder, text= '').grid(row=2,column=3)
Label(inloghouder, text= 'Naam').grid(row=3,column=5)
Label(inloghouder, text= 'Wachtwoord').grid(row=4,column=5)
Label(inloghouder, text= '').grid(row=5,column=3)
Button(inloghouder, text='Login', command= lambda:  login_galerij(e3.get(),e4.get())).grid(row=6, column=7)

Label(inloghouder, text= '').grid(row=7,column=3)
Button(inloghouder, text= 'Terug', command= lambda: raise_frame(main)).grid(row=8, column=7)

#gebruiker
"""Het keuze scherm van de gebruiker."""

Label(gebruiker, text='').grid(row=0, column=1, pady=20)
Label(gebruiker, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(gebruiker, text='').grid(row =2, column=2)
Button(gebruiker, text= 'Kunststuk selectie', command= lambda: raise_frame(selectie)).grid(row=3, column=3)
Label(gebruiker, text='').grid(row=4, column=1)
Button(gebruiker, text= 'Ticket scherm', command= lambda: raise_frame(ticketscherm)).grid(row=5, column=3)
Label(gebruiker, text='').grid(row=6, column=3, pady=10)

Button(gebruiker, text= 'Terug', command= lambda: raise_frame(main)).grid(row=7, column=3)

#selectie

Button(selectie, text= 'Terug', command= lambda: raise_frame(gebruiker)).grid()

#ticketscherm

Button(ticketscherm, text= 'Terug', command= lambda: raise_frame(gebruiker)).grid()

#galeriehouder
"""Het keuzemenu van de galeriehouder."""

Label(houder, text='').grid(row=0, column=1)
Label(houder, text= 'Maak een keuze:').grid(row=1, column=3, padx=125, pady=10)
Label(houder, text='').grid(row=2, column=2)
Button(houder, text= 'Overzicht niet geleende kunststukken', command= lambda: raise_frame(nietgeleend)).grid(row=3, column=3)
Label(houder, text='').grid(row=4, column=2)
Button(houder, text= 'Overzicht geleende kunststukken', command= lambda: raise_frame(geleend)).grid(row=5, column=3)
Label(houder, text='').grid(row=6, column=2)
Button(houder, text= 'Overzicht van bezoekers',command= lambda: raise_frame(bezoekers)).grid(row=7, column=3)
Label(houder, text='').grid(row=8, column=2)
Button(houder, text= 'Ticketnummer controle', command= lambda: raise_frame(controle)).grid(row=9, column=3)
Label(houder, text='').grid(row=10, column=2, pady=10)
Button(houder, text= 'Terug', command= lambda: raise_frame(main)).grid(row= 11, column=3)


#nietgeleend
"""Overzicht van alle niet geleende kunststukken, mogelijkheid tot lenen."""

Label(nietgeleend, text='Overzicht niet geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(nietgeleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(nietgeleend, yscrollcommand = scrollbar.set )
for kunstwerk in Jsonfiles.get_kunstdata():
    if kunstwerk['Available'] == True:
        mylist.insert(END, kunstwerk['Naam'])

mylist.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist.yview )

Button(nietgeleend, text= 'Lenen', command= lambda: leen_item(mylist.get(mylist.curselection()))).pack(pady=5)
Button(nietgeleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=5)
selectmode = SINGLE

#geleend
"""Overzicht van alle geleende kunststukken."""

Label(geleend, text='Overzicht geleende kunststukken:').pack(pady=20)
scrollbar = Scrollbar(geleend)
scrollbar.pack(side=RIGHT, fill=Y)

mylist2 = Listbox(geleend, yscrollcommand = scrollbar.set )
for kunstwerk in Jsonfiles.get_kunstdata():
    if kunstwerk['Available'] == False:
        mylist2.insert(END, kunstwerk['Naam'])

mylist2.pack(expand=1, fill=BOTH)
scrollbar.config( command = mylist2.yview )

Button(geleend, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)
selectmode = SINGLE

#bezoekers
"""Overzicht van alle bezoekers."""

Label(bezoekers, text='Overzicht van bezoekers:').pack(pady=20)
scrollbar = Scrollbar(bezoekers)
scrollbar.pack(side=RIGHT, fill=Y)

listbox= Listbox(bezoekers)
listbox.pack(expand=1, fill=BOTH)

for i in range(1001):                  #ToDo hier moet len van de lijst zijn, dus eerst regels opvragen
    listbox.insert(END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Button(bezoekers, text= 'Terug', command= lambda: raise_frame(houder)).pack(pady=10)


#controle
"""Hier kunnen de afgegeven codes van het ticketscherm worden gecontroleerd."""

Label(controle, text= '').grid(row=1, column=0, pady=20)
Label(controle, text='Voer hier de code in:').grid(row=2, column=3, padx=125, pady=10)
e1 = Entry(controle)
e1.grid(row=3, column=3)
Label(controle, text= '').grid(row=4, column=0)
Button(controle, text='Check').grid(row=5, column=3)

Label(controle, text= '').grid(row=6, column=0)
Button(controle, text= 'Terug', command= lambda: raise_frame(houder)).grid(row=7, column=3)


root.title('')
root.geometry('360x360')
raise_frame(main)
root.mainloop()

